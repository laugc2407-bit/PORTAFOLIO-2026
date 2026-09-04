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
def proyecto(titulo, resumen, archivo="", galeria=None, rol="", herramientas="", resultado="", enlace=""):
    return {
        "titulo": titulo,              # nombre del proyecto
        "resumen": resumen,            # 1 frase corta
        "archivo": archivo,            # UNA imagen o video en la raíz del repo
        "galeria": galeria or [],      # o VARIAS imágenes/videos (carrusel)
        "rol": rol,                    # tu rol, ej: "Diseño UX + modelado 3D"
        "herramientas": herramientas,  # ej: "Unity, Blender, C++"
        "resultado": resultado,        # 1 frase: qué se logró / impacto
        "enlace": enlace,              # url a demo o repo (opcional)
    }


# Proyectos "inmersivos" — foto (.jpg/.png) o video (.mp4) en la raíz del repo
INMERSIVOS = [
    proyecto(
        titulo="Museo: el universo de Tim Burton",
        resumen="Experiencia inmersiva de tipo exploratoria para una exhibición temática sobre el universo de Tim Burton, recorriendo algunas de sus obras más emblemáticas.",
        archivo="tim_burton.jpg",
        rol="Desarrollo y montaje.",
        herramientas="Unity y Maya.",
    ),
    proyecto(
        titulo="Videojuego en VR: Vayquin",
        resumen="Videojuego de realidad virtual tipo exploratorio, navegando por un planeta desconocido para reparar la nave y volver a casa.",
        archivo="vayquin_vr.mp4",
        rol="Desarrollo y montaje.",
        herramientas="Unity.",
    ),
    proyecto(
        titulo="Videojuego: Bruna Lab (En proceso)",
        resumen="Videojuego 2D para niños que quieren aprender sobre química sin el riesgo de un laboratorio.",
        archivo="bruna_lab.jpg",
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
        titulo="Animación 3D: Eclipsaris",
        resumen="Cortometraje de animación 3D.",
        galeria=[
            "eclipsaris_01.jpg",
            "eclipsaris_02.jpg",
    
        ],
        rol="Rig de personajes y desarrollo del animatic.",
        herramientas="Maya y Filmora.",
    ),
    proyecto(
        titulo="Visuales",
        resumen="Visuales reactivas al movimiento y al sonido.",
        galeria=[
            "visuales_01.jpg",
            "visuales_02.jpg",
            "visuales_03.jpg",
            "visuales_04.jpg",
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
# DISEÑO — paleta "heat map" + 70s retro. No necesitas tocar esto.
# =============================================================================

PALETTE = {
    "void": "#1c0f14",      # casi negro, base fría del "mapa de calor"
    "plum": "#4a1259",      # violeta profundo
    "crimson": "#a3122c",   # rojo intenso
    "ember": "#e0501c",     # naranja quemado
    "amber": "#f2a922",     # mostaza / ámbar
    "cream": "#f6ecd2",     # crema papel retro
    "ink": "#20120a",       # texto oscuro sobre crema
}

FONT_DISPLAY = "Anton"
FONT_KICKER = "Bungee"
FONT_BODY = "Space Grotesk"


def echo_style(colors) -> str:
    """Sombra de texto por capas, tipo mala alineación de tinta en impresión
    offset de los 70 — es el efecto de firma del título principal."""
    steps = [(3 + i * 3, 3 + i * 3, c) for i, c in enumerate(colors)]
    return "text-shadow:" + ",".join(f"{x}px {y}px 0 {c}" for x, y, c in steps) + ";"


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Anton&family=Bungee&family=Space+Grotesk:wght@400;500;700&display=swap');

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
            font-family: '{FONT_BODY}', sans-serif;
        }}

        #MainMenu, footer, header {{visibility: hidden;}}
        .block-container {{
            padding: 0 !important;
            max-width: 100% !important;
        }}
        div[data-testid="stAppViewContainer"] {{
            background: var(--cream);
        }}

        /* grain overlay, retro film texture over the whole page */
        div[data-testid="stAppViewContainer"]::after {{
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 999;
            opacity: 0.05;
            mix-blend-mode: multiply;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
        }}

        h1, h2, h3, .heat-display {{
            font-family: '{FONT_DISPLAY}', sans-serif;
            text-transform: uppercase;
            line-height: 1.15;
            letter-spacing: -0.5px;
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
            font-family: '{FONT_KICKER}', sans-serif;
        }}

        /* ---------- signature retro flourishes ------------------------------ */
        .sunburst {{
            position: absolute;
            top: 50%; left: 6%;
            width: 1000px; height: 1000px;
            transform: translate(-50%, -50%);
            background: repeating-conic-gradient(from 0deg, var(--crimson) 0deg 7deg, transparent 7deg 16deg);
            opacity: 0.16;
            border-radius: 50%;
            animation: spin 70s linear infinite;
            pointer-events: none;
            z-index: 0;
        }}
        @keyframes spin {{ to {{ transform: translate(-50%, -50%) rotate(360deg); }} }}

        .halftone-block {{
            position: absolute;
            width: 240px; height: 240px;
            background-image: radial-gradient(currentColor 3px, transparent 3px);
            background-size: 17px 17px;
            opacity: 0.3;
            pointer-events: none;
            z-index: 0;
        }}
        .halftone-block.tr {{ top: 0; right: 0; clip-path: polygon(100% 0, 100% 100%, 0 0); }}
        .halftone-block.bl {{ bottom: 0; left: 0; clip-path: polygon(0 0, 100% 100%, 0 100%); }}

        /* fixed vertical "spine" label, readable through every color band */
        .spine {{
            position: fixed;
            left: 8px; top: 50%;
            writing-mode: vertical-rl;
            transform: rotate(180deg);
            font-family: '{FONT_KICKER}', sans-serif;
            font-size: 0.7rem;
            letter-spacing: 4px;
            color: #ffffff;
            mix-blend-mode: difference;
            z-index: 300;
            pointer-events: none;
        }}
        @media (max-width: 900px) {{ .spine {{ display: none; }} }}

        /* ---------- top nav (eyebrow words, matches original nav gimmick) --- */
        .eyebrow-bar {{
            display: flex;
            justify-content: space-between;
            padding: 14px 40px;
            font-size: 0.8rem;
            letter-spacing: 1px;
            color: var(--cream);
            border-bottom: 3px solid var(--ink);
        }}
        .eyebrow-bar span {{ opacity: 0.9; }}
        .eyebrow-bar span:nth-child(2) {{ color: var(--amber); }}
        .eyebrow-bar span:nth-child(3) {{ color: var(--ember); }}

        .nav-bar {{
            position: sticky;
            top: 0;
            z-index: 100;
            display: flex;
            flex-wrap: wrap;
            gap: 6px 20px;
            padding: 14px 40px;
            background: var(--void);
            border-bottom: 3px solid var(--ink);
        }}
        .nav-bar a {{
            color: var(--cream);
            text-decoration: none;
            font-size: 0.75rem;
            letter-spacing: 0.5px;
            padding: 6px 10px;
            border: 2px solid transparent;
            transition: transform 0.12s ease, border-color 0.12s ease, color 0.12s ease;
            display: inline-block;
        }}
        .nav-bar a:hover {{
            border-color: var(--amber);
            color: var(--amber);
            transform: translate(-2px, -2px);
            box-shadow: 3px 3px 0 var(--amber);
        }}

        /* ---------- generic section shells, one per "temperature" step -----
           Streamlit gives every st.container(key="...") a class
           "st-key-<key>" on its own wrapper div, so we style sections by
           targeting that class directly (this is the only reliable way to
           put a full background behind real Streamlit widgets). */
        .st-key-hero, .st-key-about, .st-key-tools, .st-key-immersive,
        .st-key-interfaces, .st-key-visual, .st-key-research, .st-key-contact {{
            padding: 100px 60px !important;
            position: relative;
            overflow: visible;
            border-bottom: 3px solid var(--ink);
        }}
        .st-key-divider {{ padding: 0 !important; position: relative; border-bottom: 3px solid var(--ink); }}
        .st-key-hero {{ padding: 0 !important; position: relative; overflow: hidden; }}

        .st-key-about       {{ background: var(--crimson) !important; color: var(--cream); }}
        .st-key-tools       {{ background: var(--amber)   !important; color: var(--void);  }}
        .st-key-immersive   {{ background: var(--void)    !important; color: var(--cream); }}
        .st-key-interfaces  {{ background: var(--plum)    !important; color: var(--cream); }}
        .st-key-visual      {{ background: var(--ember)   !important; color: var(--void);  }}
        .st-key-research    {{ background: var(--cream)   !important; color: var(--ink);   }}
        .st-key-contact     {{ background: var(--void)    !important; color: var(--cream); padding: 0 !important; }}

        .halftone {{
            background-image: radial-gradient(currentColor 1.4px, transparent 1.4px);
            background-size: 14px 14px;
            opacity: 0.12;
            position: absolute;
            inset: 0;
            pointer-events: none;
        }}

        .kicker {{
            font-size: 0.8rem;
            letter-spacing: 2px;
            display: inline-block;
            background: var(--crimson);
            color: var(--cream);
            padding: 5px 12px;
            transform: rotate(-2deg);
            margin-bottom: 18px;
            box-shadow: 4px 4px 0 var(--ink);
        }}

        .display-xl {{ font-size: clamp(3.4rem, 11vw, 9.5rem); }}
        .display-lg {{ font-size: clamp(2.6rem, 7vw, 5.6rem); }}
        .display-md {{ font-size: clamp(1.6rem, 3vw, 2.4rem); }}

        .body-lg {{ font-size: 1.3rem; line-height: 1.5; max-width: 640px; }}
        .body-md {{ font-size: 1.05rem; line-height: 1.55; max-width: 620px; }}

        .rule {{
            height: 2px;
            background: currentColor;
            opacity: 0.35;
            margin: 26px 0;
            border: none;
        }}

        .hero-wrap {{ position: relative; overflow: hidden; }}
        .hero-inner {{ position: relative; z-index: 2; }}

        /* ---------- herramientas: fichas tipo sticker con sombra dura ------- */
        .tool-chip {{
            border: 2px solid currentColor;
            padding: 10px 16px;
            font-weight: 400;
            font-size: 0.85rem;
            letter-spacing: 0.5px;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin: 6px 10px 6px 0;
            box-shadow: 4px 4px 0 var(--ink);
            transition: transform 0.12s ease, box-shadow 0.12s ease;
        }}
        .tool-chip:nth-child(odd) {{ transform: rotate(-2deg); }}
        .tool-chip:nth-child(even) {{ transform: rotate(2deg); }}
        .tool-chip:hover {{ transform: translate(4px, 4px) rotate(0deg); box-shadow: 0 0 0 var(--ink); }}

        /* ---------- botones de contacto: mismo trato "pop" retro ------------ */
        .cta-btn {{
            display: inline-block;
            border: 3px solid var(--cream);
            color: var(--cream) !important;
            padding: 13px 24px;
            font-size: 0.85rem;
            letter-spacing: 0.5px;
            text-decoration: none;
            margin: 8px 12px 8px 0;
            box-shadow: 5px 5px 0 var(--amber);
            transition: background 0.12s ease, color 0.12s ease, transform 0.12s ease, box-shadow 0.12s ease;
        }}
        .cta-btn:hover {{
            background: var(--cream);
            color: var(--void) !important;
            transform: translate(5px, 5px);
            box-shadow: 0 0 0 var(--amber);
        }}

        [data-testid="stImage"] img {{
            border: 3px solid var(--ink);
        }}
        video {{ border: 3px solid var(--ink); }}

        /* ---------- project sections (no accordion, always visible) -------- */
        [class*="st-key-proj-"] {{
            border: 3px solid currentColor !important;
            box-shadow: 6px 6px 0 rgba(0,0,0,0.3) !important;
            padding: 26px !important;
            margin: 0 0 34px 0 !important;
            position: relative !important;
            overflow: visible !important;
        }}
        [class*="st-key-proj-"]::before {{
            content: "";
            position: absolute;
            top: 0; right: 0;
            width: 90px; height: 90px;
            background-image: radial-gradient(currentColor 1.6px, transparent 1.6px);
            background-size: 12px 12px;
            opacity: 0.16;
            clip-path: polygon(100% 0, 100% 100%, 0 0);
            pointer-events: none;
        }}
        .proj-badge {{
            position: absolute;
            top: -20px; left: -20px;
            width: 54px; height: 54px;
            border-radius: 50%;
            background: var(--ink);
            color: var(--amber);
            border: 3px solid currentColor;
            display: flex; align-items: center; justify-content: center;
            font-family: '{FONT_KICKER}', sans-serif;
            font-size: 0.95rem;
            transform: rotate(-8deg);
            box-shadow: 4px 4px 0 rgba(0,0,0,0.35);
            z-index: 5;
        }}
        .proj-title {{
            font-family: '{FONT_DISPLAY}', sans-serif;
            text-transform: uppercase;
            font-size: 1.5rem;
            letter-spacing: -0.3px;
            line-height: 1.15;
            margin: 6px 0 16px 0;
        }}
        .proj-resumen {{
            font-size: 1rem;
            line-height: 1.5;
            opacity: 0.92;
            margin: 16px 0 14px 0;
        }}
        .proj-meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 0 0 14px 0;
        }}
        .proj-chip {{
            border: 2px solid currentColor;
            padding: 7px 12px;
            font-size: 0.82rem;
            line-height: 1.3;
        }}
        .proj-chip-label {{
            display: block;
            font-family: '{FONT_KICKER}', sans-serif;
            font-size: 0.58rem;
            letter-spacing: 1px;
            text-transform: uppercase;
            opacity: 0.65;
            margin-bottom: 3px;
        }}
        .proj-resultado {{
            font-style: italic;
            border-left: 3px solid currentColor;
            padding: 2px 0 2px 12px;
            margin: 0 0 16px 0;
            opacity: 0.92;
        }}
        .proj-link-btn {{
            display: inline-block;
            border: 3px solid currentColor;
            color: currentColor !important;
            padding: 9px 18px;
            font-family: '{FONT_KICKER}', sans-serif;
            font-size: 0.75rem;
            letter-spacing: 0.5px;
            text-decoration: none;
            box-shadow: 4px 4px 0 currentColor;
            transition: transform 0.12s ease, box-shadow 0.12s ease;
        }}
        .proj-link-btn:hover {{ transform: translate(4px,4px); box-shadow: 0 0 0 currentColor; }}

        /* the carousel itself is the only piece that still lives in an
           iframe (needed for the prev/next JS) — but its height is FIXED,
           so it never has the resize problems an accordion would have. */
        iframe {{ border: none !important; display: block; }}

        @media (max-width: 640px) {{
            .st-key-hero, .st-key-about, .st-key-tools, .st-key-immersive,
            .st-key-interfaces, .st-key-visual, .st-key-research, .st-key-contact {{
                padding: 60px 24px !important;
            }}
            .eyebrow-bar, .nav-bar {{ padding: 12px 18px; }}
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
        <div class="eyebrow-bar" style="background:var(--void);">
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
# con la estética heat map en vez de romper la página.
# =============================================================================
@st.cache_data(show_spinner=False)
def placeholder_image(label: str, w: int = 900, h: int = 600) -> bytes:
    colors = [(28, 15, 20), (74, 18, 89), (163, 18, 44), (224, 80, 28), (242, 169, 34)]
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
        draw.ellipse([i - 1, 0, i + 1, h], fill=(0, 0, 0, 18))
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
    except Exception:
        font = ImageFont.load_default()
    text = f"📷  {label}"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.rectangle(
        [w / 2 - tw / 2 - 20, h / 2 - th / 2 - 14, w / 2 + tw / 2 + 20, h / 2 + th / 2 + 14],
        fill=(28, 15, 20, 210),
    )
    draw.text((w / 2 - tw / 2, h / 2 - th / 2 - 4), text, font=font, fill=(246, 236, 210, 255))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=88)
    return buf.getvalue()


def show_media(rel_path: str, label: str, height: int = None):
    """Muestra <rel_path> (buscado en la raíz del repo). Si no existe,
    muestra un placeholder heat map."""
    path = ASSETS / rel_path
    if path.exists() and path.suffix.lower() in (".mp4", ".mov", ".webm"):
        st.video(str(path), loop=True, autoplay=True, muted=True)
    elif path.exists():
        st.image(str(path), use_container_width=True)
    else:
        st.image(placeholder_image(f"Añade: {rel_path}"), use_container_width=True)


def _media_data_uri(rel_path: str, label: str):
    """Convierte <rel_path> (buscado en la raíz del repo) en un data-uri
    para incrustarlo en HTML. Si el archivo no existe, genera un
    placeholder heat map con el mismo formato (imagen), para que el
    carrusel nunca se rompa."""
    path = ASSETS / rel_path
    if path.exists() and path.suffix.lower() in (".mp4", ".mov", ".webm"):
        ext = path.suffix.lstrip(".").lower()
        data = base64.b64encode(path.read_bytes()).decode()
        return "video", f"data:video/{ext};base64,{data}"
    if path.exists():
        ext = path.suffix.lstrip(".").lower()
        mime = "jpeg" if ext in ("jpg", "jpeg") else ext
        data = base64.b64encode(path.read_bytes()).decode()
        return "image", f"data:image/{mime};base64,{data}"
    data = base64.b64encode(placeholder_image(f"Añade: {rel_path}")).decode()
    return "image", f"data:image/jpeg;base64,{data}"


def carousel_widget(media_list, label, height=280):
    """Carrusel de fotos/video con altura FIJA. Al no depender de ningún
    resize dinámico (a diferencia de un acordeón), es la parte que se
    puede meter en un iframe sin que se corte ni se descuadre."""
    if not media_list:
        st.image(placeholder_image(f"Añade fotos/video: {label}"), use_container_width=True)
        return

    slides_html = []
    for i, rel in enumerate(media_list):
        kind, uri = _media_data_uri(rel, f"{label} {i + 1}")
        if kind == "video":
            autoplay = "autoplay " if i == 0 else ""
            slides_html.append(f'<div class="hm-slide"><video src="{uri}" {autoplay}muted loop playsinline></video></div>')
        else:
            slides_html.append(f'<div class="hm-slide"><img src="{uri}" alt="{label}"></div>')

    multi = len(slides_html) > 1
    dots_html = "".join(
        f'<span class="hm-dot{" active" if i == 0 else ""}" onclick="hmGo(this,{i})"></span>'
        for i in range(len(slides_html))
    )
    nav_html = (
        '<div class="hm-arrow hm-prev" onclick="hmPrev(this)">‹</div>'
        '<div class="hm-arrow hm-next" onclick="hmNext(this)">›</div>'
        if multi else ""
    )
    dots_wrap = f'<div class="hm-dots">{dots_html}</div>' if multi else ""

    html = f"""
    <style>
        * {{ box-sizing: border-box; }}
        html, body {{ margin: 0; padding: 0; background: transparent; }}
        .hm-carousel {{
            position: relative; width: 100%; height: {height}px;
            overflow: hidden; border: 2px solid {PALETTE['ink']};
            background: {PALETTE['void']};
        }}
        .hm-track {{ display: flex; height: 100%; transition: transform 0.4s ease; }}
        .hm-slide {{ flex: 0 0 100%; height: 100%; }}
        .hm-slide img, .hm-slide video {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
        .hm-arrow {{
            position: absolute; top: 50%; transform: translateY(-50%);
            width: 34px; height: 34px; border-radius: 50%;
            background: {PALETTE['ink']}; color: {PALETTE['amber']};
            border: 2px solid {PALETTE['amber']};
            font-size: 1.2rem; cursor: pointer;
            display: flex; align-items: center; justify-content: center;
            opacity: 0.88; z-index: 5; user-select: none;
            transition: transform 0.12s ease;
            font-family: sans-serif;
        }}
        .hm-arrow:hover {{ transform: translateY(-50%) scale(1.08); }}
        .hm-prev {{ left: 10px; }}
        .hm-next {{ right: 10px; }}
        .hm-counter {{
            position: absolute; bottom: 10px; right: 12px;
            background: {PALETTE['ink']}; color: {PALETTE['cream']};
            font-family: 'Bungee', sans-serif;
            font-size: 0.6rem; letter-spacing: 1px;
            padding: 3px 8px; border: 2px solid {PALETTE['amber']}; z-index: 5;
        }}
        .hm-dots {{ position: absolute; bottom: 12px; left: 12px; display: flex; gap: 6px; z-index: 5; }}
        .hm-dot {{
            width: 9px; height: 9px; border-radius: 50%;
            background: transparent; border: 2px solid {PALETTE['cream']};
            cursor: pointer; opacity: 0.65;
        }}
        .hm-dot.active {{ background: {PALETTE['amber']}; border-color: {PALETTE['amber']}; opacity: 1; }}
    </style>
    <div class="hm-carousel" data-index="0">
        <div class="hm-track">{''.join(slides_html)}</div>
        {nav_html}
        <div class="hm-counter">01 / {len(slides_html):02d}</div>
        {dots_wrap}
    </div>
    <script>
        function hmSetIndex(root, idx) {{
            const track = root.querySelector('.hm-track');
            const slides = root.querySelectorAll('.hm-slide');
            const n = slides.length;
            idx = ((idx % n) + n) % n;
            track.style.transform = 'translateX(' + (-idx * 100) + '%)';
            root.querySelectorAll('.hm-dot').forEach((d, i) => d.classList.toggle('active', i === idx));
            const counter = root.querySelector('.hm-counter');
            if (counter) {{
                counter.textContent = String(idx + 1).padStart(2, '0') + ' / ' + String(n).padStart(2, '0');
            }}
            slides.forEach((s, i) => {{
                const v = s.querySelector('video');
                if (v) {{
                    if (i === idx) {{ v.currentTime = 0; v.play().catch(() => {{}}); }}
                    else {{ v.pause(); }}
                }}
            }});
            root.dataset.index = idx;
        }}
        function hmPrev(el) {{ const r = el.closest('.hm-carousel'); hmSetIndex(r, parseInt(r.dataset.index || '0') - 1); }}
        function hmNext(el) {{ const r = el.closest('.hm-carousel'); hmSetIndex(r, parseInt(r.dataset.index || '0') + 1); }}
        function hmGo(el, idx) {{ const r = el.closest('.hm-carousel'); hmSetIndex(r, idx); }}
    </script>
    """
    st.components.v1.html(html, height=height + 4)


def project_section(item, idx, fg_hex):
    """Cada proyecto es su propio bloque, siempre visible (nada de
    desplegable): número de catálogo, carrusel, título, resumen, ficha
    corta (rol / herramientas), resultado y enlace opcional."""
    with st.container(key=f"proj-{slugify(item['titulo'])}-{idx}"):
        st.markdown(f'<div class="proj-badge">N°{idx + 1:02d}</div>', unsafe_allow_html=True)
        carousel_widget(_project_media_list(item), item["titulo"])
        st.markdown(f'<div class="proj-title">{item["titulo"]}</div>', unsafe_allow_html=True)
        if item.get("resumen"):
            st.markdown(f'<p class="proj-resumen">{item["resumen"]}</p>', unsafe_allow_html=True)

        chips = ""
        if item.get("rol"):
            chips += f'<div class="proj-chip"><span class="proj-chip-label">Rol</span>{item["rol"]}</div>'
        if item.get("herramientas"):
            chips += f'<div class="proj-chip"><span class="proj-chip-label">Herramientas</span>{item["herramientas"]}</div>'
        if chips:
            st.markdown(f'<div class="proj-meta">{chips}</div>', unsafe_allow_html=True)

        if item.get("resultado"):
            st.markdown(f'<p class="proj-resultado">✦ {item["resultado"]}</p>', unsafe_allow_html=True)
        if item.get("enlace"):
            st.markdown(f'<a class="proj-link-btn" href="{item["enlace"]}" target="_blank">Ver proyecto ↗</a>', unsafe_allow_html=True)


def render_flow_field_bg(height_px: int, density: float = 1.0, seed: int = 0):
    """Fondo animado tipo 'loop de TouchDesigner' — partículas ámbar/ember
    fluyendo sobre negro como un campo de ruido (flow field) — generado
    100% con canvas + JS. No carga ningún archivo, así que reemplaza los
    videos pesados (mp4 de varias decenas de MB) sin perder el look."""
    html = f"""
    <style>
        html, body {{ margin: 0; padding: 0; background: {PALETTE['void']}; overflow: hidden; }}
        #hm-bg-wrap {{ position: relative; width: 100%; height: {height_px}px; background: {PALETTE['void']}; }}
        #hm-bg-canvas {{ position: absolute; inset: 0; width: 100%; height: 100%; display: block; }}
    </style>
    <div id="hm-bg-wrap"><canvas id="hm-bg-canvas"></canvas></div>
    <script>
    (function() {{
        const canvas = document.getElementById('hm-bg-canvas');
        const ctx = canvas.getContext('2d');
        const wrap = document.getElementById('hm-bg-wrap');
        const DPR = Math.min(window.devicePixelRatio || 1, 2);
        const colors = ['{PALETTE['amber']}', '{PALETTE['ember']}', '{PALETTE['crimson']}'];
        const voidColor = '{PALETTE['void']}';
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
            for (let i = 0; i < count; i++) particles.push(spawn());
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
                    const fresh = spawn();
                    Object.assign(p, fresh);
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


# =============================================================================
# SECCIONES
# =============================================================================

def section_hero():
    with st.container(key="hero"):
        anchor("inicio")
        render_flow_field_bg(height_px=460, density=1.3, seed=1)
        st.markdown(
            f"""
            <div style="position:relative; padding:70px 60px 80px 60px; background:var(--void); color:var(--cream); overflow:hidden;">
                <div class="sunburst"></div>
                <div class="halftone-block tr" style="color:var(--amber);"></div>
                <div style="position:relative; z-index:2;">
                    <div class="kicker">{SITE['nombre']}</div>
                    <div class="heat-display display-xl" style="{echo_style(['var(--amber)', 'var(--ember)', 'var(--crimson)'])}">{SITE['titulo_hero_1']}<br>{SITE['titulo_hero_2']}</div>
                    <p class="body-lg" style="margin-top:26px;">{SITE['tagline']}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def section_about():
    with st.container(key="about"):
        anchor("sobre-mi")
        col1, col2 = st.columns([1.1, 1], gap="large")
        with col1:
            st.markdown(
                f"""
                <div class="heat-display display-lg" style="{echo_style(['var(--void)', 'var(--amber)'])}">{ABOUT['titulo']}</div>
                <p class="body-lg" style="margin-top:26px;">{ABOUT['texto']}</p>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            show_media(ABOUT["imagen"], "tu foto de perfil")


def section_tools():
    with st.container(key="tools"):
        anchor("herramientas")
        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--crimson)", "var(--plum)"])}">HERRAMIENTAS</div>',
            unsafe_allow_html=True,
        )
        chips = []
        for tool in TOOLS:
            logo_path = ASSETS / "tools" / tool["archivo"]
            if logo_path.exists():
                icon_html = f'<img src="data:image/png;base64,{base64.b64encode(logo_path.read_bytes()).decode()}" style="height:22px;">'
            else:
                icon_html = "◆"
            chips.append(f'<span class="tool-chip">{icon_html} {tool["nombre"]}</span>')
        st.markdown(f'<div style="margin-top:30px;">{"".join(chips)}</div>', unsafe_allow_html=True)


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
    expected = [ABOUT["imagen"]]
    for lst in (INMERSIVOS, INTERFACES, VISUAL, INVESTIGACION):
        for item in lst:
            expected.extend(_project_media_list(item))

    missing = [p for p in expected if p and not (ASSETS / p).exists()]
    if missing:
        with st.expander(f"⚠️ DEV: faltan {len(missing)} archivo(s) en la raíz del repo (clic para ver rutas exactas)"):
            st.write(
                "Streamlit no encontró estos archivos con ese nombre exacto "
                "(revisa mayúsculas/minúsculas, extensión y carpeta):"
            )
            for p in missing:
                st.code(str(ASSETS / p))


def project_grid(items, columns=2, fg_hex=None):
    fg_hex = fg_hex or PALETTE["cream"]
    cols = st.columns(columns, gap="large")
    for idx, item in enumerate(items):
        with cols[idx % columns]:
            project_section(item, idx, fg_hex)


def section_immersive():
    with st.container(key="immersive"):
        anchor("inmersivos")
        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--ember)", "var(--amber)"])}">INMERSIVOS</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="body-md" style="margin:20px 0 44px 0;">Proyectos que combinan diseño, tecnología y narrativa para crear experiencias que se recorren, no solo se miran.</p>',
            unsafe_allow_html=True,
        )
        project_grid(INMERSIVOS, fg_hex=PALETTE["cream"])


def section_divider():
    with st.container(key="divider"):
        render_flow_field_bg(height_px=200, density=0.8, seed=2)


def section_interfaces():
    with st.container(key="interfaces"):
        anchor("interfaces")
        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--crimson)", "var(--amber)"])}">INTERFACES</div>',
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:34px;'></div>", unsafe_allow_html=True)
        project_grid(INTERFACES, fg_hex=PALETTE["cream"])


def section_visual():
    with st.container(key="visual"):
        anchor("visual")
        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--plum)", "var(--crimson)"])}">VISUAL</div>',
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:34px;'></div>", unsafe_allow_html=True)
        project_grid(VISUAL, columns=3, fg_hex=PALETTE["void"])


def section_research():
    with st.container(key="research"):
        anchor("investigacion")
        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--crimson)", "var(--plum)"])}">INVESTIGACIÓN</div>',
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:34px;'></div>", unsafe_allow_html=True)
        project_grid(INVESTIGACION, fg_hex=PALETTE["ink"])


def section_contact():
    with st.container(key="contact"):
        anchor("contacto")
        render_flow_field_bg(height_px=380, density=1.1, seed=3)
        links_html = "".join(
            f'<a class="cta-btn" href="{l["url"]}" target="_blank">{l["nombre"]}</a>' for l in CONTACT["links"]
        )
        st.markdown(
            f"""
            <div style="position:relative; padding:60px 60px 80px 60px; background:var(--void); color:var(--cream); overflow:hidden;">
                <div class="halftone-block bl" style="color:var(--amber);"></div>
                <div style="position:relative; z-index:2;">
                    <div class="heat-display display-xl" style="{echo_style(['var(--amber)', 'var(--ember)', 'var(--crimson)'])}">{CONTACT['titulo_1']}<br>{CONTACT['titulo_2']}</div>
                    <p class="body-lg" style="margin:24px 0 28px 0;">{CONTACT['texto']}</p>
                    <a class="cta-btn" href="mailto:{CONTACT['email']}">✉ {CONTACT['email']}</a>
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
