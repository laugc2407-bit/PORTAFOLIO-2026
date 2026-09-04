import base64
import io
from pathlib import Path

import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Las imágenes/videos están directamente en la raíz del repositorio
# (la misma carpeta donde vive este script), así que buscamos ahí y no
# en una subcarpeta "assets/".
ASSETS = Path(__file__).parent

st.set_page_config(
    page_title="Portafolio",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


SITE = {
    "nombre": "Laura García",
    "titulo_hero_1": "PORTAFOLIO",
    "titulo_hero_2": "CREATIVO",
    "eyebrow": ["portafolio", "diseño", "interactivo"],  # las 3 palabras de la barra superior
    "tagline": "Diseño de experiencias interactivas, mundos inmersivos y visuales que se sienten.",
}

NAV = [
    ("Sobre mí", "sobre-mi"),
    ("Herramientas", "herramientas"),
    ("Inmersivos", "inmersivos"),
    ("Interfaces", "interfaces"),
    ("Visual", "visual"),
    ("Investigación", "investigacion"),
    ("Contacto", "contacto"),
]

ABOUT = {
    "titulo": "SOBRE MÍ",
    "texto": """
Me gusta crear cosas que hagan que las personas **quieran interactuar con ellas**.

Soy estudiante de Diseño Interactivo y disfruto moverme entre diferentes formas de crear: desde pensar una experiencia y diseñar una interfaz, hasta modelar un objeto en 3D, experimentar con código o convertir una idea en algo que se pueda jugar, explorar y vivir.

Me interesa especialmente ese punto donde **el diseño y la tecnología se encuentran con lo humano**. Por eso no busco hacer proyectos que simplemente se vean bien, sino experiencias que tengan una intención, despierten curiosidad y dejen algo en quien las vive.

Soy curiosa, aprendo haciendo y no me da miedo meterme en herramientas o áreas nuevas para llevar una idea un paso más allá.

**En pocas palabras: me gusta imaginar posibilidades y después descubrir cómo hacerlas realidad.**
""",
    # Coloca tu foto en la raíz del repo: perfil.jpg
    "imagen": "perfil.jpg",
}

# Para cada herramienta puedes (opcional) poner un logo en tools/<archivo>
# (la carpeta "tools" dentro de la raíz del repo)
# Si el archivo no existe, se muestra una "ficha" con el nombre en texto,
# así que puedes dejarlo así de fácil sin subir ningún logo.
TOOLS = [
    {"nombre": "Illustrator", "archivo": "ai.png"},
    {"nombre": "Photoshop", "archivo": "ps.png"},
    {"nombre": "Audition", "archivo": "au.png"},
    {"nombre": "Canva", "archivo": "canva.png"},
    {"nombre": "C++", "archivo": "cpp.png"},
    {"nombre": "Unity", "archivo": "unity.png"},
    {"nombre": "TouchDesigner", "archivo": "touchdesigner.png"},
    {"nombre": "Filmora", "archivo": "filmora.png"},
    {"nombre": "Figma", "archivo": "figma.png"},
    {"nombre": "MediaPipe", "archivo": "mediapipe.png"},
    {"nombre": "Maya", "archivo": "maya.png"},
]


# -----------------------------------------------------------------------
# PROYECTOS — cada uno se muestra como su propio bloque, con carrusel.
# Usa la función proyecto(...) para cada uno; solo llena estos 6 campos
# cortos. Dejar "" en enlace o herramientas está bien, simplemente no
# se muestra esa línea.
# -----------------------------------------------------------------------
def proyecto(
    titulo,
    resumen,
    archivo="",
    galeria=None,
    rol="",
    herramientas="",
    resultado="",
    enlace="",
):
    return {
        "titulo": titulo,              # nombre del proyecto
        "resumen": resumen,            # 1 frase corta
        "archivo": archivo,            # UNA imagen, video local o URL de Vimeo
        "galeria": galeria or [],      # o VARIAS imágenes/videos/URLs de Vimeo
        "rol": rol,                    # tu rol, ej: "Diseño UX + modelado 3D"
        "herramientas": herramientas,  # ej: "Unity, Blender, C++"
        "resultado": resultado,        # 1 frase: qué se logró / impacto
        "enlace": enlace,              # url a demo o repo (opcional)
    }


# Proyectos "inmersivos" — foto (.jpg/.png) o video local (.mp4)
# o video de Vimeo mediante:
# https://player.vimeo.com/video/ID
INMERSIVOS = [
    proyecto(
        titulo="Museo: el universo de Tim Burton",
        resumen="Experiencia inmersiva de tipo exploratoria para una exhibición temática sobre el universo de Tim Burton, recorriendo algunas de sus obras más emblemáticas.",
        archivo="https://player.vimeo.com/video/1223905053?badge=0&autopause=0&player_id=0&app_id=58479",
    ),
    proyecto(
        titulo="Videojuego en VR: Vayquin",
        resumen="Videojuego de realidad virtual tipo exploratorio, navegando por un planeta desconocido para reparar la nave y volver a casa.",

        # AQUÍ VA EL VIDEO DE VIMEO
        # Reemplaza 123456789 por el ID real de tu video.
        archivo="https://player.vimeo.com/video/1223905112?badge=0&autopause=0&player_id=0&app_id=58479",
        rol="Desarrollo y montaje.",
        herramientas="Unity.",
    ),
    proyecto(
        titulo="Videojuego: Bruna Lab (En proceso)",
        resumen="Videojuego 2D para niños que quieren aprender sobre química sin el riesgo de un laboratorio.",
        archivo="brunalab.png",
        rol="Project Manager.",
    ),
]

# Proyectos de "Interfaces"
INTERFACES = [
    proyecto(
        titulo="App: Mundo Ayuda Mayores",
        resumen="Aplicativo para mayores de edad con baja alfabetización digital para facilitar tareas diarias.",
        galeria=[
            "mundo1.png",
            "mundo2.png",
        ],
        rol="Diseño de experiencia y de interfaz (UX/UI).",
        herramientas="Figma y Canva.",
    ),
    proyecto(
        titulo="App: Parque Éxpora",
        resumen="Aplicativo para facilitar la experiencia de espera en la cafetería del parque.",
        galeria=[
            "1.jpg",
            "2.jpg",
            "3.jpg",
            "4.jpg",
            "5.jpg",
            "6.jpg",
            "7.jpg",
            "8.jpg",
            "9.jpg",
            "10.jpg",
        ],
        rol="Diseño de experiencia y de interfaz (UX/UI).",
        herramientas="Figma y Canva.",
    ),
    proyecto(
        titulo="App: Antioquia, territorio multicultural (En proceso)",
        resumen="Aplicativo para aprender sobre la diversidad cultural de Antioquia.",
        galeria=[
            "mundo1.jpg",
            "mundo2.jpg",
        ],
        rol="Diseño de experiencia y de interfaz (UX/UI).",
        herramientas="Figma y Canva.",
    ),
]

# Proyectos de "Visual"
VISUAL = [
    proyecto(
        titulo="Modelado 3D",
        resumen="Selección de piezas y ejercicios de modelado 3D.",
        galeria=[
            "3d1.jpg",
            "3d2.jpg",
            "3d3.jpg",
            "3d4.jpg",
        ],
        herramientas="Maya y Adobe Substance 3D Painter.",
    ),
    proyecto(
        titulo="Visuales",
        resumen="Visuales reactivas al movimiento y al sonido.",
        galeria=[
            "https://player.vimeo.com/video/1223905305?badge=0&autopause=0&player_id=0&app_id=58479",
            "https://player.vimeo.com/video/1223905258?badge=0&autopause=0&player_id=0&app_id=58479",
        ],
        herramientas="TouchDesigner.",
    ),
]

# Proyectos de "Investigación"
INVESTIGACION = [
    proyecto(
        titulo="Educación en niños con TEA",
        resumen="Investigación sobre estrategias usadas en la educación para niños con TEA y propuestas a través del diseño.",
        galeria=[
            "1.1.png",
            "2.1.png",
            "3.1.png",
        ],
    ),
    proyecto(
        titulo="Investigación de mercados: Postobón",
        resumen="Estudio de mercado sobre el comportamiento posconsumo del consumidor.",
        galeria=[
            "p1.jpg",
            "p2.jpg",
            "p3.jpg",
            "p4.jpg",
            "p5.jpg",
            "p6.jpg",
            "p7.jpg",
        ],
    ),
]

CONTACT = {
    "titulo_1": "TRABAJEMOS",
    "titulo_2": "JUNTOS",
    "texto": "¿Tienes un proyecto en mente? Escríbeme y hablemos.",
    "email": "lngarciac@eafit.edu.co",
    "telefono": "+57 3103777407",
    "links": [
        {"nombre": "LinkedIn", "url": "https://linkedin.com/in/tu-usuario"},
    ],
}

# =============================================================================
# DISEÑO — dirección de arte "revista editorial años 70". No necesitas tocar esto.
# =============================================================================

PALETTE = {
    "void": "#20150e",      # marrón tinta, casi negro (fondos profundos)
    "plum": "#4a4a2a",      # verde oliva oscuro
    "crimson": "#9c3b28",   # rojo terracota
    "ember": "#cf6a2c",     # naranja quemado
    "amber": "#e0a83c",     # mostaza
    "cream": "#f3e7cf",     # papel crema de imprenta
    "ink": "#2b1c10",       # tinta marrón para texto y filetes
}

FONT_DISPLAY = "Bodoni Moda"
FONT_KICKER = "Bebas Neue"
FONT_BODY = "EB Garamond"


def echo_style(colors) -> str:
    """Sombra de texto por capas, tipo mala alineación de tinta en impresión
    offset de los 70 — es el efecto de firma del título principal."""
    steps = [(3 + i * 3, 3 + i * 3, c) for i, c in enumerate(colors)]
    return "text-shadow:" + ",".join(f"{x}px {y}px 0 {c}" for x, y, c in steps) + ";"


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Bebas+Neue&family=EB+Garamond:ital,wght@0,400..700;1,400..700&display=swap');

        :root {{
            --void: {PALETTE['void']};
            --plum: {PALETTE['plum']};
            --crimson: {PALETTE['crimson']};
            --ember: {PALETTE['ember']};
            --amber: {PALETTE['amber']};
            --cream: {PALETTE['cream']};
            --ink: {PALETTE['ink']};
        }}

        html, body, [class*="css"] {{
            font-family: '{FONT_BODY}', Georgia, serif;
        }}

        #MainMenu, footer, header {{visibility: hidden;}}
        .block-container {{
            padding: 0 !important;
            max-width: 100% !important;
        }}
        div[data-testid="stAppViewContainer"] {{
            background: var(--cream);
        }}

        /* textura de papel: fibra sutil + veladura cálida, sin tocar legibilidad */
        div[data-testid="stAppViewContainer"]::before {{
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 998;
            opacity: 0.35;
            mix-blend-mode: multiply;
            background-image:
                repeating-linear-gradient(0deg, rgba(43,28,16,0.035) 0 1px, transparent 1px 4px),
                repeating-linear-gradient(90deg, rgba(43,28,16,0.025) 0 1px, transparent 1px 6px);
        }}

        /* grano de impresión analógica sobre toda la página */
        div[data-testid="stAppViewContainer"]::after {{
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 999;
            opacity: 0.075;
            mix-blend-mode: multiply;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
        }}

        h1, h2, h3, .heat-display {{
            font-family: '{FONT_DISPLAY}', 'Times New Roman', serif;
            font-weight: 900;
            text-transform: uppercase;
            line-height: 1.02;
            letter-spacing: -1px;
            margin: 0;
            padding: 0.15em 0;
            overflow: visible;
        }}

        /* make sure no Streamlit wrapper ever clips our headline glyphs */
        div[data-testid="stVerticalBlock"],
        div[data-testid="element-container"],
        div[data-testid="stMarkdown"],
        div[data-testid="stMarkdownContainer"] {{
            overflow: visible !important;
        }}

        .kicker, .nav-bar a, .tool-chip, .card-badge, .cta-btn, .eyebrow-bar span {{
            font-family: '{FONT_KICKER}', 'Helvetica Neue', sans-serif;
        }}

        /* ---------- signature retro flourishes ------------------------------ */
        .sunburst {{
            position: absolute;
            top: 50%; left: 6%;
            width: 1000px; height: 1000px;
            transform: translate(-50%, -50%);
            background: repeating-conic-gradient(from 0deg, var(--ember) 0deg 9deg, transparent 9deg 20deg);
            opacity: 0.13;
            border-radius: 50%;
            animation: spin 90s linear infinite;
            pointer-events: none;
            z-index: 0;
        }}
        @keyframes spin {{ to {{ transform: translate(-50%, -50%) rotate(360deg); }} }}

        .halftone-block {{
            position: absolute;
            width: 240px; height: 240px;
            background-image: radial-gradient(currentColor 3px, transparent 3px);
            background-size: 17px 17px;
            opacity: 0.28;
            pointer-events: none;
            z-index: 0;
        }}
        .halftone-block.tr {{ top: 0; right: 0; clip-path: polygon(100% 0, 100% 100%, 0 0); }}
        .halftone-block.bl {{ bottom: 0; left: 0; clip-path: polygon(0 0, 100% 100%, 0 100%); }}

        /* fixed vertical "spine" label, readable through every color band */
        .spine {{
            position: fixed;
            left: 10px; top: 50%;
            writing-mode: vertical-rl;
            transform: rotate(180deg);
            font-family: '{FONT_KICKER}', sans-serif;
            font-size: 0.72rem;
            letter-spacing: 6px;
            text-transform: uppercase;
            color: #ffffff;
            mix-blend-mode: difference;
            z-index: 300;
            pointer-events: none;
        }}
        @media (max-width: 900px) {{ .spine {{ display: none; }} }}

        /* ---------- masthead / nav (misma mecánica, look de revista) -------- */
        .eyebrow-bar {{
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            padding: 12px 44px;
            font-size: 0.82rem;
            letter-spacing: 5px;
            text-transform: uppercase;
            color: var(--cream);
            border-bottom: 1px solid rgba(243,231,207,0.35);
        }}
        .eyebrow-bar span {{ opacity: 0.95; }}
        .eyebrow-bar span:nth-child(2) {{ color: var(--amber); }}
        .eyebrow-bar span:nth-child(3) {{ color: var(--ember); }}

        .nav-bar {{
            position: sticky;
            top: 0;
            z-index: 100;
            display: flex;
            flex-wrap: wrap;
            gap: 4px 8px;
            padding: 12px 44px;
            background: var(--cream);
            border-top: 3px double var(--ink);
            border-bottom: 3px double var(--ink);
        }}
        .nav-bar a {{
            color: var(--ink);
            text-decoration: none;
            font-size: 0.95rem;
            letter-spacing: 2.5px;
            text-transform: uppercase;
            padding: 5px 14px;
            border: 1px solid transparent;
            transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease;
            display: inline-block;
        }}
        .nav-bar a:hover {{
            background: var(--crimson);
            border-color: var(--ink);
            color: var(--cream);
        }}

        /* ---------- generic section shells, one per "temperature" step -----
           Streamlit gives every st.container(key="...") a class
           "st-key-<key>" on its own wrapper div, so we style sections by
           targeting that class directly (this is the only reliable way to
           put a full background behind real Streamlit widgets). */
        .st-key-hero, .st-key-about, .st-key-tools, .st-key-immersive,
        .st-key-interfaces, .st-key-visual, .st-key-research, .st-key-contact {{
            padding: 110px 72px !important;
            position: relative;
            overflow: visible;
            border-bottom: 4px double var(--ink);
        }}
        .st-key-divider {{ padding: 0 !important; position: relative; border-bottom: 4px double var(--ink); }}
        .st-key-hero {{ padding: 0 !important; position: relative; overflow: hidden; }}

        .st-key-about       {{ background: var(--crimson) !important; color: var(--cream); }}
        .st-key-tools       {{ background: var(--amber)   !important; color: var(--ink);   }}
        .st-key-immersive   {{ background: var(--void)    !important; color: var(--cream); }}
        .st-key-interfaces  {{ background: var(--plum)    !important; color: var(--cream); }}
        .st-key-visual      {{ background: var(--ember)   !important; color: var(--ink);   }}
        .st-key-research    {{ background: var(--cream)   !important; color: var(--ink);   }}
        .st-key-contact     {{ background: var(--void)    !important; color: var(--cream); padding: 0 !important; }}

        /* filete superior fino dentro de cada sección, como caja de artículo */
        .st-key-about::before, .st-key-tools::before, .st-key-immersive::before,
        .st-key-interfaces::before, .st-key-visual::before, .st-key-research::before {{
            content: "";
            position: absolute;
            top: 34px; left: 72px; right: 72px;
            height: 0;
            border-top: 1px solid currentColor;
            opacity: 0.4;
            pointer-events: none;
        }}

        .halftone {{
            background-image: radial-gradient(currentColor 1.4px, transparent 1.4px);
            background-size: 14px 14px;
            opacity: 0.12;
            position: absolute;
            inset: 0;
            pointer-events: none;
        }}

        .kicker {{
            font-size: 0.95rem;
            letter-spacing: 5px;
            text-transform: uppercase;
            display: inline-block;
            background: transparent;
            color: var(--amber);
            padding: 4px 0 8px 0;
            border-bottom: 1px solid currentColor;
            transform: none;
            margin-bottom: 22px;
            box-shadow: none;
        }}

        .display-xl {{ font-size: clamp(3.2rem, 10.5vw, 9rem); }}
        .display-lg {{ font-size: clamp(2.4rem, 6.6vw, 5.2rem); }}
        .display-md {{ font-size: clamp(1.5rem, 3vw, 2.3rem); }}

        .body-lg {{ font-size: 1.32rem; line-height: 1.62; max-width: 34em; }}
        .body-md {{ font-size: 1.12rem; line-height: 1.66; max-width: 34em; }}

        /* capitular editorial en el texto "Sobre mí" (puro CSS) */
        .st-key-about .body-lg > p:first-of-type::first-letter,
        .st-key-about p.body-lg::first-letter {{
            font-family: '{FONT_DISPLAY}', serif;
            font-weight: 900;
            font-size: 3.4em;
            line-height: 0.78;
            float: left;
            margin: 0.06em 0.09em 0 0;
            color: var(--amber);
        }}

        .rule {{
            height: 0;
            background: transparent;
            border-top: 3px double currentColor;
            opacity: 0.5;
            margin: 30px 0;
        }}

        .hero-wrap {{ position: relative; overflow: hidden; }}
        .hero-inner {{ position: relative; z-index: 2; }}

        /* ---------- herramientas: fichas de catálogo impreso --------------- */
        .tool-chip {{
            border: 1px solid currentColor;
            border-bottom-width: 3px;
            padding: 9px 16px;
            font-weight: 400;
            font-size: 1rem;
            letter-spacing: 2.5px;
            text-transform: uppercase;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            margin: 7px 10px 7px 0;
            background: rgba(243,231,207,0.35);
            box-shadow: none;
            transition: background 0.15s ease, color 0.15s ease, transform 0.15s ease;
        }}
        .tool-chip:nth-child(odd) {{ transform: rotate(-1deg); }}
        .tool-chip:nth-child(even) {{ transform: rotate(1deg); }}
        .tool-chip:hover {{ transform: rotate(0deg) translateY(-2px); background: var(--ink); color: var(--cream); }}

        /* ---------- botones de contacto: cintillo tipográfico -------------- */
        .cta-btn {{
            display: inline-block;
            border: 1px solid var(--cream);
            border-bottom-width: 3px;
            color: var(--cream) !important;
            padding: 12px 26px;
            font-size: 1rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            text-decoration: none;
            margin: 10px 14px 10px 0;
            box-shadow: none;
            transition: background 0.15s ease, color 0.15s ease, transform 0.15s ease;
        }}
        .cta-btn:hover {{
            background: var(--amber);
            border-color: var(--amber);
            color: var(--void) !important;
            transform: translateY(-2px);
        }}

        [data-testid="stImage"] img {{
            border: 1px solid var(--ink);
            outline: 6px solid var(--cream);
            outline-offset: -12px;
            filter: saturate(0.92) sepia(0.08) contrast(1.02);
        }}

        video {{
            border: 1px solid var(--ink);
        }}

        /* Vimeo dentro del carrusel */
        .hm-slide iframe {{
            width: 100%;
            height: 100%;
            border: none;
            display: block;
        }}

        /* ---------- project sections (no accordion, always visible) -------- */
        [class*="st-key-proj-"] {{
            border: 1px solid currentColor !important;
            border-top: 5px double currentColor !important;
            box-shadow: none !important;
            background: rgba(243,231,207,0.06) !important;
            padding: 30px 30px 34px 30px !important;
            margin: 0 !important;
            position: relative !important;
            overflow: visible !important;
        }}
        [class*="st-key-proj-"]::before {{
            content: "";
            position: absolute;
            top: 0; right: 0;
            width: 86px; height: 86px;
            background-image: radial-gradient(currentColor 1.6px, transparent 1.6px);
            background-size: 12px 12px;
            opacity: 0.14;
            clip-path: polygon(100% 0, 100% 100%, 0 0);
            pointer-events: none;
        }}
        .proj-badge {{
            position: absolute;
            top: -18px; left: 24px;
            width: auto; height: auto;
            border-radius: 0;
            background: var(--ink);
            color: var(--amber);
            border: 1px solid currentColor;
            display: inline-flex; align-items: center; justify-content: center;
            font-family: '{FONT_KICKER}', sans-serif;
            font-size: 0.9rem;
            letter-spacing: 3px;
            padding: 4px 12px;
            transform: none;
            box-shadow: none;
            z-index: 5;
        }}
        .proj-title {{
            font-family: '{FONT_DISPLAY}', serif;
            font-weight: 900;
            text-transform: uppercase;
            font-size: 1.62rem;
            letter-spacing: -0.4px;
            line-height: 1.06;
            margin: 18px 0 12px 0;
            padding-bottom: 12px;
            border-bottom: 3px double currentColor;
        }}
        .proj-resumen {{
            font-size: 1.08rem;
            line-height: 1.6;
            opacity: 0.94;
            margin: 14px 0 16px 0;
        }}
        .proj-meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin: 0 0 16px 0;
        }}
        .proj-chip {{
            border: none;
            border-left: 1px solid currentColor;
            padding: 4px 0 4px 12px;
            font-size: 0.98rem;
            line-height: 1.35;
        }}
        .proj-chip-label {{
            display: block;
            font-family: '{FONT_KICKER}', sans-serif;
            font-size: 0.72rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            opacity: 0.7;
            margin-bottom: 3px;
        }}
        .proj-resultado {{
            font-style: italic;
            font-size: 1.05rem;
            border-left: none;
            border-top: 1px solid currentColor;
            padding: 12px 0 2px 0;
            margin: 0 0 18px 0;
            opacity: 0.92;
        }}
        .proj-link-btn {{
            display: inline-block;
            border: 1px solid currentColor;
            border-bottom-width: 3px;
            color: currentColor !important;
            padding: 9px 20px;
            font-family: '{FONT_KICKER}', sans-serif;
            font-size: 0.95rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            text-decoration: none;
            box-shadow: none;
            transition: transform 0.15s ease, opacity 0.15s ease;
        }}
        .proj-link-btn:hover {{ transform: translateY(-2px); opacity: 0.75; }}

        /* the carousel itself is the only piece that still lives in an
           iframe (needed for the prev/next JS) — but its height is FIXED,
           so it never has the resize problems an accordion would have. */
        iframe {{ border: none !important; display: block; }}

        @media (max-width: 640px) {{
            .st-key-hero, .st-key-about, .st-key-tools, .st-key-immersive,
            .st-key-interfaces, .st-key-visual, .st-key-research, .st-key-contact {{
                padding: 64px 24px !important;
            }}
            .st-key-about::before, .st-key-tools::before, .st-key-immersive::before,
            .st-key-interfaces::before, .st-key-visual::before, .st-key-research::before {{
                left: 24px; right: 24px; top: 22px;
            }}
            .eyebrow-bar, .nav-bar {{ padding: 12px 18px; letter-spacing: 3px; }}
            .sunburst {{ width: 600px; height: 600px; }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def eyebrow_and_nav():
    words = SITE["eyebrow"]
    st.markdown(
        f'<div class="spine">{SITE["nombre"]} — {words[0]} · {words[1]} · {words[2]}</div>',
        unsafe_allow_html=True,
    )
    nav_links = "".join(f'<a href="#{a}">{label}</a>' for label, a in NAV)
    st.markdown(
        f"""
        <div class="eyebrow-bar" style="background:var(--ink);">
            <span>{words[0]}</span><span>{words[1]}</span><span>{words[2]}</span>
        </div>
        <div class="nav-bar">
            {nav_links}
        </div>
        """,
        unsafe_allow_html=True,
    )


def anchor(name: str):
    st.markdown(f'<div id="{name}"></div>', unsafe_allow_html=True)


def slugify(text: str) -> str:
    return "".join(c if c.isalnum() else "-" for c in text.lower()).strip("-")


# =============================================================================
# Utilidades de medios: si el archivo no existe, se genera un reemplazo
# con la estética editorial 70s en vez de romper la página.
# =============================================================================
@st.cache_data(show_spinner=False)
def placeholder_image(label: str, w: int = 900, h: int = 600) -> bytes:
    colors = [
        (32, 21, 14),
        (74, 74, 42),
        (156, 59, 40),
        (207, 106, 44),
        (224, 168, 60),
    ]

    img = Image.new("RGB", (w, h))
    px = img.load()
    n = len(colors) - 1

    for x in range(w):
        t = x / max(w - 1, 1) * n
        i = min(int(t), n - 1)
        frac = t - i
        c0, c1 = colors[i], colors[i + 1]

        r = int(c0[0] + (c1[0] - c0[0]) * frac)
        g = int(c0[1] + (c1[1] - c0[1]) * frac)
        b = int(c0[2] + (c1[2] - c0[2]) * frac)

        for y in range(h):
            px[x, y] = (r, g, b)

    draw = ImageDraw.Draw(img, "RGBA")

    for i in range(0, w, 14):
        draw.ellipse(
            [i - 1, 0, i + 1, h],
            fill=(0, 0, 0, 18)
        )

    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
            26,
        )
    except Exception:
        try:
            font = ImageFont.truetype(
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                26,
            )
        except Exception:
            font = ImageFont.load_default()

    text = f"❧  {label}"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]

    draw.rectangle(
        [
            w / 2 - tw / 2 - 20,
            h / 2 - th / 2 - 14,
            w / 2 + tw / 2 + 20,
            h / 2 + th / 2 + 14,
        ],
        fill=(32, 21, 14, 215),
    )

    draw.text(
        (w / 2 - tw / 2, h / 2 - th / 2 - 4),
        text,
        font=font,
        fill=(243, 231, 207, 255),
    )

    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=88)

    return buf.getvalue()


