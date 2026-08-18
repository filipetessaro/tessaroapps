# Migra as paginas legais dos repos antigos para o site unico `tessaroapps`.
#
# Cada pagina vira uma PASTA com index.html, porque o GitHub Pages nao serve
# extensao implicita de forma confiavel. Isso muda a profundidade de cada
# arquivo, entao todo link interno e todo asset precisa ser reescrito -- e e
# por isso que isto e um script, e nao 23 edicoes na mao.
#
# O conteudo das paginas nao e tocado: sao textos legais ja aceitos por loja.

import io
import os
import re
import shutil

RAIZ = r'c:/Users/tessa/OneDrive/Documents/CloudeCode'
TMP = r'c:/Users/tessa/AppData/Local/Temp/claude/c--Users-tessa-OneDrive-Documents-CloudeCode/d7748e6c-689c-4886-8b78-2a57565c88a8/scratchpad'
DESTINO = os.path.join(RAIZ, 'tessaroapps')

# origem -> { arquivo: caminho relativo a raiz do app ('' = index do app) }
APPS = {
    'iris': {
        'src': os.path.join(RAIZ, 'iris-privacy'),
        'paginas': {
            'index.html': '',
            'privacy.html': 'privacy',
            'terms.html': 'terms',
            'delete-account.html': 'delete-account',
            'psicologos.html': 'psicologos',
        },
        'assets': ['style.css', 'icon.png'],
    },
    'plantscan': {
        'src': os.path.join(RAIZ, 'plantscan-ai-legal'),
        'paginas': {
            'index.html': '',
            'privacy-policy.html': 'privacy',
            'terms-of-use.html': 'terms',
        },
        'assets': [],
    },
    'coinsnap': {
        # O index.html deste repo E a politica de privacidade: nao ha landing.
        'src': os.path.join(RAIZ, 'coin-value-snap-privacy'),
        'paginas': {
            'index.html': 'privacy',
            'delete-account.html': 'delete-account',
        },
        'assets': [],
    },
    'photoevolve': {
        'src': os.path.join(RAIZ, 'photoevolve-site'),
        'paginas': {
            'index.html': '',
            'privacy.html': 'privacy',
            'terms.html': 'terms',
            'delete-account.html': 'delete-account',
            'index-en.html': 'en',
            'privacy-en.html': 'en/privacy',
            'terms-en.html': 'en/terms',
            'delete-account-en.html': 'en/delete-account',
            'index-es.html': 'es',
            'privacy-es.html': 'es/privacy',
            'terms-es.html': 'es/terms',
            'delete-account-es.html': 'es/delete-account',
        },
        'assets': ['style.css'],
    },
    'garagerank': {
        # Idem: o index e a politica.
        'src': os.path.join(TMP, 'garagerank-legal'),
        'paginas': {'index.html': 'privacy'},
        'assets': [],
    },
    'inbloom': {
        # index.html e privacy-policy.html sao byte a byte o mesmo arquivo.
        'src': os.path.join(TMP, 'inbloom-app-legal'),
        'paginas': {'privacy-policy.html': 'privacy'},
        'assets': [],
    },
}


def reescrever(html, paginas, assets, destino_rel):
    """Ajusta links internos e assets para a nova profundidade do arquivo."""
    subir = '../' * (destino_rel.count('/') + 1) if destino_rel else ''

    def alvo(arquivo):
        rel = paginas[arquivo]
        return (subir + rel + '/') if rel else (subir or './')

    def troca(m):
        attr, aspas, valor = m.group(1), m.group(2), m.group(3)
        if valor in paginas:
            return f'{attr}={aspas}{alvo(valor)}{aspas}'
        if valor in assets:
            return f'{attr}={aspas}{subir}{valor}{aspas}'
        return m.group(0)

    return re.sub(r'(href|src)=(["\'])([^"\']+)\2', troca, html)


def migrar():
    for app, cfg in APPS.items():
        for arquivo, rel in cfg['paginas'].items():
            origem = os.path.join(cfg['src'], arquivo)
            pasta = os.path.join(DESTINO, app, *rel.split('/')) if rel else os.path.join(DESTINO, app)
            os.makedirs(pasta, exist_ok=True)
            html = io.open(origem, encoding='utf-8').read()
            html = reescrever(html, cfg['paginas'], cfg['assets'], rel)
            io.open(os.path.join(pasta, 'index.html'), 'w', encoding='utf-8').write(html)
            print(f'  /{app}/{rel + "/" if rel else ""}  <- {arquivo}')
        for asset in cfg['assets']:
            shutil.copy2(os.path.join(cfg['src'], asset), os.path.join(DESTINO, app, asset))
            print(f'  /{app}/{asset}')


migrar()
