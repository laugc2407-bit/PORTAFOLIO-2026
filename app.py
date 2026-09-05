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
    "imagen": "perfil.png",
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
# DIRECCIÓN DE ARTE — "revista de arte y moda, 1974"
# Paleta impresa en offset: papel crema, tinta cálida, terracota, mostaza,
# oliva y rojo óxido. Todo el sitio lee de aquí.
# =============================================================================

PALETTE = {
    "paper": "#f1e6cf",       # papel crema
    "paper2": "#e4d3b2",      # papel envejecido
    "ink": "#1d1611",         # tinta negra cálida
    "espresso": "#4a2c1a",    # marrón oscuro
    "terracotta": "#a84428",  # terracota
    "burnt": "#c9622a",       # naranja quemado
    "mustard": "#d9a02b",     # mostaza
    "olive": "#5a6238",       # verde oliva
    "oxblood": "#6d1f22",     # rojo óxido
}

FONT_DISPLAY = "Bodoni Moda"    # titulares didone, alto contraste
FONT_ACCENT = "Abril Fatface"   # acentos gordos de portada
FONT_COND = "Oswald"            # condensada para folios, rótulos y nav
FONT_BODY = "EB Garamond"       # cuerpo de texto editorial

# Temas por sección (fondo / tinta / acento) — cada bloque es una página
# distinta de la revista, impresa con otra tinta.
THEMES = {
    "inmersivos": {"bg": PALETTE["ink"], "fg": PALETTE["paper"], "ac": PALETTE["mustard"]},
    "interfaces": {"bg": PALETTE["olive"], "fg": PALETTE["paper"], "ac": PALETTE["mustard"]},
    "visual": {"bg": PALETTE["burnt"], "fg": PALETTE["ink"], "ac": PALETTE["paper"]},
    "investigacion": {"bg": PALETTE["paper2"], "fg": PALETTE["ink"], "ac": PALETTE["terracotta"]},
}


def offset_ink(colors, step: int = 4) -> str:
    """Registro de tinta desalineado (offset de los 70): capas de sombra
    dura desplazadas en diagonal."""
    return "text-shadow:" + ",".join(
        f"{step * (i + 1)}px {step * (i + 1)}px 0 {c}" for i, c in enumerate(colors)
    ) + ";"


def slugify(text: str) -> str:
    return "".join(c if c.isalnum() else "-" for c in text.lower()).strip("-")