def show_media(rel_path: str, label: str, height: int = None):
    """Muestra <rel_path> (buscado en la raíz del repo). Si no existe,
    muestra un placeholder editorial."""

    path = ASSETS / rel_path

    if path.exists() and path.suffix.lower() in (".mp4", ".mov", ".webm"):
        st.video(
            str(path),
            loop=True,
            autoplay=True,
            muted=True,
        )

    elif path.exists():
        st.image(
            str(path),
            use_container_width=True,
        )

    else:
        st.image(
            placeholder_image(f"Añade: {rel_path}"),
            use_container_width=True,
        )


def _media_data_uri(rel_path: str, label: str):
    """Convierte medios locales en data-uri y detecta enlaces de Vimeo
    para reproducirlos directamente dentro del carrusel."""

    # ================================================================
    # 🎬 VIMEO
    # ================================================================
    # Si recibimos una URL del reproductor de Vimeo, NO intentamos
    # convertirla a base64. La devolvemos como iframe embebido.
    if isinstance(rel_path, str) and "player.vimeo.com/video/" in rel_path:
        return "vimeo", rel_path

    # ================================================================
    # 🎥 VIDEO LOCAL
    # ================================================================
    path = ASSETS / rel_path

    if path.exists() and path.suffix.lower() in (
        ".mp4",
        ".mov",
        ".webm",
    ):
        ext = path.suffix.lstrip(".").lower()
        data = base64.b64encode(path.read_bytes()).decode()

        return (
            "video",
            f"data:video/{ext};base64,{data}",
        )

    # ================================================================
    # 🖼️ IMAGEN LOCAL
    # ================================================================
    if path.exists():
        ext = path.suffix.lstrip(".").lower()
        mime = "jpeg" if ext in ("jpg", "jpeg") else ext
        data = base64.b64encode(path.read_bytes()).decode()

        return (
            "image",
            f"data:image/{mime};base64,{data}",
        )

    # ================================================================
    # ❌ ARCHIVO NO ENCONTRADO
    # ================================================================
    data = base64.b64encode(
        placeholder_image(f"Añade: {rel_path}")
    ).decode()

    return (
        "image",
        f"data:image/jpeg;base64,{data}",
    )


