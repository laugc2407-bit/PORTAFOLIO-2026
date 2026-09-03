# =============================================================================
#  PORTAFOLIO — app.py
#  Plantilla de portafolio "heat map / retro 70s" hecha en Streamlit.
#
#  👉 PARA EDITAR TEXTOS: todo lo que necesitas cambiar está en el bloque
#     "CONTENIDO" más abajo (busca la palabra CONTENIDO). No necesitas tocar
#     nada después de eso a menos que quieras cambiar el diseño.
#
#  👉 PARA AÑADIR IMÁGENES Y VIDEOS: no edites código. Solo copia tus
#     archivos dentro de la carpeta /assets con el nombre EXACTO que se pide
#     en cada comentario de la sección CONTENIDO. Mientras un archivo no
#     exista, la página muestra automáticamente un espacio de reemplazo con
#     el estilo heat map, así que nunca se ve roto.
#
#  Lee el archivo README.md para instrucciones de instalación y despliegue.
# =============================================================================

import base64
import io
from pathlib import Path

import streamlit as st
from PIL import Image, ImageDraw, ImageFont

ASSETS = Path(__file__).parent / "assets"

st.set_page_config(
    page_title="Portafolio",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =============================================================================
#  CONTENIDO  —  EDITA SOLO AQUÍ
# =============================================================================

SITE = {
    "nombre": "Tu Nombre Aquí",
    "titulo_hero_1": "PORTAFOLIO",
    "titulo_hero_2": "CREATIVO",
    "eyebrow": ["portafolio", "diseño", "interactivo"],   # las 3 palabras de la barra superior
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
    "texto": (
        "Escribe aquí 4-6 líneas sobre ti: quién eres, en qué te especializas "
        "y qué hace único tu trabajo. Ejemplo: 'Soy diseñador(a) de experiencias "
        "interactivas enfocado(a) en mundos inmersivos, interfaces y narrativa "
        "visual. Combino herramientas de tiempo real con procesos artesanales "
        "para crear proyectos que se sienten tanto como se ven.'"
    ),
    # Coloca tu foto en: assets/perfil.jpg  (retrato, cualquier proporción)
    "imagen": "perfil.jpg",
}

# Para cada herramienta puedes (opcional) poner un logo en assets/tools/<archivo>
# Si el archivo no existe, se muestra una "ficha" con el nombre en texto —
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

# =============================================================================
#  FICHA DE PROYECTO — usa siempre estos mismos campos, copia y pega una
#  entrada para crear un proyecto nuevo. Todos los campos son texto simple;
#  dejar "" (vacío) en link si no tienes uno.
#
#   "titulo"       -> nombre del proyecto
#   "resumen"      -> 1 línea, se ve siempre en la tarjeta (sin desplegar)
#   "rol"          -> tu rol en el proyecto (ej. "Diseño UX / modelado 3D")
#   "herramientas" -> separadas por coma (ej. "Unity, Figma, C++")
#   "descripcion"  -> 2-3 líneas, se ve solo al desplegar la tarjeta
#   "archivo"      -> ruta dentro de assets/projects/ (imagen o .mp4)
#   "link"         -> url opcional ("" si no aplica)
# =============================================================================

# Proyectos "inmersivos" — cada uno puede tener foto (.jpg/.png) o video (.mp4)
# Coloca el archivo en assets/projects/ con el nombre indicado.
INMERSIVOS = [
    {
        "titulo": "Museo: el universo de Tim Burton",
        "resumen": "Escribe aquí una sola línea que resuma el proyecto.",
        "rol": "Tu rol en el proyecto",
        "herramientas": "Herramienta 1, Herramienta 2",
        "descripcion": "Descripción corta: contexto, qué hiciste y el resultado.",
        "archivo": "projects/tim_burton.jpg",
        "link": "",
    },
    {
        "titulo": "Videojuego en VR: Vayquin",
        "resumen": "Escribe aquí una sola línea que resuma el proyecto.",
        "rol": "Tu rol en el proyecto",
        "herramientas": "Herramienta 1, Herramienta 2",
        "descripcion": "Descripción corta: contexto, qué hiciste y el resultado.",
        "archivo": "projects/vayquin_vr.mp4",
        "link": "",
    },
    {
        "titulo": "Videojuego: Bruna Lab",
        "resumen": "Escribe aquí una sola línea que resuma el proyecto.",
        "rol": "Tu rol en el proyecto",
        "herramientas": "Herramienta 1, Herramienta 2",
        "descripcion": "Descripción corta: contexto, qué hiciste y el resultado.",
        "archivo": "projects/bruna_lab.jpg",
        "link": "",
    },
    {
        "titulo": "Taller ABR/ABP",
        "resumen": "Escribe aquí una sola línea que resuma el proyecto.",
        "rol": "Tu rol en el proyecto",
        "herramientas": "Herramienta 1, Herramienta 2",
        "descripcion": "Descripción corta: contexto, qué hiciste y el resultado.",
        "archivo": "projects/abr_abp.jpg",
        "link": "",
    },
]

# Proyectos de "Interfaces"
INTERFACES = [
    {
        "titulo": "App: Mundo Ayuda Mayores",
        "resumen": "Escribe aquí una sola línea que resuma el proyecto.",
        "rol": "Tu rol en el proyecto",
        "herramientas": "Herramienta 1, Herramienta 2",
        "descripcion": "Descripción corta: contexto, qué hiciste y el resultado.",
        "archivo": "projects/mundo_ayuda_mayores.jpg",
        "link": "",
    },
    {
        "titulo": "App: Parque Éxpora",
        "resumen": "Escribe aquí una sola línea que resuma el proyecto.",
        "rol": "Tu rol en el proyecto",
        "herramientas": "Herramienta 1, Herramienta 2",
        "descripcion": "Descripción corta: contexto, qué hiciste y el resultado.",
        "archivo": "projects/parque_expora.jpg",
        "link": "",
    },
]

# Proyectos de "Visual" — modelado, animación 3D, piezas visuales
VISUAL = [
    {
        "titulo": "Modelado 3D",
        "resumen": "Escribe aquí una sola línea que resuma el proyecto.",
        "rol": "Tu rol en el proyecto",
        "herramientas": "Herramienta 1, Herramienta 2",
        "descripcion": "Descripción corta: contexto, qué hiciste y el resultado.",
        "archivo": "projects/modelado_3d.jpg",
        "link": "",
    },
    {
        "titulo": "Animación 3D: Eclipsaris",
        "resumen": "Escribe aquí una sola línea que resuma el proyecto.",
        "rol": "Tu rol en el proyecto",
        "herramientas": "Herramienta 1, Herramienta 2",
        "descripcion": "Descripción corta: contexto, qué hiciste y el resultado.",
        "archivo": "projects/eclipsaris.mp4",
        "link": "",
    },
    {
        "titulo": "Visuales",
        "resumen": "Escribe aquí una sola línea que resuma el proyecto.",
        "rol": "Tu rol en el proyecto",
        "herramientas": "Herramienta 1, Herramienta 2",
        "descripcion": "Descripción corta: contexto, qué hiciste y el resultado.",
        "archivo": "projects/visuales.jpg",
        "link": "",
    },
]

# Proyectos de "Investigación"
INVESTIGACION = [
    {
        "titulo": "Educación en los niños con TEA",
        "resumen": "Escribe aquí una sola línea que resuma el proyecto.",
        "rol": "Tu rol en el proyecto",
        "herramientas": "Herramienta 1, Herramienta 2",
        "descripcion": "Descripción corta: contexto, metodología y hallazgos.",
        "archivo": "projects/tea.jpg",
        "link": "",
    },
    {
        "titulo": "Investigación de mercados: Postobón",
        "resumen": "Escribe aquí una sola línea que resuma el proyecto.",
        "rol": "Tu rol en el proyecto",
        "herramientas": "Herramienta 1, Herramienta 2",
        "descripcion": "Descripción corta: objetivo del estudio y tu aporte.",
        "archivo": "projects/postobon.jpg",
        "link": "",
    },
]

CONTACT = {
    "titulo_1": "TRABAJEMOS",
    "titulo_2": "JUNTOS",
    "texto": "¿Tienes un proyecto en mente? Escríbeme y hablemos.",
    "email": "tu-correo@ejemplo.com",
    "links": [
        {"nombre": "LinkedIn", "url": "https://linkedin.com/in/tu-usuario"},
        {"nombre": "Instagram", "url": "https://instagram.com/tu-usuario"},
        {"nombre": "Behance", "url": "https://behance.net/tu-usuario"},
    ],
}

# ---- Videos de fondo (loops hechos en TouchDesigner) ----------------------
# Exporta desde TouchDesigner como .mp4, corto (5-15s), sin audio, y
# comprímelo (H.264, <10-15 MB idealmente) para que la web cargue rápido.
# Colócalos en /assets con estos nombres exactos:
BG_VIDEOS = {
    "hero": "hero_bg.mp4",        # fondo grande detrás del título principal
    "divider": "divider_bg.mp4",  # franja angosta entre "Sobre mí" y "Herramientas"
    "footer": "footer_bg.mp4",    # fondo detrás de "Trabajemos juntos"
}

# =============================================================================
#  DISEÑO — paleta "heat map" + 70s retro. No necesitas tocar esto.
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
        div[data-testid="stVerticalBlock"] {{
            gap: 0 !important;
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
            line-height: 1;
            letter-spacing: -1px;
            margin: 0;
            padding-top: 0.12em;
            overflow: visible;
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

        [class*="st-key-card-"] {{
            border: 3px solid currentColor !important;
            padding: 30px 26px !important;
            margin: 22px 0 !important;
            position: relative !important;
            overflow: visible !important;
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

        .card {{
            border: 3px solid currentColor;
            padding: 26px;
            height: 100%;
        }}
        .card h4 {{
            font-family: '{FONT_DISPLAY}', sans-serif;
            text-transform: uppercase;
            font-size: 1.5rem;
            margin: 0 0 10px 0;
        }}
        .card p {{ margin: 0; opacity: 0.9; line-height: 1.45; }}
        .card ul {{ margin: 10px 0 0 18px; padding: 0; }}
        .card li {{ margin-bottom: 4px; }}

        [class*="st-key-card-"] h4 {{
            font-family: '{FONT_DISPLAY}', sans-serif;
            text-transform: uppercase;
            font-size: 1.7rem;
            letter-spacing: -0.5px;
            margin: 0 0 10px 0;
        }}
        [class*="st-key-card-"] p {{ margin: 0; opacity: 0.9; line-height: 1.45; }}
        [class*="st-key-card-"] p.resumen {{ opacity: 0.85; font-size: 0.95rem; margin-top: 2px; }}
        [class*="st-key-card-"] ul {{ margin: 10px 0 0 18px; padding: 0; }}
        [class*="st-key-card-"] li {{ margin-bottom: 4px; }}

        /* desplegable de detalles de cada proyecto */
        [class*="st-key-card-"] [data-testid="stExpander"] {{
            margin-top: 16px;
            border: 2px solid currentColor;
            background: transparent;
        }}
        [class*="st-key-card-"] [data-testid="stExpander"] summary {{
            font-family: '{FONT_KICKER}', sans-serif;
            font-size: 0.75rem;
            letter-spacing: 0.5px;
            padding: 8px 12px;
        }}
        [class*="st-key-card-"] [data-testid="stExpanderDetails"] {{
            padding: 4px 14px 14px 14px;
            font-size: 0.95rem;
            line-height: 1.5;
        }}

        .card-badge {{
            position: absolute;
            top: -22px; left: -22px;
            width: 58px; height: 58px;
            border-radius: 50%;
            background: var(--ink);
            color: var(--amber);
            border: 3px solid currentColor;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.05rem;
            transform: rotate(-8deg);
            box-shadow: 4px 4px 0 rgba(0,0,0,0.35);
            z-index: 5;
        }}

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

        /* ---------- background video / placeholder strips ------------------ */
        .bgvideo-wrap {{
            position: relative;
            width: 100%;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .bgvideo-wrap video {{
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .bgvideo-label {{
            position: relative;
            z-index: 2;
            text-align: center;
            font-family: '{FONT_BODY}', sans-serif;
            font-weight: 700;
            color: var(--cream);
            text-shadow: 0 2px 10px rgba(0,0,0,0.6);
            padding: 20px;
        }}
        .heat-placeholder {{
            width: 100%;
            height: 100%;
            position: absolute;
            inset: 0;
            background: linear-gradient(120deg, var(--void), var(--plum), var(--crimson), var(--ember), var(--amber), var(--void));
            background-size: 300% 300%;
            animation: heatshift 12s ease infinite;
        }}
        @keyframes heatshift {{
            0%   {{ background-position: 0% 50%; }}
            50%  {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}

        [data-testid="stImage"] img {{
            border: 3px solid var(--ink);
        }}
        video {{ border: 3px solid var(--ink); }}

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
    st.markdown(
        f"""
        <div class="eyebrow-bar" style="background:var(--void);">
            <span>{words[0]}</span><span>{words[1]}</span><span>{words[2]}</span>
        </div>
        <div class="nav-bar">
            {''.join(f'<a href="#{anchor}">{label}</a>' for label, anchor in NAV)}
        </div>
        """,
        unsafe_allow_html=True,
    )


def anchor(name: str):
    st.markdown(f'<div id="{name}"></div>', unsafe_allow_html=True)


def slugify(text: str) -> str:
    return "".join(c if c.isalnum() else "-" for c in text.lower()).strip("-")


# =============================================================================
#  Utilidades de medios: si el archivo no existe, se genera un reemplazo
#  con la estética heat map en vez de romper la página.
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
    """Muestra assets/<rel_path>. Si no existe, muestra un placeholder heat map."""
    path = ASSETS / rel_path
    if path.exists() and path.suffix.lower() in (".mp4", ".mov", ".webm"):
        st.video(str(path), loop=True, autoplay=True, muted=True)
    elif path.exists():
        st.image(str(path), use_container_width=True)
    else:
        st.image(placeholder_image(f"Añade: assets/{rel_path}"), use_container_width=True)


def bg_video_section(key: str, height_px: int, fallback_text: str):
    """Franja de fondo para loops de TouchDesigner. Usa base64 para que el
    <video> cubra completamente el contenedor sin controles ni bordes."""
    filename = BG_VIDEOS.get(key)
    path = ASSETS / filename if filename else None
    if path and path.exists():
        data = base64.b64encode(path.read_bytes()).decode()
        ext = path.suffix.lstrip(".")
        st.markdown(
            f"""
            <div class="bgvideo-wrap" style="height:{height_px}px;">
                <video autoplay muted loop playsinline>
                    <source src="data:video/{ext};base64,{data}" type="video/{ext}">
                </video>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="bgvideo-wrap" style="height:{height_px}px;">
                <div class="heat-placeholder"></div>
                <div class="bgvideo-label">🎬 Espacio para loop de TouchDesigner<br>
                <span style="font-weight:400; opacity:0.85;">coloca tu archivo en assets/{filename}</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =============================================================================
#  SECCIONES
# =============================================================================

def section_hero():
    with st.container(key="hero"):
        anchor("inicio")
        bg_video_section("hero", height_px=460, fallback_text="hero")
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


def project_card(item, idx):
    with st.container(key=f"card-{slugify(item['titulo'])}-{idx}"):
        st.markdown(f'<div class="card-badge">N°{idx + 1:02d}</div>', unsafe_allow_html=True)
        show_media(item["archivo"], item["titulo"])
        st.markdown(
            f"""<h4>{item['titulo']}</h4><p class="resumen">{item.get('resumen', '')}</p>""",
            unsafe_allow_html=True,
        )
        with st.expander("Ver detalles", key=f"exp-{slugify(item['titulo'])}-{idx}"):
            if item.get("rol"):
                st.markdown(f"**Rol:** {item['rol']}")
            if item.get("herramientas"):
                st.markdown(f"**Herramientas:** {item['herramientas']}")
            if item.get("descripcion"):
                st.markdown(item["descripcion"])
            if item.get("link"):
                st.markdown(f"[Ver proyecto ↗]({item['link']})")


def project_grid(items):
    cols = st.columns(2, gap="large")
    for idx, item in enumerate(items):
        with cols[idx % 2]:
            project_card(item, idx)


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
        project_grid(INMERSIVOS)


def section_divider():
    with st.container(key="divider"):
        bg_video_section("divider", height_px=200, fallback_text="divider")


def section_interfaces():
    with st.container(key="interfaces"):
        anchor("interfaces")
        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--crimson)", "var(--amber)"])}">INTERFACES</div>',
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:34px;'></div>", unsafe_allow_html=True)
        project_grid(INTERFACES)


def section_visual():
    with st.container(key="visual"):
        anchor("visual")
        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--plum)", "var(--crimson)"])}">VISUAL</div>',
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:34px;'></div>", unsafe_allow_html=True)
        cols = st.columns(len(VISUAL), gap="medium")
        for idx, (col, item) in enumerate(zip(cols, VISUAL)):
            with col:
                project_card(item, idx)


def section_research():
    with st.container(key="research"):
        anchor("investigacion")
        st.markdown(
            f'<div class="heat-display display-lg" style="{echo_style(["var(--crimson)", "var(--plum)"])}">INVESTIGACIÓN</div>',
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:34px;'></div>", unsafe_allow_html=True)
        project_grid(INVESTIGACION)


def section_contact():
    with st.container(key="contact"):
        anchor("contacto")
        bg_video_section("footer", height_px=380, fallback_text="footer")
        st.markdown(
            f"""
            <div style="position:relative; padding:60px 60px 80px 60px; background:var(--void); color:var(--cream); overflow:hidden;">
                <div class="halftone-block bl" style="color:var(--amber);"></div>
                <div style="position:relative; z-index:2;">
                    <div class="heat-display display-xl" style="{echo_style(['var(--amber)', 'var(--ember)', 'var(--crimson)'])}">{CONTACT['titulo_1']}<br>{CONTACT['titulo_2']}</div>
                    <p class="body-lg" style="margin:24px 0 28px 0;">{CONTACT['texto']}</p>
                    <a class="cta-btn" href="mailto:{CONTACT['email']}">✉ {CONTACT['email']}</a>
                    {''.join(f'<a class="cta-btn" href="{l["url"]}" target="_blank">{l["nombre"]}</a>' for l in CONTACT['links'])}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =============================================================================
#  RENDER
# =============================================================================

inject_css()
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
