"""Casos observables de los laboratorios y del sitio final."""
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.parse import urlsplit, parse_qs
from playwright.sync_api import sync_playwright
import os, html5lib, tinycss2

ROOT=Path(__file__).resolve().parents[1]
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT)))
Thread(target=server.serve_forever,daemon=True).start()
base=f'http://127.0.0.1:{server.server_port}/'
count=0
def require(condition,message):
    global count
    assert condition,message
    count+=1

def css_errors(tokens):
    found=[]
    for t in tokens:
        if t.type=='error': found.append(t.message)
        for attr in ('content','arguments'):
            if getattr(t,attr,None): found.extend(css_errors(getattr(t,attr)))
    return found

try:
    for path in ROOT.rglob('*.html'):
        parser=html5lib.HTMLParser();parser.parse(path.read_text(encoding='utf-8'))
        require(not parser.errors, f'{path.relative_to(ROOT)}: reparaciones HTML5 {parser.errors}')
    for path in ROOT.rglob('*.css'):
        tokens=tinycss2.parse_stylesheet(path.read_text(encoding='utf-8'),skip_whitespace=True,skip_comments=True)
        require(not css_errors(tokens), f'{path.relative_to(ROOT)}: sintaxis CSS')
    with sync_playwright() as pw:
        engine=os.environ.get('COURSE_BROWSER','firefox')
        browser=getattr(pw,engine).launch()
        context=browser.new_context(viewport={'width':1280,'height':900})
        page=context.new_page();bad=[]
        page.on('response',lambda r:bad.append(r.url) if r.status>=400 and r.url.startswith(base) else None)
        def open_(path):
            page.goto(base+path,wait_until='networkidle')
        units=sorted(p.name for p in ROOT.glob('unidad*') if p.is_dir())
        def lab(i): open_(units[i]+'/ejemplo/index.html')
        def compute(selector,prop): return page.locator(selector).evaluate('(e,p)=>getComputedStyle(e).getPropertyValue(p)',prop)
        # Cada ejemplo se carga y la página no desborda a 320, 768 y 1440 px.
        for i in range(31):
            lab(i)
            for width in (320,768,1440):
                page.set_viewport_size({'width':width,'height':900})
                require(page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),f'Unidad {i}: desbordamiento a {width}')
        page.set_viewport_size({'width':1280,'height':900})
        lab(9)
        require(compute('.destacado','color')=='rgb(159, 18, 57)','cascada destacado')
        require(compute('.aviso:not(.destacado)','color')=='rgb(22, 101, 52)','cascada aviso')
        lab(10)
        require(compute('.panel > p','background-color')=='rgb(240, 249, 255)','selector hijo')
        lab(11)
        require(page.locator('.contenido').bounding_box()['width']==250,'content-box 250')
        require(page.locator('.borde').bounding_box()['width']==200,'border-box 200')
        lab(17)
        page.set_viewport_size({'width':320,'height':900})
        require(len(compute('.galeria','grid-template-columns').split())==1,'Grid una columna')
        page.set_viewport_size({'width':1440,'height':900})
        require(len(compute('.galeria','grid-template-columns').split())>=3,'Grid amplio')
        lab(20)
        page.set_viewport_size({'width':320,'height':900})
        require(len(compute('.agenda','grid-template-columns').split())==1,'query estrecha')
        page.set_viewport_size({'width':1440,'height':900})
        require(len(compute('.agenda','grid-template-columns').split())==2,'query amplia')
        lab(21)
        page.set_viewport_size({'width':320,'height':900})
        page.wait_for_function("document.querySelector('img').currentSrc.includes('aula-cuadrada.svg')")
        require('aula-cuadrada.svg' in page.locator('img').evaluate('(e)=>e.currentSrc'),'picture estrecho')
        lab(22)
        require(compute('.tema a','color')=='rgb(107, 33, 168)','variable heredada')
        lab(24);page.emulate_media(reduced_motion='reduce')
        require(compute('.tarjeta','transition-duration')=='0s','movimiento reducido')
        page.emulate_media(reduced_motion='no-preference')
        lab(7)
        page.get_by_role('button').click()
        require('/index.html' in page.url,'formulario vacío permanece')
        page.get_by_label('Nombre ficticio').fill('Ana')
        page.get_by_label('Correo ficticio').fill('incorrecto')
        page.get_by_label('Lectura',exact=True).check()
        require(not page.locator('form').evaluate('(e)=>e.checkValidity()'),'correo inválido')
        page.get_by_label('Correo ficticio').fill('ana@example.com')
        page.get_by_role('button').click();page.wait_for_url('**/resultado.html?*')
        require(parse_qs(urlsplit(page.url).query)['taller']==['lectura'],'GET taller')
        # Proyecto final: páginas, fragmentos, validación, teclado y contenido variable.
        project='ejemplos/sitio-final/'
        for name in ('index.html','talleres.html','contacto.html','resultado.html','404.html'):
            open_(project+name)
            for width in (320,768,1440):
                page.set_viewport_size({'width':width,'height':900})
                require(page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),name+': reflujo')
            page.add_style_tag(content='html { font-size: 200%; }')
            page.set_viewport_size({'width':320,'height':900})
            require(page.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),name+': fuente 200%')
        page.set_viewport_size({'width':1280,'height':900})
        open_(project+'index.html');page.keyboard.press('Tab')
        require(page.evaluate('document.activeElement.className')=='saltar','primer Tab salto')
        require(page.locator('.saltar').bounding_box()['y']>=0,'salto visible')
        page.keyboard.press('Enter')
        require(page.evaluate('document.activeElement.id')=='contenido','salto enfoca main')
        page.get_by_role('link',name='Ver el taller de robótica').click()
        require(page.url.endswith('talleres.html#robotica'),'destino de tarjeta')
        summary=page.get_by_text('¿Necesito experiencia previa?',exact=True)
        summary.focus();page.keyboard.press('Enter')
        require(page.locator('details').first.get_attribute('open') is not None,'details teclado')
        open_(project+'contacto.html')
        page.get_by_role('button').click();require(page.url.endswith('contacto.html'),'contacto vacío')
        page.get_by_label('Nombre ficticio').fill('Ana')
        page.get_by_label('Correo ficticio').fill('ana@example.com')
        page.get_by_label('Robótica',exact=True).check()
        page.get_by_label('Mensaje ficticio').fill('corto')
        require(not page.locator('form').evaluate('(e)=>e.checkValidity()'),'mensaje corto')
        page.get_by_label('Mensaje ficticio').fill('Quiero practicar una consulta.')
        require(page.locator('form').evaluate('(e)=>e.checkValidity()'),'datos completos')
        page.get_by_role('button').click();page.wait_for_url('**/resultado.html?*')
        require(page.get_by_text('No se envió un mensaje.',exact=True).is_visible(),'resultado honesto')
        require(parse_qs(urlsplit(page.url).query)['taller']==['robotica'],'opción enviada')
        # Prueba del proyecto independiente copiado: sus recursos no salen de la carpeta.
        import shutil,tempfile
        with tempfile.TemporaryDirectory() as td:
            dest=Path(td)/'sitio';shutil.copytree(ROOT/'ejemplos/sitio-final',dest)
            local=context.new_page();local.goto((dest/'index.html').as_uri())
            require(local.locator('img').evaluate('(e)=>e.complete && e.naturalWidth>0'),'imagen portable')
            local.get_by_role('link',name='Talleres',exact=True).click()
            require(local.url.endswith('talleres.html'),'navegación portable')
            local.close()
        require(not bad,'recursos HTTP fallidos '+repr(bad))
        browser.close()
    print(f'Correcto: {count} comprobaciones de estructura, estilos y comportamiento ({engine}).')
finally:
    server.shutdown();server.server_close()