def carousel_widget(media_list, label, height=280):
    """Carrusel de fotos/video con altura FIJA.

    Soporta:
    - imágenes locales
    - videos locales
    - videos de Vimeo usando:
      https://player.vimeo.com/video/ID
    """

    if not media_list:
        st.image(
            placeholder_image(f"Añade fotos/video: {label}"),
            use_container_width=True,
        )
        return

    slides_html = []

    for i, rel in enumerate(media_list):
        kind, uri = _media_data_uri(
            rel,
            f"{label} {i + 1}",
        )

        # ============================================================
        # 🎥 VIDEO LOCAL
        # ============================================================
        if kind == "video":
            autoplay = "autoplay " if i == 0 else ""

            slides_html.append(
                f'''
                <div class="hm-slide">
                    <video
                        src="{uri}"
                        {autoplay}
                        muted
                        loop
                        playsinline>
                    </video>
                </div>
                '''
            )

        # ============================================================
        # 🎬 VIDEO VIMEO
        # ============================================================
        elif kind == "vimeo":
            slides_html.append(
                f'''
                <div class="hm-slide">
                    <iframe
                        src="{uri}"
                        width="100%"
                        height="100%"
                        frameborder="0"
                        allow="autoplay; fullscreen; picture-in-picture"
                        allowfullscreen>
                    </iframe>
                </div>
                '''
            )

        # ============================================================
        # 🖼️ IMAGEN
        # ============================================================
        else:
            slides_html.append(
                f'''
                <div class="hm-slide">
                    <img
                        src="{uri}"
                        alt="{label}">
                </div>
                '''
            )

    multi = len(slides_html) > 1

    dots_html = "".join(
        f'''
        <span
            class="hm-dot{" active" if i == 0 else ""}"
            onclick="hmGo(this,{i})">
        </span>
        '''
        for i in range(len(slides_html))
    )

    nav_html = (
        '<div class="hm-arrow hm-prev" onclick="hmPrev(this)">‹</div>'
        '<div class="hm-arrow hm-next" onclick="hmNext(this)">›</div>'
        if multi
        else ""
    )

    dots_wrap = (
        f'<div class="hm-dots">{dots_html}</div>'
        if multi
        else ""
    )

    html = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');

        * {{
            box-sizing: border-box;
        }}

        html, body {{
            margin: 0;
            padding: 0;
            background: transparent;
        }}

        .hm-carousel {{
            position: relative;
            width: 100%;
            height: {height}px;
            overflow: hidden;
            border: 1px solid {PALETTE['ink']};
            background: {PALETTE['void']};
        }}

        .hm-track {{
            display: flex;
            height: 100%;
            transition: transform 0.45s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .hm-slide {{
            flex: 0 0 100%;
            height: 100%;
        }}

        .hm-slide img,
        .hm-slide video,
        .hm-slide iframe {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }}

        .hm-slide img,
        .hm-slide video {{
            filter: saturate(0.92) sepia(0.08) contrast(1.02);
        }}

        .hm-arrow {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 30px;
            height: 38px;
            border-radius: 0;
            background: {PALETTE['cream']};
            color: {PALETTE['ink']};
            border: 1px solid {PALETTE['ink']};
            font-size: 1.15rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0.92;
            z-index: 5;
            user-select: none;
            transition: background 0.15s ease, color 0.15s ease;
            font-family: 'Bebas Neue', sans-serif;
        }}

        .hm-arrow:hover {{
            background: {PALETTE['crimson']};
            color: {PALETTE['cream']};
        }}

        .hm-prev {{
            left: 12px;
        }}

        .hm-next {{
            right: 12px;
        }}

        .hm-counter {{
            position: absolute;
            bottom: 12px;
            right: 12px;
            background: {PALETTE['cream']};
            color: {PALETTE['ink']};
            font-family: 'Bebas Neue', sans-serif;
            font-size: 0.78rem;
            letter-spacing: 3px;
            padding: 2px 10px;
            border: 1px solid {PALETTE['ink']};
            z-index: 5;
        }}

        .hm-dots {{
            position: absolute;
            bottom: 14px;
            left: 12px;
            display: flex;
            gap: 7px;
            z-index: 5;
        }}

        .hm-dot {{
            width: 8px;
            height: 8px;
            border-radius: 0;
            background: transparent;
            border: 1px solid {PALETTE['cream']};
            cursor: pointer;
            opacity: 0.7;
        }}

        .hm-dot.active {{
            background: {PALETTE['amber']};
            border-color: {PALETTE['amber']};
            opacity: 1;
        }}
    </style>

    <div class="hm-carousel" data-index="0">
        <div class="hm-track">
            {''.join(slides_html)}
        </div>

        {nav_html}

        <div class="hm-counter">
            01 / {len(slides_html):02d}
        </div>

        {dots_wrap}
    </div>

    <script>
        function hmSetIndex(root, idx) {{
            const track = root.querySelector('.hm-track');
            const slides = root.querySelectorAll('.hm-slide');
            const n = slides.length;

            idx = ((idx % n) + n) % n;

            track.style.transform =
                'translateX(' + (-idx * 100) + '%)';

            root.querySelectorAll('.hm-dot').forEach(
                (d, i) => d.classList.toggle(
                    'active',
                    i === idx
                )
            );

            const counter = root.querySelector('.hm-counter');

            if (counter) {{
                counter.textContent =
                    String(idx + 1).padStart(2, '0') +
                    ' / ' +
                    String(n).padStart(2, '0');
            }}

            // Pausar/reproducir videos locales.
            slides.forEach((s, i) => {{
                const v = s.querySelector('video');

                if (v) {{
                    if (i === idx) {{
                        v.currentTime = 0;
                        v.play().catch(() => {{}});
                    }} else {{
                        v.pause();
                    }}
                }}
            }});

            root.dataset.index = idx;
        }}

        function hmPrev(el) {{
            const r = el.closest('.hm-carousel');

            hmSetIndex(
                r,
                parseInt(r.dataset.index || '0') - 1
            );
        }}

        function hmNext(el) {{
            const r = el.closest('.hm-carousel');

            hmSetIndex(
                r,
                parseInt(r.dataset.index || '0') + 1
            );
        }}

        function hmGo(el, idx) {{
            const r = el.closest('.hm-carousel');

            hmSetIndex(r, idx);
        }}
    </script>
    """

    st.components.v1.html(
        html,
        height=height + 4,
    )


def project_section(item, idx, fg_hex):
    """Cada proyecto es su propio bloque, siempre visible (nada de
    desplegable): número de catálogo, carrusel, título, resumen, ficha
    corta (rol / herramientas), resultado y enlace opcional."""
    with st.container(key=f"proj-{slugify(item['titulo'])}-{idx}"):
        st.markdown(
            f'<div class="proj-badge">N°{idx + 1:02d}</div>',
            unsafe_allow_html=True,
        )

        carousel_widget(
            _project_media_list(item),
            item["titulo"],
        )

        st.markdown(
            f'<div class="proj-title">{item["titulo"]}</div>',
            unsafe_allow_html=True,
        )

        if item.get("resumen"):
            st.markdown(
                f'<p class="proj-resumen">{item["resumen"]}</p>',
                unsafe_allow_html=True,
            )

        chips = ""

        if item.get("rol"):
            chips += (
                '<div class="proj-chip">'
                '<span class="proj-chip-label">Rol</span>'
                f'{item["rol"]}'
                '</div>'
            )

        if item.get("herramientas"):
            chips += (
                '<div class="proj-chip">'
                '<span class="proj-chip-label">Herramientas</span>'
                f'{item["herramientas"]}'
                '</div>'
            )

        if chips:
            st.markdown(
                f'<div class="proj-meta">{chips}</div>',
                unsafe_allow_html=True,
            )

        if item.get("resultado"):
            st.markdown(
                f'<p class="proj-resultado">❧ {item["resultado"]}</p>',
                unsafe_allow_html=True,
            )

        if item.get("enlace"):
            st.markdown(
                f'<a class="proj-link-btn" '
                f'href="{item["enlace"]}" '
                f'target="_blank">Ver proyecto ↗</a>',
                unsafe_allow_html=True,
            )


def render_flow_field_bg(
    height_px: int,
    density: float = 1.0,
    seed: int = 0,
):
    """Fondo animado tipo 'loop de TouchDesigner' — partículas mostaza/naranja
    quemado fluyendo sobre tinta marrón como un campo de ruido (flow field) —
    generado 100% con canvas + JS. No carga ningún archivo, así que reemplaza
    los videos pesados (mp4 de varias decenas de MB) sin perder el look."""

    html = f"""
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            background: {PALETTE['void']};
            overflow: hidden;
        }}

        #hm-bg-wrap {{
            position: relative;
            width: 100%;
            height: {height_px}px;
            background: {PALETTE['void']};
        }}

        #hm-bg-canvas {{
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            display: block;
        }}
    </style>

    <div id="hm-bg-wrap">
        <canvas id="hm-bg-canvas"></canvas>
    </div>

    <script>
    (function() {{
        const canvas = document.getElementById('hm-bg-canvas');
        const ctx = canvas.getContext('2d');
        const wrap = document.getElementById('hm-bg-wrap');

        const DPR = Math.min(window.devicePixelRatio || 1, 2);

        const colors = [
            '{PALETTE['amber']}',
            '{PALETTE['ember']}',
            '{PALETTE['crimson']}'
        ];

        const voidColor = '{PALETTE['void']}';

        const seed = {seed};
        const density = {density};

        let W, H, particles = [];

        function hexToRgb(hex) {{
            hex = hex.replace('#', '');
            const n = parseInt(hex, 16);

            return [
                (n >> 16) & 255,
                (n >> 8) & 255,
                n & 255
            ];
        }}

        const rgbColors = colors.map(hexToRgb);
        const voidRgb = hexToRgb(voidColor);

        function fieldAngle(x, y, t) {{
            return (
                Math.sin(x * 0.006 + t * 0.35 + seed) +
                Math.cos(y * 0.008 - t * 0.28 + seed * 1.3) +
                Math.sin((x + y) * 0.004 + t * 0.18)
            ) * Math.PI * 0.6;
        }}

        function spawn() {{
            const c = rgbColors[
                Math.floor(Math.random() * rgbColors.length)
            ];

            return {{
                x: Math.random() * W,
                y: Math.random() * H,
                speed: 0.4 + Math.random() * 1.1,
                r: 0.6 + Math.random() * 1.5,
                life: 220 + Math.random() * 320,
                age: Math.random() * 300,
                color: c,
            }};
        }}

        function resize() {{
            W = wrap.clientWidth;
            H = wrap.clientHeight;

            canvas.width = W * DPR;
            canvas.height = H * DPR;

            canvas.style.width = W + 'px';
            canvas.style.height = H + 'px';

            ctx.setTransform(DPR, 0, 0, DPR, 0, 0);

            ctx.fillStyle = voidColor;
            ctx.fillRect(0, 0, W, H);

            const count = Math.max(
                80,
                Math.floor((W * H) / 9000 * density)
            );

            particles = [];

            for (let i = 0; i < count; i++) {{
                particles.push(spawn());
            }}
        }}

        let t = 0;

        function frame() {{
            t += 0.016;

            ctx.fillStyle =
                'rgba(' +
                voidRgb[0] + ',' +
                voidRgb[1] + ',' +
                voidRgb[2] + ',' +
                '0.07)';

            ctx.fillRect(0, 0, W, H);

            for (let p of particles) {{
                const angle = fieldAngle(p.x, p.y, t);

                p.x += Math.cos(angle) * p.speed;
                p.y += Math.sin(angle) * p.speed + 0.12;

                p.age += 1;

                if (
                    p.x < -10 ||
                    p.x > W + 10 ||
                    p.y < -10 ||
                    p.y > H + 10 ||
                    p.age > p.life
                ) {{
                    const fresh = spawn();
                    Object.assign(p, fresh);
                }}

                ctx.beginPath();

                ctx.fillStyle =
                    'rgba(' +
                    p.color[0] + ',' +
                    p.color[1] + ',' +
                    p.color[2] + ',' +
                    '0.55)';

                ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                ctx.fill();
            }}

            requestAnimationFrame(frame);
        }}

        resize();
        window.addEventListener('resize', resize);
        requestAnimationFrame(frame);
    }})();
    </script>
    """

    st.components.v1.html(
        html,
        height=height_px + 4,
    )


# =============================================================================
# SECCIONES
# =============================================================================

def section_hero():
    with st.container(key="hero"):
        anchor("inicio")

        render_flow_field_bg(
            height_px=460,
            density=1.3,
            seed=1,
        )

        st.markdown(
            f"""
            <div style="position:relative; padding:80px 72px 96px 72px; background:var(--void); color:var(--cream); overflow:hidden; border-top:1px solid rgba(243,231,207,0.25);">
                <div class="sunburst"></div>
                <div class="halftone-block tr" style="color:var(--amber);"></div>

                <div style="position:relative; z-index:2;">
                    <div class="kicker">{SITE['nombre']}</div>

                    <div
                        class="heat-display display-xl"
                        style="{echo_style(['var(--amber)', 'var(--ember)', 'var(--crimson)'])}">
                        {SITE['titulo_hero_1']}<br>
                        {SITE['titulo_hero_2']}
                    </div>

                    <div style="border-top:3px double rgba(243,231,207,0.5); max-width:38em; margin:34px 0 0 0;"></div>

                    <p
                        class="body-lg"
                        style="margin-top:22px; font-style:italic;">
                        {SITE['tagline']}
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def section_about():
    with st.container(key="about"):
        anchor("sobre-mi")

        col1, col2 = st.columns(
            [1.15, 1],
            gap="large",
        )

        with col1:
            st.markdown(
                f"""
                <div
                    class="heat-display display-lg"
                    style="{echo_style(['var(--void)', 'var(--amber)'])}">
                    {ABOUT['titulo']}
                </div>

                <div style="border-top:3px double rgba(243,231,207,0.55); max-width:34em; margin:26px 0 0 0;"></div>

                <p
                    class="body-lg"
                    style="margin-top:24px;">
                    {ABOUT['texto']}
                </p>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                "<div style='height:52px;'></div>",
                unsafe_allow_html=True,
            )
            show_media(
                ABOUT["imagen"],
                "tu foto de perfil",
            )


def section_tools():
    with st.container(key="tools"):
        anchor("herramientas")

        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--crimson)", "var(--plum)"])}">HERRAMIENTAS</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            "<div style='border-top:3px double rgba(43,28,16,0.55); margin:24px 0 0 0;'></div>",
            unsafe_allow_html=True,
        )

        chips = []

        for tool in TOOLS:
            logo_path = (
                ASSETS /
                "tools" /
                tool["archivo"]
            )

            if logo_path.exists():
                icon_html = (
                    '<img '
                    f'src="data:image/png;base64,'
                    f'{base64.b64encode(logo_path.read_bytes()).decode()}" '
                    'style="height:22px;">'
                )
            else:
                icon_html = "✦"

            chips.append(
                f'<span class="tool-chip">'
                f'{icon_html} '
                f'{tool["nombre"]}'
                f'</span>'
            )

        st.markdown(
            f'<div style="margin-top:32px;">'
            f'{"".join(chips)}'
            f'</div>',
            unsafe_allow_html=True,
        )


def _project_media_list(item):
    """Une 'archivo' (un solo medio) y 'galeria' (varios) en una sola lista
    para alimentar el carrusel, sin importar cómo esté definido el proyecto."""

    if item.get("galeria"):
        return list(item["galeria"])

    if item.get("archivo"):
        return [item["archivo"]]

    return []


def render_missing_assets_banner():
    """Aviso de desarrollo (solo para ti, no para reclutadores): revisa qué
    imágenes/videos referenciados en el código NO se encontraron en /assets
    y muestra la ruta EXACTA que se buscó, para detectar rápido errores de
    mayúsculas, extensión o carpeta. Bórralo cuando ya no lo necesites."""

    expected = [
        ABOUT["imagen"]
    ]

    for lst in (
        INMERSIVOS,
        INTERFACES,
        VISUAL,
        INVESTIGACION,
    ):
        for item in lst:
            expected.extend(
                _project_media_list(item)
            )

    # Los enlaces de Vimeo no son archivos locales,
    # así que NO deben aparecer como archivos faltantes.
    missing = [
        p
        for p in expected
        if p
        and "player.vimeo.com/video/" not in str(p)
        and not (ASSETS / p).exists()
    ]

    if missing:
        with st.expander(
            f"⚠️ DEV: faltan {len(missing)} archivo(s) "
            "en la raíz del repo "
            "(clic para ver rutas exactas)"
        ):
            st.write(
                "Streamlit no encontró estos archivos con ese nombre exacto "
                "(revisa mayúsculas/minúsculas, extensión y carpeta):"
            )

            for p in missing:
                st.code(
                    str(ASSETS / p)
                )


def project_grid(items, section_key, columns=2, fg_hex=None):
    """Distribuye proyectos usando columnas reales de Streamlit.

    - 2 columnas: dos tarjetas del mismo ancho.
    - Si queda un proyecto impar al final, se centra con el mismo ancho
      que una tarjeta normal.
    """
    fg_hex = fg_hex or PALETTE["cream"]

    if not items:
        return

    # En este portafolio trabajamos con 2 columnas en escritorio.
    # El tercer/último proyecto ocupa una columna centrada, no todo el ancho.
    cols_count = 2 if columns <= 2 else columns

    for start_idx in range(0, len(items), cols_count):
        row_items = items[start_idx:start_idx + cols_count]

        if len(row_items) == cols_count:
            cols = st.columns(cols_count, gap="large")
            for local_idx, item in enumerate(row_items):
                with cols[local_idx]:
                    project_section(item, start_idx + local_idx, fg_hex)

        else:
            # Última fila incompleta: dejamos espacios laterales iguales.
            if cols_count == 2 and len(row_items) == 1:
                empty_left, center, empty_right = st.columns([1, 1, 1], gap="large")
                with center:
                    project_section(row_items[0], start_idx, fg_hex)
            else:
                cols = st.columns(cols_count, gap="large")
                for local_idx, item in enumerate(row_items):
                    with cols[local_idx]:
                        project_section(item, start_idx + local_idx, fg_hex)

def section_immersive():
    with st.container(key="immersive"):
        anchor("inmersivos")

        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--ember)", "var(--amber)"])}">INMERSIVOS</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<p class="body-md" style="margin:22px 0 50px 0; border-top:3px double rgba(243,231,207,0.5); padding-top:22px; font-style:italic;">Proyectos que combinan diseño, tecnología y narrativa para crear experiencias que se recorren, no solo se miran.</p>',
            unsafe_allow_html=True,
        )

        project_grid(
            INMERSIVOS,
            "immersivos",
            fg_hex=PALETTE["cream"],
        )


def section_divider():
    with st.container(key="divider"):
        render_flow_field_bg(
            height_px=200,
            density=0.8,
            seed=2,
        )


def section_interfaces():
    with st.container(key="interfaces"):
        anchor("interfaces")

        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--crimson)", "var(--amber)"])}">INTERFACES</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            "<div style='border-top:3px double rgba(243,231,207,0.5); margin:24px 0 0 0; height:40px;'></div>",
            unsafe_allow_html=True,
        )

        project_grid(
            INTERFACES,
            "interfaces",
            fg_hex=PALETTE["cream"],
        )


def section_visual():
    with st.container(key="visual"):
        anchor("visual")

        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--plum)", "var(--crimson)"])}">VISUAL</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            "<div style='border-top:3px double rgba(43,28,16,0.5); margin:24px 0 0 0; height:40px;'></div>",
            unsafe_allow_html=True,
        )

        project_grid(
            VISUAL,
            "visual",
            columns=2,
            fg_hex=PALETTE["void"],
        )


def section_research():
    with st.container(key="research"):
        anchor("investigacion")

        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--crimson)", "var(--plum)"])}">INVESTIGACIÓN</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            "<div style='border-top:3px double rgba(43,28,16,0.5); margin:24px 0 0 0; height:40px;'></div>",
            unsafe_allow_html=True,
        )

        project_grid(
            INVESTIGACION,
            "investigacion",
            fg_hex=PALETTE["ink"],
        )


def section_contact():
    with st.container(key="contact"):
        anchor("contacto")

        render_flow_field_bg(
            height_px=380,
            density=1.1,
            seed=3,
        )

        links_html = "".join(
            f'<a class="cta-btn" '
            f'href="{l["url"]}" '
            f'target="_blank">'
            f'{l["nombre"]}'
            f'</a>'
            for l in CONTACT["links"]
        )

        st.markdown(
            f"""
            <div style="position:relative; padding:70px 72px 96px 72px; background:var(--void); color:var(--cream); overflow:hidden; border-top:1px solid rgba(243,231,207,0.25);">
                <div class="halftone-block bl" style="color:var(--amber);"></div>

                <div style="position:relative; z-index:2;">
                    <div
                        class="heat-display display-xl"
                        style="{echo_style(['var(--amber)', 'var(--ember)', 'var(--crimson)'])}">
                        {CONTACT['titulo_1']}<br>
                        {CONTACT['titulo_2']}
                    </div>

                    <div style="border-top:3px double rgba(243,231,207,0.5); max-width:38em; margin:32px 0 0 0;"></div>

                    <p
                        class="body-lg"
                        style="margin:22px 0 30px 0; font-style:italic;">
                        {CONTACT['texto']}
                    </p>

                    <a
                        class="cta-btn"
                        href="mailto:{CONTACT['email']}">
                        ✉ {CONTACT['email']}
                    </a>

                    {links_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =============================================================================
# RENDER
# =============================================================================

inject_css()
render_missing_assets_banner()
eyebrow_and_nav()
section_hero()
section_about()
section_tools()
section_immersive()
section_divider()
section_interfaces()
section_visual()
section_research()
section_contact()