def anchor(name: str):
    st.markdown(f'<div id="{name}"></div>', unsafe_allow_html=True)


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Abril+Fatface&family=Oswald:wght@300;400;500;600&family=EB+Garamond:ital,wght@0,400..700;1,400..700&display=swap');

        :root {{
            --paper: {PALETTE['paper']};
            --paper2: {PALETTE['paper2']};
            --ink: {PALETTE['ink']};
            --espresso: {PALETTE['espresso']};
            --terracotta: {PALETTE['terracotta']};
            --burnt: {PALETTE['burnt']};
            --mustard: {PALETTE['mustard']};
            --olive: {PALETTE['olive']};
            --oxblood: {PALETTE['oxblood']};
        }}

        html, body, [class*="css"] {{
            font-family: '{FONT_BODY}', Georgia, serif;
            color: var(--ink);
        }}

        #MainMenu, footer, header {{ visibility: hidden; }}
        .block-container {{ padding: 0 !important; max-width: 100% !important; }}
        div[data-testid="stAppViewContainer"] {{ background: var(--paper); }}

        /* nada debe recortar los titulares grandes */
        div[data-testid="stVerticalBlock"],
        div[data-testid="element-container"],
        div[data-testid="stMarkdown"],
        div[data-testid="stMarkdownContainer"],
        div[data-testid="column"] {{ overflow: visible !important; }}

        /* ---------- textura de imprenta: fibra de papel + grano ----------- */
        div[data-testid="stAppViewContainer"]::before {{
            content: "";
            position: fixed; inset: 0;
            pointer-events: none; z-index: 997;
            opacity: 0.4; mix-blend-mode: multiply;
            background-image:
                repeating-linear-gradient(0deg, rgba(29,22,17,0.030) 0 1px, transparent 1px 4px),
                repeating-linear-gradient(90deg, rgba(29,22,17,0.022) 0 1px, transparent 1px 7px);
        }}
        div[data-testid="stAppViewContainer"]::after {{
            content: "";
            position: fixed; inset: 0;
            pointer-events: none; z-index: 999;
            opacity: 0.085; mix-blend-mode: multiply;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
        }}

        /* ---------- sistema tipográfico ---------------------------------- */
        h1, h2, h3, .disp {{
            font-family: '{FONT_DISPLAY}', 'Times New Roman', serif;
            font-weight: 900;
            text-transform: uppercase;
            line-height: 0.92;
            letter-spacing: -0.02em;
            margin: 0; padding: 0;
        }}
        .disp-xxl {{ font-size: clamp(3.6rem, 15vw, 13rem); }}
        .disp-xl  {{ font-size: clamp(3rem, 9vw, 7.4rem); }}
        .disp-lg  {{ font-size: clamp(2.2rem, 5.6vw, 4.6rem); }}
        .disp-md  {{ font-size: clamp(1.5rem, 2.6vw, 2.3rem); line-height: 1.02; }}

        .accent {{
            font-family: '{FONT_ACCENT}', '{FONT_DISPLAY}', serif;
            font-weight: 400;
            text-transform: uppercase;
            letter-spacing: -0.01em;
        }}
        .ital {{ font-style: italic; text-transform: none; letter-spacing: 0; }}

        .label {{
            font-family: '{FONT_COND}', sans-serif;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.34em;
            font-size: 0.72rem;
        }}
        .folio {{
            font-family: '{FONT_COND}', sans-serif;
            font-weight: 400;
            letter-spacing: 0.22em;
            font-size: 0.7rem;
            text-transform: uppercase;
            opacity: 0.85;
        }}
        .num-big {{
            font-family: '{FONT_DISPLAY}', serif;
            font-weight: 900;
            font-size: clamp(2.6rem, 6vw, 5.4rem);
            line-height: 0.8;
        }}
        .lede {{
            font-size: clamp(1.15rem, 1.6vw, 1.5rem);
            line-height: 1.5;
            font-style: italic;
            max-width: 30em;
        }}
        .body {{ font-size: 1.14rem; line-height: 1.62; }}
        .body p {{ margin: 0 0 1em 0; }}
        .caption {{
            font-family: '{FONT_COND}', sans-serif;
            font-size: 0.68rem;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            opacity: 0.78;
            padding-top: 8px;
        }}

        .rule-d {{ border-top: 3px double currentColor; opacity: 0.55; margin: 0; }}
        .rule-t {{ border-top: 1px solid currentColor; opacity: 0.45; margin: 0; }}

        /* capitular de revista */
        .dropcap > p:first-of-type::first-letter {{
            font-family: '{FONT_ACCENT}', serif;
            font-size: 4.1em;
            line-height: 0.74;
            float: left;
            margin: 0.08em 0.1em 0 0;
            color: var(--mustard);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def inject_css_layout():
    st.markdown(
        f"""
        <style>
        /* =====================================================================
           MAQUETA — cada st.container(key="x") recibe la clase .st-key-x,
           así que cada bloque se comporta como una página de la revista.
           ===================================================================== */

        .st-key-cover, .st-key-about, .st-key-tools, .st-key-contact,
        .st-key-work-inmersivos, .st-key-work-interfaces,
        .st-key-work-visual, .st-key-work-investigacion {{
            position: relative;
            overflow: visible;
            padding: clamp(56px, 7vw, 118px) clamp(22px, 5vw, 84px) !important;
        }}
        .st-key-cover {{ padding-bottom: clamp(40px, 4vw, 60px) !important; }}

        .st-key-cover    {{ background: var(--ink) !important; color: var(--paper); }}
        .st-key-about    {{ background: var(--paper) !important; color: var(--ink); }}
        .st-key-tools    {{ background: var(--oxblood) !important; color: var(--paper); }}
        .st-key-contact  {{ background: var(--ink) !important; color: var(--paper); padding-top: 0 !important; }}

        .st-key-work-inmersivos    {{ background: {THEMES['inmersivos']['bg']} !important; color: {THEMES['inmersivos']['fg']}; }}
        .st-key-work-interfaces    {{ background: {THEMES['interfaces']['bg']} !important; color: {THEMES['interfaces']['fg']}; }}
        .st-key-work-visual        {{ background: {THEMES['visual']['bg']} !important; color: {THEMES['visual']['fg']}; }}
        .st-key-work-investigacion {{ background: {THEMES['investigacion']['bg']} !important; color: {THEMES['investigacion']['fg']}; }}

        .st-key-strip-1, .st-key-strip-2, .st-key-strip-3 {{
            padding: 0 !important; position: relative; background: var(--ink) !important;
        }}

        /* marco de página impresa: filete interior en cada sección */
        .st-key-about::after, .st-key-tools::after, .st-key-work-inmersivos::after,
        .st-key-work-interfaces::after, .st-key-work-visual::after,
        .st-key-work-investigacion::after {{
            content: "";
            position: absolute;
            inset: clamp(20px, 2.4vw, 40px);
            border: 1px solid currentColor;
            opacity: 0.22;
            pointer-events: none;
        }}

        /* ---------- cabecera / navegación como sumario ------------------- */
        .mast {{
            display: flex; justify-content: space-between; align-items: baseline;
            gap: 18px; flex-wrap: wrap;
            padding: 12px clamp(22px, 5vw, 84px);
            background: var(--ink); color: var(--paper);
        }}
        .mast .label {{ opacity: 0.9; }}
        .mast .label:nth-child(2) {{ color: var(--mustard); }}
        .mast .label:nth-child(3) {{ color: var(--burnt); }}

        .nav {{
            position: sticky; top: 0; z-index: 120;
            display: flex; flex-wrap: wrap; align-items: center;
            gap: 2px 4px;
            padding: 10px clamp(18px, 5vw, 84px);
            background: var(--paper);
            border-top: 3px double var(--ink);
            border-bottom: 3px double var(--ink);
        }}
        .nav .nav-name {{
            font-family: '{FONT_DISPLAY}', serif; font-weight: 900;
            text-transform: uppercase; letter-spacing: 0.02em;
            font-size: 0.98rem; margin-right: 22px; white-space: nowrap;
        }}
        .nav a {{
            font-family: '{FONT_COND}', sans-serif;
            font-weight: 400; font-size: 0.82rem;
            letter-spacing: 0.18em; text-transform: uppercase;
            color: var(--ink); text-decoration: none;
            padding: 5px 11px; border: 1px solid transparent;
            transition: background .18s ease, color .18s ease, border-color .18s ease;
        }}
        .nav a sup {{ font-size: 0.6em; opacity: 0.6; margin-right: 4px; }}
        .nav a:hover {{ background: var(--terracotta); color: var(--paper); border-color: var(--ink); }}

        /* lomo vertical fijo */
        .spine {{
            position: fixed; left: 9px; top: 50%;
            writing-mode: vertical-rl; transform: rotate(180deg);
            font-family: '{FONT_COND}', sans-serif;
            font-size: 0.66rem; letter-spacing: 0.42em; text-transform: uppercase;
            color: #ffffff; mix-blend-mode: difference;
            z-index: 300; pointer-events: none;
        }}
        @media (max-width: 1000px) {{ .spine {{ display: none; }} }}

        /* ---------- portada ---------------------------------------------- */
        .sunburst {{
            position: absolute; top: 42%; left: 62%;
            width: 1250px; height: 1250px; transform: translate(-50%, -50%);
            background: repeating-conic-gradient(from 0deg, var(--terracotta) 0deg 8deg, transparent 8deg 22deg);
            opacity: 0.16; border-radius: 50%;
            animation: spin 120s linear infinite;
            pointer-events: none; z-index: 0;
        }}
        @keyframes spin {{ to {{ transform: translate(-50%, -50%) rotate(360deg); }} }}

        .halftone {{
            position: absolute; pointer-events: none; z-index: 0;
            background-image: radial-gradient(currentColor 2.6px, transparent 2.6px);
            background-size: 15px 15px; opacity: 0.3;
        }}
        .halftone.tr {{ top: 0; right: 0; width: 300px; height: 300px; clip-path: polygon(100% 0, 100% 100%, 0 0); }}
        .halftone.bl {{ bottom: 0; left: 0; width: 300px; height: 300px; clip-path: polygon(0 0, 100% 100%, 0 100%); }}

        .cover-grid {{ position: relative; z-index: 2; }}
        .cover-title {{ margin: 6px 0 0 0; }}
        .cover-title .l2 {{ display: block; margin-left: clamp(0px, 6vw, 130px); color: var(--mustard); }}
        .rise {{ animation: rise .9s cubic-bezier(.2,.7,.2,1) both; }}
        .rise-2 {{ animation: rise 1.1s cubic-bezier(.2,.7,.2,1) both; }}
        @keyframes rise {{ from {{ opacity: 0; transform: translateY(26px); }} to {{ opacity: 1; transform: none; }} }}

        /* sumario de portada */
        .toc {{ display: grid; gap: 0; border-top: 1px solid currentColor; }}
        .toc a {{
            display: flex; align-items: baseline; gap: 14px;
            padding: 9px 2px; text-decoration: none; color: inherit;
            border-bottom: 1px solid rgba(241,230,207,0.28);
            transition: padding-left .2s ease, background .2s ease, color .2s ease;
        }}
        .toc a:hover {{ padding-left: 12px; background: rgba(217,160,43,0.14); color: var(--mustard); }}
        .toc .n {{ font-family: '{FONT_COND}', sans-serif; font-size: 0.7rem; letter-spacing: 0.2em; opacity: 0.65; }}
        .toc .t {{ font-family: '{FONT_DISPLAY}', serif; font-weight: 900; text-transform: uppercase; font-size: 1.02rem; }}
        .toc .d {{ flex: 1; border-bottom: 1px dotted currentColor; opacity: 0.35; transform: translateY(-4px); }}

        /* ---------- cinta tipográfica (ticker impreso) -------------------- */
        .ticker {{
            overflow: hidden; white-space: nowrap;
            background: var(--mustard); color: var(--ink);
            border-top: 1px solid var(--ink); border-bottom: 1px solid var(--ink);
            padding: 9px 0;
        }}
        .ticker-inner {{ display: inline-block; animation: slide 34s linear infinite; }}
        .ticker span {{
            font-family: '{FONT_COND}', sans-serif; font-weight: 500;
            text-transform: uppercase; letter-spacing: 0.36em; font-size: 0.76rem;
            padding: 0 22px;
        }}
        @keyframes slide {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-50%); }} }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def inject_css_pieces():
    st.markdown(
        f"""
        <style>
        /* ---------- fichas de proyecto = artículos de revista ------------- */
        [class*="st-key-art-"] {{
            position: relative !important;
            overflow: visible !important;
            padding: 0 !important;
        }}
        .art-num {{
            font-family: '{FONT_DISPLAY}', serif; font-weight: 900;
            font-size: clamp(3rem, 7vw, 6.2rem); line-height: 0.78;
            color: transparent;
            -webkit-text-stroke: 1.4px currentColor;
            opacity: 0.75;
            margin: 0 0 6px 0;
        }}
        .art-kicker {{
            font-family: '{FONT_COND}', sans-serif;
            text-transform: uppercase;
            letter-spacing: 0.28em; font-size: 0.68rem; opacity: 0.8;
            display: block; margin-bottom: 10px;
        }}
        .art-title {{
            font-family: '{FONT_DISPLAY}', serif; font-weight: 900;
            text-transform: uppercase; line-height: 0.98;
            font-size: clamp(1.55rem, 2.5vw, 2.5rem);
            letter-spacing: -0.015em;
            margin: 4px 0 14px 0;
        }}
        .art-lede {{
            font-size: 1.12rem; line-height: 1.58; font-style: italic;
            margin: 0 0 18px 0; max-width: 34em;
        }}
        .art-meta {{ margin: 0 0 18px 0; }}
        .art-row {{
            display: flex; gap: 16px; align-items: baseline;
            border-top: 1px solid currentColor; padding: 9px 0;
            opacity: 0.95;
        }}
        .art-row:last-child {{ border-bottom: 1px solid currentColor; }}
        .art-row .k {{
            font-family: '{FONT_COND}', sans-serif; font-size: 0.66rem;
            letter-spacing: 0.22em; text-transform: uppercase;
            min-width: 108px; opacity: 0.72;
        }}
        .art-row .v {{ font-size: 1.02rem; line-height: 1.4; }}
        .art-result {{
            font-style: italic; font-size: 1.05rem;
            padding: 12px 0 0 0; margin: 0 0 18px 0;
            border-top: 3px double currentColor;
        }}
        .art-link {{
            display: inline-block; text-decoration: none; color: inherit !important;
            font-family: '{FONT_COND}', sans-serif; font-size: 0.76rem;
            letter-spacing: 0.24em; text-transform: uppercase;
            padding: 11px 22px;
            border: 1px solid currentColor; border-bottom-width: 3px;
            transition: transform .18s ease, background .18s ease, color .18s ease;
        }}
        .art-link:hover {{ transform: translateY(-3px); }}

        /* registro de tinta desplazado detrás de cada medio */
        [class*="st-key-art-"] iframe {{ border: 1px solid currentColor !important; }}
        .st-key-work-inmersivos [class*="st-key-art-"] iframe {{ box-shadow: 13px 13px 0 {THEMES['inmersivos']['ac']}; }}
        .st-key-work-interfaces [class*="st-key-art-"] iframe {{ box-shadow: 13px 13px 0 {THEMES['interfaces']['ac']}; }}
        .st-key-work-visual [class*="st-key-art-"] iframe {{ box-shadow: 13px 13px 0 {THEMES['visual']['ac']}; }}
        .st-key-work-investigacion [class*="st-key-art-"] iframe {{ box-shadow: 13px 13px 0 {THEMES['investigacion']['ac']}; }}

        /* ---------- retrato / imágenes de Streamlit ---------------------- */
        [data-testid="stImage"] img {{
            border: 1px solid var(--ink);
            filter: saturate(0.86) sepia(0.14) contrast(1.05);
            box-shadow: 14px 14px 0 var(--terracotta);
        }}
        video {{ border: 1px solid var(--ink); }}

        /* ---------- colofón de herramientas ------------------------------ */
        .colophon {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(178px, 1fr));
            border-top: 1px solid currentColor;
            border-left: 1px solid currentColor;
        }}
        .col-item {{
            display: flex; align-items: center; gap: 12px;
            padding: 17px 16px;
            border-right: 1px solid currentColor;
            border-bottom: 1px solid currentColor;
            transition: background .2s ease, color .2s ease;
        }}
        .col-item:hover {{ background: var(--mustard); color: var(--ink); }}
        .col-item .n {{
            font-family: '{FONT_COND}', sans-serif; font-size: 0.62rem;
            letter-spacing: 0.16em; opacity: 0.6;
        }}
        .col-item .nm {{
            font-family: '{FONT_DISPLAY}', serif; font-weight: 900;
            text-transform: uppercase; font-size: 0.94rem; line-height: 1.05;
        }}
        .col-item img {{ height: 22px; width: auto; filter: saturate(0.9); }}

        /* ---------- contraportada / contacto ----------------------------- */
        .btn {{
            display: inline-block; text-decoration: none;
            color: var(--paper) !important;
            font-family: '{FONT_COND}', sans-serif; font-size: 0.8rem;
            letter-spacing: 0.24em; text-transform: uppercase;
            padding: 14px 26px; margin: 10px 14px 10px 0;
            border: 1px solid var(--paper); border-bottom-width: 3px;
            transition: background .18s ease, color .18s ease, transform .18s ease;
        }}
        .btn:hover {{
            background: var(--mustard); border-color: var(--mustard);
            color: var(--ink) !important; transform: translateY(-3px);
        }}
        .contact-line {{
            display: flex; gap: 16px; align-items: baseline;
            border-top: 1px solid rgba(241,230,207,0.4); padding: 10px 0;
            font-size: 1.05rem;
        }}
        .contact-line .k {{
            font-family: '{FONT_COND}', sans-serif; font-size: 0.66rem;
            letter-spacing: 0.22em; text-transform: uppercase;
            min-width: 104px; opacity: 0.7;
        }}
        .back-cover {{ position: relative; padding: 64px 0 8px 0; }}
        .back-inner {{ position: relative; z-index: 2; }}
        .back-inner .folio {{ display: block; margin-bottom: 12px; }}
        .back-inner .l2 {{
            display: block; color: var(--mustard);
            margin-left: clamp(0px, 5vw, 110px);
        }}
        .contact-block {{ max-width: 44em; margin-bottom: 26px; }}

        /* pie de imprenta */
        .colofon-final {{
            display: flex; justify-content: space-between; flex-wrap: wrap; gap: 12px;
            padding: 16px clamp(22px, 5vw, 84px);
            background: var(--ink); color: var(--paper);
            border-top: 1px solid rgba(241,230,207,0.3);
        }}

        /* ---------- aviso DEV, discreto ---------------------------------- */
        div[data-testid="stExpander"] details {{
            border: 1px solid rgba(29,22,17,0.35) !important;
            background: var(--paper2) !important;
            border-radius: 0 !important;
        }}
        div[data-testid="stExpander"] summary p, div[data-testid="stExpander"] summary {{
            font-family: '{FONT_COND}', sans-serif !important;
            text-transform: uppercase; letter-spacing: 0.14em; font-size: 0.72rem !important;
        }}

        @media (max-width: 900px) {{
            .art-num {{ font-size: 3rem; }}
            .cover-title .l2 {{ margin-left: 0; }}
            [data-testid="stImage"] img, [class*="st-key-art-"] iframe {{ box-shadow: 8px 8px 0 var(--terracotta); }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# =============================================================================
# MEDIOS — misma lógica de siempre: archivos locales, videos locales y
# enlaces de Vimeo. Si un archivo falta, se dibuja un sustituto impreso.
# =============================================================================

@st.cache_data(show_spinner=False)
def placeholder_image(label: str, w: int = 900, h: int = 600) -> bytes:
    colors = [
        (29, 22, 17),
        (109, 31, 34),
        (168, 68, 40),
        (201, 98, 42),
        (217, 160, 43),
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

    # trama de semitono, como una foto mal impresa
    for i in range(0, w, 15):
        draw.ellipse([i - 1, 0, i + 1, h], fill=(0, 0, 0, 20))

    draw.rectangle([16, 16, w - 16, h - 16], outline=(241, 230, 207, 170), width=2)

    font = None
    for candidate in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ):
        try:
            font = ImageFont.truetype(candidate, 26)
            break
        except Exception:
            continue
    if font is None:
        font = ImageFont.load_default()

    text = f"❧  {label}"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]

    draw.rectangle(
        [w / 2 - tw / 2 - 22, h / 2 - th / 2 - 16, w / 2 + tw / 2 + 22, h / 2 + th / 2 + 16],
        fill=(29, 22, 17, 220),
    )
    draw.text(
        (w / 2 - tw / 2, h / 2 - th / 2 - 4),
        text,
        font=font,
        fill=(241, 230, 207, 255),
    )

    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=88)

    return buf.getvalue()


def show_media(rel_path: str, label: str, height: int = None):
    """Muestra <rel_path> (buscado en la raíz del repo). Si no existe,
    muestra un sustituto con la misma estética."""

    path = ASSETS / rel_path

    if path.exists() and path.suffix.lower() in (".mp4", ".mov", ".webm"):
        st.video(str(path), loop=True, autoplay=True, muted=True)

    elif path.exists():
        st.image(str(path), use_container_width=True)

    else:
        st.image(placeholder_image(f"Añade: {rel_path}"), use_container_width=True)


def _media_data_uri(rel_path: str, label: str):
    """Convierte medios locales en data-uri y detecta enlaces de Vimeo
    para reproducirlos directamente dentro del carrusel."""

    # Vimeo: se devuelve tal cual para embeberlo como iframe.
    if isinstance(rel_path, str) and "player.vimeo.com/video/" in rel_path:
        return "vimeo", rel_path

    path = ASSETS / rel_path

    # Video local.
    if path.exists() and path.suffix.lower() in (".mp4", ".mov", ".webm"):
        ext = path.suffix.lstrip(".").lower()
        data = base64.b64encode(path.read_bytes()).decode()
        return "video", f"data:video/{ext};base64,{data}"

    # Imagen local.
    if path.exists():
        ext = path.suffix.lstrip(".").lower()
        mime = "jpeg" if ext in ("jpg", "jpeg") else ext
        data = base64.b64encode(path.read_bytes()).decode()
        return "image", f"data:image/{mime};base64,{data}"

    # No encontrado.
    data = base64.b64encode(placeholder_image(f"Añade: {rel_path}")).decode()
    return "image", f"data:image/jpeg;base64,{data}"


def _project_media_list(item):
    """Une 'archivo' (un solo medio) y 'galeria' (varios) en una sola lista
    para alimentar el carrusel."""

    if item.get("galeria"):
        return list(item["galeria"])

    if item.get("archivo"):
        return [item["archivo"]]

    return []


def carousel_widget(media_list, label, height=430, theme=None):
    """Carrusel de fotos/videos con altura FIJA, presentado como una plancha
    de contactos: filete fino, folio de lámina, flechas de imprenta y índice
    de láminas. Soporta imágenes locales, videos locales y Vimeo."""

    theme = theme or {"bg": PALETTE["ink"], "fg": PALETTE["paper"], "ac": PALETTE["mustard"]}

    if not media_list:
        st.image(placeholder_image(f"Añade fotos/video: {label}"), use_container_width=True)
        return

    slides_html = []

    for i, rel in enumerate(media_list):
        kind, uri = _media_data_uri(rel, f"{label} {i + 1}")

        if kind == "video":
            autoplay = "autoplay " if i == 0 else ""
            slides_html.append(
                f'<div class="hm-slide"><video src="{uri}" {autoplay}muted loop playsinline></video></div>'
            )

        elif kind == "vimeo":
            slides_html.append(
                f'<div class="hm-slide"><iframe src="{uri}" width="100%" height="100%" '
                f'frameborder="0" allow="autoplay; fullscreen; picture-in-picture" '
                f'allowfullscreen></iframe></div>'
            )

        else:
            slides_html.append(
                f'<div class="hm-slide"><img src="{uri}" alt="{label}"></div>'
            )

    multi = len(slides_html) > 1

    dots_html = "".join(
        f'<span class="hm-dot{" active" if i == 0 else ""}" onclick="hmGo(this,{i})"></span>'
        for i in range(len(slides_html))
    )

    nav_html = (
        '<div class="hm-nav">'
        '<div class="hm-arrow" onclick="hmPrev(this)">←</div>'
        '<div class="hm-arrow" onclick="hmNext(this)">→</div>'
        '</div>'
        if multi
        else ""
    )

    dots_wrap = f'<div class="hm-dots">{dots_html}</div>' if multi else ""

    html = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;500&display=swap');

        * {{ box-sizing: border-box; }}
        html, body {{ margin: 0; padding: 0; background: transparent; }}

        .hm-carousel {{
            position: relative; width: 100%; height: {height}px;
            overflow: hidden;
            background: {theme['bg']};
            border: 1px solid {theme['fg']};
        }}
        .hm-track {{ display: flex; height: 100%; transition: transform .55s cubic-bezier(.4,0,.2,1); }}
        .hm-slide {{ flex: 0 0 100%; height: 100%; overflow: hidden; }}
        .hm-slide img, .hm-slide video, .hm-slide iframe {{
            width: 100%; height: 100%; object-fit: cover; display: block; border: none;
        }}
        .hm-slide img, .hm-slide video {{
            filter: saturate(0.86) sepia(0.14) contrast(1.06);
            transition: transform 1.1s cubic-bezier(.2,.7,.2,1), filter .4s ease;
        }}
        .hm-carousel:hover .hm-slide img {{ transform: scale(1.035); filter: saturate(0.95) sepia(0.06) contrast(1.04); }}

        /* folio de lámina, arriba a la izquierda */
        .hm-counter {{
            position: absolute; top: 0; left: 0; z-index: 6;
            background: {theme['ac']}; color: {theme['bg']};
            font-family: 'Oswald', sans-serif; font-weight: 500;
            font-size: 0.66rem; letter-spacing: 0.22em;
            padding: 5px 12px;
        }}
        /* flechas de imprenta, abajo a la derecha */
        .hm-nav {{ position: absolute; bottom: 0; right: 0; display: flex; z-index: 6; }}
        .hm-arrow {{
            width: 40px; height: 34px;
            display: flex; align-items: center; justify-content: center;
            background: {theme['fg']}; color: {theme['bg']};
            border-left: 1px solid {theme['bg']};
            font-family: 'Oswald', sans-serif; font-size: 0.92rem;
            cursor: pointer; user-select: none;
            transition: background .18s ease, color .18s ease;
        }}
        .hm-arrow:hover {{ background: {theme['ac']}; color: {theme['bg']}; }}

        /* índice de láminas: marcas verticales */
        .hm-dots {{ position: absolute; bottom: 12px; left: 12px; display: flex; gap: 6px; z-index: 6; }}
        .hm-dot {{
            width: 12px; height: 3px; background: {theme['fg']};
            opacity: 0.45; cursor: pointer; transition: opacity .2s ease, background .2s ease, width .2s ease;
        }}
        .hm-dot.active {{ background: {theme['ac']}; opacity: 1; width: 26px; }}
    </style>

    <div class="hm-carousel" data-index="0">
        <div class="hm-track">{''.join(slides_html)}</div>
        <div class="hm-counter">LÁM. 01 / {len(slides_html):02d}</div>
        {nav_html}
        {dots_wrap}
    </div>

    <script>
        function hmSetIndex(root, idx) {{
            const track = root.querySelector('.hm-track');
            const slides = root.querySelectorAll('.hm-slide');
            const n = slides.length;

            idx = ((idx % n) + n) % n;
            track.style.transform = 'translateX(' + (-idx * 100) + '%)';

            root.querySelectorAll('.hm-dot').forEach(
                (d, i) => d.classList.toggle('active', i === idx)
            );

            const counter = root.querySelector('.hm-counter');
            if (counter) {{
                counter.textContent =
                    'L\\u00c1M. ' + String(idx + 1).padStart(2, '0') +
                    ' / ' + String(n).padStart(2, '0');
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
            hmSetIndex(r, parseInt(r.dataset.index || '0') - 1);
        }}

        function hmNext(el) {{
            const r = el.closest('.hm-carousel');
            hmSetIndex(r, parseInt(r.dataset.index || '0') + 1);
        }}

        function hmGo(el, idx) {{
            const r = el.closest('.hm-carousel');
            hmSetIndex(r, idx);
        }}
    </script>
    """

    st.components.v1.html(html, height=height + 4)


def render_flow_field_bg(height_px: int, density: float = 1.0, seed: int = 0):
    """Banda gráfica generativa — partículas mostaza / naranja quemado /
    terracota fluyendo sobre tinta, como una lámina experimental impresa.
    Se dibuja en canvas, no carga archivos."""

    html = f"""
    <style>
        html, body {{ margin: 0; padding: 0; background: {PALETTE['ink']}; overflow: hidden; }}
        #hm-bg-wrap {{ position: relative; width: 100%; height: {height_px}px; background: {PALETTE['ink']}; }}
        #hm-bg-canvas {{ position: absolute; inset: 0; width: 100%; height: 100%; display: block; }}
    </style>

    <div id="hm-bg-wrap"><canvas id="hm-bg-canvas"></canvas></div>

    <script>
    (function() {{
        const canvas = document.getElementById('hm-bg-canvas');
        const ctx = canvas.getContext('2d');
        const wrap = document.getElementById('hm-bg-wrap');
        const DPR = Math.min(window.devicePixelRatio || 1, 2);

        const colors = ['{PALETTE['mustard']}', '{PALETTE['burnt']}', '{PALETTE['terracotta']}'];
        const voidColor = '{PALETTE['ink']}';
        const seed = {seed};
        const density = {density};

        let W, H, particles = [];

        function hexToRgb(hex) {{
            hex = hex.replace('#', '');
            const n = parseInt(hex, 16);
            return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
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
            const c = rgbColors[Math.floor(Math.random() * rgbColors.length)];
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

            const count = Math.max(80, Math.floor((W * H) / 9000 * density));
            particles = [];
            for (let i = 0; i < count; i++) {{ particles.push(spawn()); }}
        }}

        let t = 0;

        function frame() {{
            t += 0.016;

            ctx.fillStyle = 'rgba(' + voidRgb[0] + ',' + voidRgb[1] + ',' + voidRgb[2] + ',0.07)';
            ctx.fillRect(0, 0, W, H);

            for (let p of particles) {{
                const angle = fieldAngle(p.x, p.y, t);
                p.x += Math.cos(angle) * p.speed;
                p.y += Math.sin(angle) * p.speed + 0.12;
                p.age += 1;

                if (p.x < -10 || p.x > W + 10 || p.y < -10 || p.y > H + 10 || p.age > p.life) {{
                    Object.assign(p, spawn());
                }}

                ctx.beginPath();
                ctx.fillStyle = 'rgba(' + p.color[0] + ',' + p.color[1] + ',' + p.color[2] + ',0.55)';
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

    st.components.v1.html(html, height=height_px + 4)


def ticker_band(words):
    """Cinta tipográfica horizontal, como el lomo repetido de una revista."""
    run = "".join(f"<span>{w}</span><span>✦</span>" for w in words)
    st.markdown(
        f'<div class="ticker"><div class="ticker-inner">{run}{run}</div></div>',
        unsafe_allow_html=True,
    )


def spacer(px: int):
    st.markdown(f"<div style='height:{px}px;'></div>", unsafe_allow_html=True)


def render_missing_assets_banner():
    """Aviso de desarrollo (solo para ti): revisa qué imágenes/videos
    referenciados en el código NO se encontraron, y muestra la ruta EXACTA
    que se buscó. Bórralo cuando ya no lo necesites."""

    expected = [ABOUT["imagen"]]

    for lst in (INMERSIVOS, INTERFACES, VISUAL, INVESTIGACION):
        for item in lst:
            expected.extend(_project_media_list(item))

    missing = [
        p
        for p in expected
        if p
        and "player.vimeo.com/video/" not in str(p)
        and not (ASSETS / p).exists()
    ]

    if missing:
        with st.expander(
            f"⚠️ DEV: faltan {len(missing)} archivo(s) en la raíz del repo "
            "(clic para ver rutas exactas)"
        ):
            st.write(
                "Streamlit no encontró estos archivos con ese nombre exacto "
                "(revisa mayúsculas/minúsculas, extensión y carpeta):"
            )
            for p in missing:
                st.code(str(ASSETS / p))


# =============================================================================
# PÁGINAS DE LA REVISTA
# =============================================================================

SECTION_NUM = {a: i + 1 for i, (_, a) in enumerate(NAV)}


def masthead_and_nav():
    words = SITE["eyebrow"]

    st.markdown(
        f'<div class="spine">{SITE["nombre"]} — {words[0]} · {words[1]} · {words[2]}</div>',
        unsafe_allow_html=True,
    )

    nav_links = "".join(
        f'<a href="#{a}"><sup>{SECTION_NUM[a]:02d}</sup>{label}</a>'
        for label, a in NAV
    )

    st.markdown(
        f"""
        <div class="mast">
            <span class="label">{words[0]}</span>
            <span class="label">{words[1]}</span>
            <span class="label">{words[2]}</span>
        </div>
        <div class="nav">
            <span class="nav-name">{SITE['nombre']}</span>
            {nav_links}
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_cover():
    """Portada: titular a sangre, sol naciente girando y sumario de la
    edición a la derecha."""
    with st.container(key="cover"):
        anchor("inicio")

        st.markdown(
            '<div class="sunburst"></div>'
            '<div class="halftone tr" style="color:var(--mustard);"></div>',
            unsafe_allow_html=True,
        )

        col_title, col_toc = st.columns([1.62, 1], gap="large")

        with col_title:
            toc_items = "".join(
                f'<a href="#{a}"><span class="n">{SECTION_NUM[a]:02d}</span>'
                f'<span class="t">{label}</span><span class="d"></span></a>'
                for label, a in NAV
            )

            st.markdown(
                f"""
                <div class="cover-grid rise">
                    <div class="label" style="color:var(--mustard);">{SITE['nombre']}</div>
                    <div class="disp disp-xxl cover-title"
                         style="{offset_ink(['var(--terracotta)', 'var(--espresso)'], 5)}">
                        {SITE['titulo_hero_1']}
                        <span class="l2 accent">{SITE['titulo_hero_2']}</span>
                    </div>
                    <div class="rule-d" style="margin:34px 0 20px 0; max-width:40em;"></div>
                    <p class="lede rise-2" style="margin:0;">{SITE['tagline']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col_toc:
            st.markdown(
                f"""
                <div class="cover-grid rise-2" style="padding-top:14px;">
                    <div class="folio" style="margin-bottom:12px;">
                        {SITE['eyebrow'][0]} · {SITE['eyebrow'][1]} · {SITE['eyebrow'][2]}
                    </div>
                    <div class="toc">{toc_items}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def section_about():
    """Doble página de apertura: retrato a la izquierda, texto a dos
    columnas con capitular a la derecha."""
    with st.container(key="about"):
        anchor("sobre-mi")

        st.markdown(
            f"""
            <div class="folio" style="margin-bottom:10px;">
                {SECTION_NUM['sobre-mi']:02d} — {SITE['eyebrow'][1]}
            </div>
            <div class="disp disp-xl" style="{offset_ink(['var(--burnt)'], 4)}">
                {ABOUT['titulo']}
            </div>
            <div class="rule-d" style="margin:30px 0 44px 0;"></div>
            """,
            unsafe_allow_html=True,
        )

        col_img, col_txt = st.columns([0.92, 1.28], gap="large")

        with col_img:
            show_media(ABOUT["imagen"], "tu foto de perfil")
            st.markdown(
                f'<div class="caption">{SITE["nombre"]} — {SITE["eyebrow"][0]}</div>',
                unsafe_allow_html=True,
            )

        with col_txt:
            st.markdown(
                f'<div class="body dropcap">\n\n{ABOUT["texto"]}\n\n</div>',
                unsafe_allow_html=True,
            )


def section_tools():
    """Colofón: las herramientas como índice técnico de la edición."""
    with st.container(key="tools"):
        anchor("herramientas")

        items = []

        for i, tool in enumerate(TOOLS):
            logo_path = ASSETS / "tools" / tool["archivo"]

            if logo_path.exists():
                icon_html = (
                    '<img src="data:image/png;base64,'
                    f'{base64.b64encode(logo_path.read_bytes()).decode()}">'
                )
            else:
                icon_html = '<span class="n">✦</span>'

            items.append(
                '<div class="col-item">'
                f'<span class="n">{i + 1:02d}</span>'
                f'{icon_html}'
                f'<span class="nm">{tool["nombre"]}</span>'
                '</div>'
            )

        st.markdown(
            f"""
            <div class="folio" style="margin-bottom:10px;">
                {SECTION_NUM['herramientas']:02d} — {SITE['eyebrow'][2]}
            </div>
            <div class="disp disp-lg" style="{offset_ink(['var(--mustard)'], 4)}">HERRAMIENTAS</div>
            <div class="rule-d" style="margin:28px 0 34px 0;"></div>
            <div class="colophon">{''.join(items)}</div>
            """,
            unsafe_allow_html=True,
        )


def article(item, idx, theme, kicker, flip=False):
    """Ficha de proyecto compuesta como artículo: láminas a un lado,
    titular + entradilla + créditos al otro. El orden se alterna para que
    la lectura avance en zigzag, como en una revista."""

    with st.container(key=f"art-{slugify(item['titulo'])}-{idx}"):
        ratio = [1, 1.42] if flip else [1.42, 1]
        cols = st.columns(ratio, gap="large")

        col_media = cols[1] if flip else cols[0]
        col_text = cols[0] if flip else cols[1]

        with col_media:
            carousel_widget(
                _project_media_list(item),
                item["titulo"],
                height=430,
                theme=theme,
            )

        with col_text:
            rows = ""

            if item.get("rol"):
                rows += (
                    '<div class="art-row"><span class="k">Rol</span>'
                    f'<span class="v">{item["rol"]}</span></div>'
                )

            if item.get("herramientas"):
                rows += (
                    '<div class="art-row"><span class="k">Herramientas</span>'
                    f'<span class="v">{item["herramientas"]}</span></div>'
                )

            meta = f'<div class="art-meta">{rows}</div>' if rows else ""

            resultado = (
                f'<p class="art-result">{item["resultado"]}</p>'
                if item.get("resultado")
                else ""
            )

            enlace = (
                f'<a class="art-link" href="{item["enlace"]}" target="_blank">Ver proyecto ↗</a>'
                if item.get("enlace")
                else ""
            )

            resumen = (
                f'<p class="art-lede">{item["resumen"]}</p>'
                if item.get("resumen")
                else ""
            )

            st.markdown(
                f"""
                <div style="padding-top:6px;">
                    <div class="art-num">{idx + 1:02d}</div>
                    <span class="art-kicker">{kicker}</span>
                    <div class="art-title">{item['titulo']}</div>
                    {resumen}
                    {meta}
                    {resultado}
                    {enlace}
                </div>
                """,
                unsafe_allow_html=True,
            )


def section_work(key, anchor_id, titulo, items, theme, standfirst=""):
    """Sección de trabajo: apertura tipográfica y después un artículo por
    proyecto, alternando la posición de las láminas."""

    with st.container(key=f"work-{key}"):
        anchor(anchor_id)

        lede = (
            f'<p class="lede" style="margin:26px 0 0 0; max-width:38em;">{standfirst}</p>'
            if standfirst
            else ""
        )

        st.markdown(
            f"""
            <div class="folio" style="margin-bottom:10px;">
                {SECTION_NUM.get(anchor_id, 0):02d} — {len(items):02d} {'proyectos' if len(items) != 1 else 'proyecto'}
            </div>
            <div class="disp disp-xl" style="{offset_ink([theme['ac']], 5)}">{titulo}</div>
            {lede}
            <div class="rule-d" style="margin:34px 0 8px 0;"></div>
            """,
            unsafe_allow_html=True,
        )

        kicker = f"{titulo} · {SITE['nombre']}"

        for i, item in enumerate(items):
            spacer(54)
            article(item, i, theme, kicker, flip=bool(i % 2))


def section_contact():
    """Contraportada: titular a sangre, datos de contacto como créditos."""
    with st.container(key="contact"):
        anchor("contacto")

        render_flow_field_bg(height_px=300, density=1.15, seed=3)

        links_html = "".join(
            f'<a class="btn" href="{l["url"]}" target="_blank">{l["nombre"]}</a>'
            for l in CONTACT["links"]
        )

        # OJO: este HTML se envía en UNA sola línea y sin líneas en blanco.
        # Si se deja indentado o con saltos, Streamlit lo interpreta como
        # bloque de código y muestra el código en crudo.
        contacto_html = (
            '<div class="back-cover">'
            '<div class="halftone bl" style="color:var(--mustard);"></div>'
            '<div class="back-inner">'
            f'<div class="folio">{SECTION_NUM["contacto"]:02d} — {SITE["eyebrow"][0]}</div>'
            f'<div class="disp disp-xxl" style="{offset_ink(["var(--terracotta)", "var(--espresso)"], 5)}">'
            f'{CONTACT["titulo_1"]}'
            f'<span class="l2 accent">{CONTACT["titulo_2"]}</span>'
            '</div>'
            '<div class="rule-d" style="margin:34px 0 22px 0; max-width:40em;"></div>'
            f'<p class="lede" style="margin:0 0 30px 0;">{CONTACT["texto"]}</p>'
            '<div class="contact-block">'
            '<div class="contact-line"><span class="k">Correo</span>'
            f'<span>{CONTACT["email"]}</span></div>'
            '<div class="contact-line"><span class="k">Teléfono</span>'
            f'<span>{CONTACT["telefono"]}</span></div>'
            '</div>'
            f'<a class="btn" href="mailto:{CONTACT["email"]}">✉ {CONTACT["email"]}</a>'
            f'{links_html}'
            '</div>'
            '</div>'
        )

        st.markdown(contacto_html, unsafe_allow_html=True)


def final_colophon():
    words = SITE["eyebrow"]
    st.markdown(
        '<div class="colofon-final">'
        f'<span class="folio">{SITE["nombre"]}</span>'
        f'<span class="folio">{words[0]} · {words[1]} · {words[2]}</span>'
        f'<span class="folio">{SITE["titulo_hero_1"]} {SITE["titulo_hero_2"]}</span>'
        '</div>',
        unsafe_allow_html=True,
    )


# =============================================================================
# ORDEN DE LA EDICIÓN
# =============================================================================

inject_css()
inject_css_layout()
inject_css_pieces()

render_missing_assets_banner()
masthead_and_nav()

section_cover()

with st.container(key="strip-1"):
    render_flow_field_bg(height_px=190, density=1.25, seed=1)

ticker_band(
    [SITE["eyebrow"][0], SITE["eyebrow"][1], SITE["eyebrow"][2], SITE["nombre"]]
)

section_about()
section_tools()

section_work(
    "inmersivos",
    "inmersivos",
    "INMERSIVOS",
    INMERSIVOS,
    THEMES["inmersivos"],
    standfirst="Proyectos que combinan diseño, tecnología y narrativa para crear experiencias que se recorren, no solo se miran.",
)

with st.container(key="strip-2"):
    render_flow_field_bg(height_px=140, density=0.9, seed=2)

section_work("interfaces", "interfaces", "INTERFACES", INTERFACES, THEMES["interfaces"])
section_work("visual", "visual", "VISUAL", VISUAL, THEMES["visual"])
section_work(
    "investigacion",
    "investigacion",
    "INVESTIGACIÓN",
    INVESTIGACION,
    THEMES["investigacion"],
)

ticker_band(
    [SITE["titulo_hero_1"], SITE["titulo_hero_2"], SITE["nombre"], SITE["eyebrow"][1]]
)

section_contact()
final_colophon()
