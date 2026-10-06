"""Comprueba integridad de rutas, navegación y documentos del curso."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re

ROOT=Path(__file__).resolve().parents[1]
errors=[]
links=0
class Document(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.refs=[]; self.lang=None; self.titles=0; self.h1=0; self.labels=[]; self.controls=[]; self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='html': self.lang=a.get('lang')
        if tag=='title': self.titles+=1
        if tag=='h1': self.h1+=1
        if tag=='label' and a.get('for'): self.labels.append(a['for'])
        if tag in ('input','textarea','select'): self.controls.append(a)
        if tag=='img': self.images.append(a)
        for k in ('href','src','action'):
            if k in a: self.refs.append(a[k])
        if 'srcset' in a:
            self.refs.extend(x.strip().split()[0] for x in a['srcset'].split(',') if x.strip())
        for k in ('aria-labelledby','aria-describedby'):
            if k in a: self.refs.extend('#'+x for x in a[k].split())

htmls={}
for p in ROOT.rglob('*.html'):
    d=Document();d.feed(p.read_text(encoding='utf-8'));htmls[p.resolve()]=d
    if d.lang!='es' or d.titles!=1 or d.h1!=1: errors.append(f'{p.relative_to(ROOT)}: lang/title/h1')
    if len(d.ids)!=len(set(d.ids)): errors.append(f'{p.relative_to(ROOT)}: ids duplicados')
    for image in d.images:
        if 'alt' not in image: errors.append(f'{p.relative_to(ROOT)}: imagen sin alt')
    for target in d.labels:
        if target not in d.ids: errors.append(f'{p.relative_to(ROOT)}: label sin control {target}')

def check(source,url):
    global links
    url=url.strip().split(' ')[0]
    parts=urlsplit(url)
    if parts.scheme or parts.netloc: return
    links+=1
    dest=(source.parent/unquote(parts.path)).resolve() if parts.path else source.resolve()
    if dest.is_dir():
        dest=next((dest/n for n in ('README.md','index.html') if (dest/n).is_file()),dest)
    if not dest.exists(): errors.append(f'{source.relative_to(ROOT)}: destino inexistente {url}');return
    if parts.fragment and dest in htmls and unquote(parts.fragment) not in htmls[dest].ids:
        errors.append(f'{source.relative_to(ROOT)}: fragmento inexistente {url}')

for p,d in htmls.items():
    for url in d.refs: check(p,url)
for p in ROOT.rglob('*.css'):
    for url in re.findall(r'url\(["\']?([^\)"\']+)',p.read_text(encoding='utf-8')): check(p,url)
for p in ROOT.rglob('*.md'):
    s=p.read_text(encoding='utf-8')
    if len(re.findall(r'^```',s,re.M))%2: errors.append(f'{p.relative_to(ROOT)}: bloque sin cierre')
    prose=re.sub(r'^```[^\n]*\n.*?^```[^\n]*$', '', s, flags=re.M|re.S)
    for url in re.findall(r'\[[^\]]*\]\(([^)]+)\)',prose): check(p,url)

units=sorted(ROOT.glob('unidad*/README.md'))
for i,p in enumerate(units):
    s=p.read_text(encoding='utf-8')
    for name in ('PRACTICA.md','SOLUCIONES.md'):
        if not (p.parent/name).is_file() or name not in s: errors.append(f'{p.parent.name}: recurso de práctica ausente {name}')
    if i+1<len(units) and units[i+1].parent.name not in s: errors.append(f'{p.parent.name}: falta siguiente')
    if i and units[i-1].parent.name not in s: errors.append(f'{p.parent.name}: falta anterior')
    if '../README.md' not in s: errors.append(f'{p.parent.name}: falta índice')
assert len(units)==33, 'Se esperan 33 unidades'
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Correcto: {len(units)} unidades, {len(htmls)} documentos HTML y {links} destinos locales comprobados.')
print('No comprueba URLs externas, renderizado completo ni todos los criterios de accesibilidad.')
