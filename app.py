# =====================================================
# PORTAFOLIO — app.py
# Portafolio creativo / diseño interactivo
# Streamlit + estética heat map / retro 70s
# =====================================================

import base64
import io
from pathlib import Path

import streamlit as st
from PIL import Image, ImageDraw, ImageFont


# =====================================================
# CONFIGURACIÓN GENERAL
# =====================================================

ASSETS = Path(__file__).parent / "assets"

st.set_page_config(
    page_title="Portafolio",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =====================================================
# CONTENIDO
# =====================================================

SITE = {
    "nombre": "Laura García",
    "titulo_hero_1": "PORTAFOLIO",
    "titulo_hero_2": "CREATIVO",
    "eyebrow": ["portafolio", "diseño", "interactivo"],
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


# =====================================================
# SOBRE MÍ
# =====================================================

ABOUT = {
    "titulo": "SOBRE MÍ",

    "texto": """
Me gusta crear cosas que hagan que las personas **quieran interactuar con ellas**.

Soy estudiante de Diseño Interactivo y disfruto moverme entre diferentes formas de crear: desde pensar una experiencia y diseñar una interfaz, hasta modelar un objeto en 3D, experimentar con código o convertir una idea en algo que se pueda jugar, explorar y vivir.

Me interesa especialmente ese punto donde **el diseño y la tecnología se encuentran con lo humano**. Por eso no busco hacer proyectos que simplemente se vean bien, sino experiencias que tengan una intención, despierten curiosidad y dejen algo en quien las vive.

Soy curiosa, aprendo haciendo y no me da miedo meterme en herramientas o áreas nuevas para llevar una idea un paso más allá.

**En pocas palabras: me gusta imaginar posibilidades y después descubrir cómo hacerlas realidad.**
""",

    # Coloca tu foto en:
    # assets/perfil.jpg
    "imagen": "perfil.jpg",
}


# =====================================================
# HERRAMIENTAS
# =====================================================

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


# =====================================================
# FUNCIÓN PARA CREAR PROYECTOS
# =====================================================

def proyecto(
    titulo,
    resumen,
    archivo="",
    rol="",
    herramientas="",
    resultado="",
    enlace="",
    galeria=None,
):
    """
    Crea la información de un proyecto.

    archivo:
        Imagen o video principal.

    galeria:
        Lista opcional de imágenes/videos para mostrar
        como carrusel.

    Si un proyecto tiene galeria, el carrusel tendrá prioridad
    sobre archivo.
    """

    return {
        "titulo": titulo,
        "resumen": resumen,
        "archivo": archivo,
        "rol": rol,
        "herramientas": herramientas,
        "resultado": resultado,
        "enlace": enlace,
        "galeria": galeria or [],
    }


# =====================================================
# PROYECTOS — INMERSIVOS
# =====================================================

INMERSIVOS = [

    proyecto(
        titulo="Museo: el universo de Tim Burton",

        resumen=(
            "Experiencia inmersiva de tipo exploratoria para una "
            "exhibición temática sobre el universo de Tim Burton, "
            "recorriendo algunas de sus obras más emblemáticas."
        ),

        archivo="projects/tim_burton.jpg",

        rol="Desarrollo y montaje.",

        herramientas="Unity y Maya.",
    ),


    proyecto(
        titulo="Videojuego en VR: Vayquin",

        resumen=(
            "Videojuego de realidad virtual tipo exploratorio, "
            "navegando por un planeta desconocido para reparar "
            "la nave y volver a casa."
        ),

        archivo="projects/vayquin_vr.mp4",

        rol="Desarrollo y montaje.",

        herramientas="Unity.",
    ),


    proyecto(
        titulo="Videojuego: Bruna Lab (En proceso)",

        resumen=(
            "Videojuego 2D para niños que quieren aprender "
            "sobre química sin el riesgo de un laboratorio."
        ),

        archivo="projects/bruna_lab.jpg",

        rol="Project Manager.",
    ),
]


# =====================================================
# PROYECTOS — INTERFACES
# =====================================================

INTERFACES = [

    proyecto(
        titulo="App: Mundo Ayuda Mayores",

        resumen=(
            "Aplicativo para mayores de edad con baja alfabetización "
            "digital para facilitar tareas diarias."
        ),

        archivo="projects/mundo_ayuda_mayores.jpg",

        rol="Diseño de experiencia y de interfaz (UX/UI).",

        herramientas="Figma y Canva.",
    ),


    proyecto(
        titulo="App: Parque Explora",

        resumen=(
            "Aplicativo para facilitar la experiencia de espera "
            "en la cafetería del parque."
        ),

        archivo="projects/parque_expora.jpg",

        rol="Diseño de experiencia y de interfaz (UX/UI).",

        herramientas="Figma y Canva.",
    ),


    proyecto(
        titulo="App: Antioquia, territorio multicultural (En proceso)",

        resumen=(
            "Aplicativo para aprender sobre la diversidad "
            "cultural de Antioquia."
        ),

        # IMPORTANTE:
        # Cambia este nombre si tu archivo tiene otro nombre.
        archivo="projects/antioquia_multicultural.jpg",

        rol="Diseño de experiencia y de interfaz (UX/UI).",

        herramientas="Figma y Canva.",
    ),
]


# =====================================================
# PROYECTOS — VISUAL
# =====================================================

VISUAL = [

    # -------------------------------------------------
    # MODELADO 3D
    # -------------------------------------------------

    proyecto(
        titulo="Modelado 3D",

        resumen=(
            "Selección de piezas y ejercicios de modelado 3D."
        ),

        # Imagen principal por si todavía no tienes galería.
        archivo="projects/modelado_3d.jpg",

        herramientas="Maya y Adobe Substance 3D Painter.",

        # =================================================
        # AGREGA AQUÍ TODAS LAS IMÁGENES DEL PROYECTO
        #
        # Ejemplo:
        #
        # "galeria": [
        #     "projects/modelado_3d.jpg",
        #     "projects/modelado_3d_02.jpg",
        #     "projects/modelado_3d_03.jpg",
        #     "projects/modelado_3d_04.jpg",
        # ],
        #
        # =================================================

        galeria=[
            "projects/modelado_3d.jpg",
        ],
    ),


    # -------------------------------------------------
    # ECLIPSARIS
    # -------------------------------------------------

    proyecto(
        titulo="Animación 3D: Eclipsaris",

        resumen=(
            "Cortometraje de animación 3D."
        ),

        archivo="projects/eclipsaris.mp4",

        rol="Rig de los personajes y desarrollo del animatic.",

        herramientas="Maya y Filmora.",

        galeria=[
            "projects/eclipsaris.mp4",
        ],
    ),


    # -------------------------------------------------
    # VISUALES / TOUCHDESIGNER
    # -------------------------------------------------

    proyecto(
        titulo="Visuales",

        resumen=(
            "Visuales reactivas al movimiento y al sonido."
        ),

        archivo="projects/visuales.jpg",

        herramientas="TouchDesigner.",

        # Puedes añadir aquí todas las capturas o videos.
        #
        # Ejemplo:
        #
        # "galeria": [
        #     "projects/visuales.jpg",
        #     "projects/visuales_02.jpg",
        #     "projects/visuales_03.jpg",
        #     "projects/visuales_04.mp4",
        # ],

        galeria=[
            "projects/visuales.jpg",
        ],
    ),
]


# =====================================================
# PROYECTOS — INVESTIGACIÓN
# =====================================================

INVESTIGACION = [

    proyecto(
        titulo="Educación en niños con TEA",

        resumen=(
            "Investigación sobre estrategias usadas en la educación "
            "para niños con TEA y propuestas a través del diseño."
        ),

        archivo="projects/tea.jpg",
    ),


    proyecto(
        titulo="Investigación de mercados: Postobón",

        resumen=(
            "Estudio de mercado sobre el comportamiento "
            "posconsumo del consumidor."
        ),

        archivo="projects/postobon.jpg",
    ),
]


# =====================================================
# CONTACTO
# =====================================================

CONTACT = {
    "titulo_1": "TRABAJEMOS",
    "titulo_2": "JUNTOS",

    "texto": (
        "¿Tienes un proyecto en mente? "
        "Escríbeme y hablemos."
    ),

    "email": "lngarciac@eafit.edu.co",

    "telefono": "+57 3103777407",

    "links": [
        {
            "nombre": "LinkedIn",
            "url": "https://linkedin.com/in/tu-usuario",
        },
    ],
}


# =====================================================
# VIDEOS DE FONDO
# =====================================================

BG_VIDEOS = {
    "hero": "hero_bg.mp4",
    "divider": "divider_bg.mp4",
    "footer": "footer_bg.mp4",
}


# =====================================================
# PALETA
# =====================================================

PALETTE = {
    "void": "#1c0f14",
    "plum": "#4a1259",
    "crimson": "#a3122c",
    "ember": "#e0501c",
    "amber": "#f2a922",
    "cream": "#f6ecd2",
    "ink": "#20120a",
}


FONT_DISPLAY = "Anton"
FONT_KICKER = "Bungee"
FONT_BODY = "Space Grotesk"


# =====================================================
# EFECTO DE SOMBRA
# =====================================================

def echo_style(colors) -> str:
    """
    Crea la sombra de texto por capas,
    inspirada en impresión retro de los años 70.
    """

    steps = [
        (3 + i * 3, 3 + i * 3, c)
        for i, c in enumerate(colors)
    ]

    return (
        "text-shadow:"
        + ",".join(
            f"{x}px {y}px 0 {c}"
            for x, y, c in steps
        )
        + ";"
    )


# =====================================================
# CSS
# =====================================================

def inject_css():

    st.markdown(
        f"""
        <style>

        @import url(
            'https://fonts.googleapis.com/css2?family=Anton&family=Bungee&family=Space+Grotesk:wght@400;500;700&display=swap'
        );


        :root {{
            --void: {PALETTE['void']};
            --plum: {PALETTE['plum']};
            --crimson: {PALETTE['crimson']};
            --ember: {PALETTE['ember']};
            --amber: {PALETTE['amber']};
            --cream: {PALETTE['cream']};
            --ink: {PALETTE['ink']};
        }}


        html,
        body,
        [class*="css"] {{
            font-family: '{FONT_BODY}', sans-serif;
        }}


        #MainMenu,
        footer,
        header {{
            visibility: hidden;
        }}


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


        /* ---------------------------------------------
           TEXTURA DE PELÍCULA
        --------------------------------------------- */

        div[data-testid="stAppViewContainer"]::after {{
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 999;
            opacity: 0.05;
            mix-blend-mode: multiply;

            background-image: url(
                "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"
            );
        }}


        /* ---------------------------------------------
           TITULOS
        --------------------------------------------- */

        h1,
        h2,
        h3,
        .heat-display {{
            font-family: '{FONT_DISPLAY}', sans-serif;
            text-transform: uppercase;
            line-height: 1.15;
            letter-spacing: -0.5px;
            margin: 0;
            padding: 0.15em 0;
            overflow: visible;
        }}


        div[data-testid="stVerticalBlock"],
        div[data-testid="element-container"],
        div[data-testid="stMarkdown"],
        div[data-testid="stMarkdownContainer"] {{
            overflow: visible !important;
        }}


        .kicker,
        .nav-bar a,
        .tool-chip,
        .card-badge,
        .cta-btn,
        .eyebrow-bar span {{
            font-family: '{FONT_KICKER}', sans-serif;
        }}


        /* ---------------------------------------------
           DECORACIÓN RETRO
        --------------------------------------------- */

        .sunburst {{
            position: absolute;

            top: 50%;
            left: 6%;

            width: 1000px;
            height: 1000px;

            transform: translate(-50%, -50%);

            background:
                repeating-conic-gradient(
                    from 0deg,
                    var(--crimson) 0deg 7deg,
                    transparent 7deg 16deg
                );

            opacity: 0.16;

            border-radius: 50%;

            animation: spin 70s linear infinite;

            pointer-events: none;
            z-index: 0;
        }}


        @keyframes spin {{
            to {{
                transform:
                    translate(-50%, -50%)
                    rotate(360deg);
            }}
        }}


        .halftone-block {{
            position: absolute;

            width: 240px;
            height: 240px;

            background-image:
                radial-gradient(
                    currentColor 3px,
                    transparent 3px
                );

            background-size: 17px 17px;

            opacity: 0.3;

            pointer-events: none;

            z-index: 0;
        }}


        .halftone-block.tr {{
            top: 0;
            right: 0;

            clip-path:
                polygon(
                    100% 0,
                    100% 100%,
                    0 0
                );
        }}


        .halftone-block.bl {{
            bottom: 0;
            left: 0;

            clip-path:
                polygon(
                    0 0,
                    100% 100%,
                    0 100%
                );
        }}


        /* ---------------------------------------------
           SPINE
        --------------------------------------------- */

        .spine {{
            position: fixed;

            left: 8px;
            top: 50%;

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


        @media (max-width: 900px) {{
            .spine {{
                display: none;
            }}
        }}


        /* ---------------------------------------------
           BARRA SUPERIOR
        --------------------------------------------- */

        .eyebrow-bar {{
            display: flex;

            justify-content: space-between;

            padding: 14px 40px;

            font-size: 0.8rem;

            letter-spacing: 1px;

            color: var(--cream);

            border-bottom:
                3px solid var(--ink);
        }}


        .eyebrow-bar span {{
            opacity: 0.9;
        }}


        .eyebrow-bar span:nth-child(2) {{
            color: var(--amber);
        }}


        .eyebrow-bar span:nth-child(3) {{
            color: var(--ember);
        }}


        /* ---------------------------------------------
           NAV
        --------------------------------------------- */

        .nav-bar {{
            position: sticky;

            top: 0;

            z-index: 100;

            display: flex;

            flex-wrap: wrap;

            gap: 6px 20px;

            padding: 14px 40px;

            background: var(--void);

            border-bottom:
                3px solid var(--ink);
        }}


        .nav-bar a {{
            color: var(--cream);

            text-decoration: none;

            font-size: 0.75rem;

            letter-spacing: 0.5px;

            padding: 6px 10px;

            border: 2px solid transparent;

            transition:
                transform 0.12s ease,
                border-color 0.12s ease,
                color 0.12s ease;

            display: inline-block;
        }}


        .nav-bar a:hover {{
            border-color: var(--amber);

            color: var(--amber);

            transform:
                translate(-2px, -2px);

            box-shadow:
                3px 3px 0 var(--amber);
        }}


        /* ---------------------------------------------
           SECCIONES
        --------------------------------------------- */

        .st-key-hero,
        .st-key-about,
        .st-key-tools,
        .st-key-immersive,
        .st-key-interfaces,
        .st-key-visual,
        .st-key-research,
        .st-key-contact {{

            padding: 100px 60px !important;

            position: relative;

            overflow: visible;

            border-bottom:
                3px solid var(--ink);
        }}


        .st-key-divider {{
            padding: 0 !important;

            position: relative;

            border-bottom:
                3px solid var(--ink);
        }}


        .st-key-hero {{
            padding: 0 !important;

            position: relative;

            overflow: hidden;
        }}


        .st-key-about {{
            background: var(--crimson) !important;
            color: var(--cream);
        }}


        .st-key-tools {{
            background: var(--amber) !important;
            color: var(--void);
        }}


        .st-key-immersive {{
            background: var(--void) !important;
            color: var(--cream);
        }}


        .st-key-interfaces {{
            background: var(--plum) !important;
            color: var(--cream);
        }}


        .st-key-visual {{
            background: var(--ember) !important;
            color: var(--void);
        }}


        .st-key-research {{
            background: var(--cream) !important;
            color: var(--ink);
        }}


        .st-key-contact {{
            background: var(--void) !important;
            color: var(--cream);

            padding: 0 !important;
        }}


        /* ---------------------------------------------
           CARDS
        --------------------------------------------- */

        [class*="st-key-card-"] {{
            border:
                3px solid currentColor !important;

            padding:
                30px 26px !important;

            margin:
                22px 0 !important;

            position:
                relative !important;

            overflow:
                visible !important;
        }}


        .card {{
            border:
                3px solid currentColor;

            padding: 26px;

            height: 100%;
        }}


        .card h4 {{
            font-family:
                '{FONT_DISPLAY}', sans-serif;

            text-transform:
                uppercase;

            font-size:
                1.5rem;

            margin:
                0 0 10px 0;
        }}


        .card p {{
            margin: 0;

            opacity: 0.9;

            line-height: 1.45;
        }}


        .card ul {{
            margin:
                10px 0 0 18px;

            padding: 0;
        }}


        .card li {{
            margin-bottom: 4px;
        }}


        [class*="st-key-card-"] h4 {{
            font-family:
                '{FONT_DISPLAY}', sans-serif;

            text-transform:
                uppercase;

            font-size:
                1.7rem;

            letter-spacing:
                -0.5px;

            margin:
                0 0 10px 0;
        }}


        [class*="st-key-card-"] p {{
            margin: 0;

            opacity: 0.9;

            line-height: 1.45;
        }}


        [class*="st-key-card-"] ul {{
            margin:
                10px 0 0 18px;

            padding: 0;
        }}


        [class*="st-key-card-"] li {{
            margin-bottom: 4px;
        }}


        /* ---------------------------------------------
           BADGE
        --------------------------------------------- */

        .card-badge {{
            position: absolute;

            top: -22px;
            left: -22px;

            width: 58px;
            height: 58px;

            border-radius: 50%;

            background: var(--ink);

            color: var(--amber);

            border:
                3px solid currentColor;

            display: flex;

            align-items: center;

            justify-content: center;

            font-size: 1.05rem;

            transform: rotate(-8deg);

            box-shadow:
                4px 4px 0 rgba(0,0,0,0.35);

            z-index: 5;
        }}


        /* ---------------------------------------------
           TOOL CHIPS
        --------------------------------------------- */

        .tool-chip {{
            border:
                2px solid currentColor;

            padding:
                10px 16px;

            font-weight: 400;

            font-size: 0.85rem;

            letter-spacing: 0.5px;

            display: inline-flex;

            align-items: center;

            gap: 8px;

            margin:
                6px 10px 6px 0;

            box-shadow:
                4px 4px 0 var(--ink);

            transition:
                transform 0.12s ease,
                box-shadow 0.12s ease;
        }}


        .tool-chip:nth-child(odd) {{
            transform:
                rotate(-2deg);
        }}


        .tool-chip:nth-child(even) {{
            transform:
                rotate(2deg);
        }}


        .tool-chip:hover {{
            transform:
                translate(4px, 4px)
                rotate(0deg);

            box-shadow:
                0 0 0 var(--ink);
        }}


        /* ---------------------------------------------
           CTA
        --------------------------------------------- */

        .cta-btn {{
            display: inline-block;

            border:
                3px solid var(--cream);

            color:
                var(--cream) !important;

            padding:
                13px 24px;

            font-size:
                0.85rem;

            letter-spacing:
                0.5px;

            text-decoration:
                none;

            margin:
                8px 12px 8px 0;

            box-shadow:
                5px 5px 0 var(--amber);

            transition:
                background 0.12s ease,
                color 0.12s ease,
                transform 0.12s ease,
                box-shadow 0.12s ease;
        }}


        .cta-btn:hover {{
            background:
                var(--cream);

            color:
                var(--void) !important;

            transform:
                translate(5px, 5px);

            box-shadow:
                0 0 0 var(--amber);
        }}


        /* ---------------------------------------------
           VIDEOS DE FONDO
        --------------------------------------------- */

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

            font-family:
                '{FONT_BODY}', sans-serif;

            font-weight: 700;

            color:
                var(--cream);

            text-shadow:
                0 2px 10px rgba(0,0,0,0.6);

            padding: 20px;
        }}


        .heat-placeholder {{
            width: 100%;
            height: 100%;

            position: absolute;

            inset: 0;

            background:
                linear-gradient(
                    120deg,
                    var(--void),
                    var(--plum),
                    var(--crimson),
                    var(--ember),
                    var(--amber),
                    var(--void)
                );

            background-size: 300% 300%;

            animation:
                heatshift 12s ease infinite;
        }}


        @keyframes heatshift {{
            0% {{
                background-position:
                    0% 50%;
            }}

            50% {{
                background-position:
                    100% 50%;
            }}

            100% {{
                background-position:
                    0% 50%;
            }}
        }}


        /* ---------------------------------------------
           IMÁGENES Y VIDEOS
        --------------------------------------------- */

        [data-testid="stImage"] img {{
            border:
                3px solid var(--ink);
        }}


        video {{
            border:
                3px solid var(--ink);
        }}


        /* ---------------------------------------------
           CARRUSEL
        --------------------------------------------- */

        .carousel-counter {{
            text-align: center;

            font-family:
                '{FONT_KICKER}', sans-serif;

            font-size:
                0.8rem;

            letter-spacing:
                1px;

            padding:
                10px;

            color:
                currentColor;

            opacity:
                0.8;
        }}


        .carousel-caption {{
            text-align: center;

            font-family:
                '{FONT_BODY}', sans-serif;

            font-size:
                0.8rem;

            margin-top:
                4px;

            opacity:
                0.7;
        }}


        /* ---------------------------------------------
           MOBILE
        --------------------------------------------- */

        @media (max-width: 640px) {{

            .st-key-hero,
            .st-key-about,
            .st-key-tools,
            .st-key-immersive,
            .st-key-interfaces,
            .st-key-visual,
            .st-key-research,
            .st-key-contact {{

                padding:
                    60px 24px !important;
            }}


            .eyebrow-bar,
            .nav-bar {{
                padding:
                    12px 18px;
            }}


            .sunburst {{
                width: 600px;
                height: 600px;
            }}
        }}

        </style>
        """,

        unsafe_allow_html=True,
    )


# =====================================================
# NAVEGACIÓN
# =====================================================

def eyebrow_and_nav():

    words = SITE["eyebrow"]


    st.markdown(
        f"""
        <div class="spine">
            {SITE['nombre']} —
            {words[0]} ·
            {words[1]} ·
            {words[2]}
        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown(
        f"""
        <div
            class="eyebrow-bar"
            style="background:var(--void);"
        >
            <span>{words[0]}</span>
            <span>{words[1]}</span>
            <span>{words[2]}</span>
        </div>


        <div class="nav-bar">

            {
                ''.join(
                    f'<a href="#{anchor}">{label}</a>'
                    for label, anchor in NAV
                )
            }

        </div>
        """,

        unsafe_allow_html=True,
    )


# =====================================================
# ANCLAS
# =====================================================

def anchor(name: str):

    st.markdown(
        f'<div id="{name}"></div>',
        unsafe_allow_html=True,
    )


# =====================================================
# SLUGIFY
# =====================================================

def slugify(text: str) -> str:

    return "".join(
        c if c.isalnum() else "-"
        for c in text.lower()
    ).strip("-")


# =====================================================
# PLACEHOLDER
# =====================================================

@st.cache_data(show_spinner=False)
def placeholder_image(
    label: str,
    w: int = 900,
    h: int = 600,
) -> bytes:

    colors = [
        (28, 15, 20),
        (74, 18, 89),
        (163, 18, 44),
        (224, 80, 28),
        (242, 169, 34),
    ]


    img = Image.new(
        "RGB",
        (w, h),
    )


    px = img.load()

    n = len(colors) - 1


    for x in range(w):

        t = (
            x /
            max(w - 1, 1)
        ) * n

        i = min(
            int(t),
            n - 1,
        )

        frac = t - i

        c0 = colors[i]
        c1 = colors[i + 1]


        r = int(
            c0[0]
            + (c1[0] - c0[0]) * frac
        )

        g = int(
            c0[1]
            + (c1[1] - c0[1]) * frac
        )

        b = int(
            c0[2]
            + (c1[2] - c0[2]) * frac
        )


        for y in range(h):

            px[x, y] = (
                r,
                g,
                b,
            )


    draw = ImageDraw.Draw(
        img,
        "RGBA",
    )


    for i in range(
        0,
        w,
        14,
    ):

        draw.ellipse(
            [
                i - 1,
                0,
                i + 1,
                h,
            ],

            fill=(
                0,
                0,
                0,
                18,
            ),
        )


    try:

        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            26,
        )

    except Exception:

        font = ImageFont.load_default()


    text = f"📷  {label}"


    bbox = draw.textbbox(
        (0, 0),
        text,
        font=font,
    )


    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]


    draw.rectangle(
        [
            w / 2 - tw / 2 - 20,
            h / 2 - th / 2 - 14,
            w / 2 + tw / 2 + 20,
            h / 2 + th / 2 + 14,
        ],

        fill=(
            28,
            15,
            20,
            210,
        ),
    )


    draw.text(
        (
            w / 2 - tw / 2,
            h / 2 - th / 2 - 4,
        ),

        text,

        font=font,

        fill=(
            246,
            236,
            210,
            255,
        ),
    )


    buf = io.BytesIO()

    img.save(
        buf,
        format="JPEG",
        quality=88,
    )


    return buf.getvalue()


# =====================================================
# MOSTRAR MEDIA
# =====================================================

def show_media(
    rel_path: str,
    label: str,
    height: int = None,
):

    """
    Muestra una imagen o video.

    Si el archivo no existe,
    muestra automáticamente un placeholder.
    """

    path = ASSETS / rel_path


    if (
        path.exists()
        and path.suffix.lower()
        in (".mp4", ".mov", ".webm")
    ):

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
            placeholder_image(
                f"Añade: assets/{rel_path}"
            ),

            use_container_width=True,
        )


# =====================================================
# CARRUSEL
# =====================================================

def show_carousel(
    images,
    label,
    key,
):
    """
    Carrusel navegable para imágenes y videos.

    Usa st.session_state para recordar
    qué imagen está viendo el usuario.
    """

    if not images:
        return


    state_key = f"carousel_{key}"


    if state_key not in st.session_state:

        st.session_state[state_key] = 0


    current = st.session_state[state_key]


    current = current % len(images)


    st.session_state[state_key] = current


    # -------------------------------------------------
    # MEDIA ACTUAL
    # -------------------------------------------------

    current_media = images[current]


    show_media(
        current_media,
        label,
    )


    # -------------------------------------------------
    # CONTADOR
    # -------------------------------------------------

    st.markdown(
        f"""
        <div class="carousel-counter">
            {current + 1} / {len(images)}
        </div>
        """,

        unsafe_allow_html=True,
    )


    # -------------------------------------------------
    # BOTONES
    # -------------------------------------------------

    col1, col2, col3 = st.columns(
        [1, 2, 1],
        gap="small",
    )


    with col1:

        if st.button(
            "← ANTERIOR",
            key=f"{key}_prev",
            use_container_width=True,
        ):

            st.session_state[state_key] = (
                current - 1
            ) % len(images)

            st.rerun()


    with col2:

        st.markdown(
            f"""
            <div class="carousel-caption">
                Explora el proyecto
            </div>
            """,

            unsafe_allow_html=True,
        )


    with col3:

        if st.button(
            "SIGUIENTE →",
            key=f"{key}_next",
            use_container_width=True,
        ):

            st.session_state[state_key] = (
                current + 1
            ) % len(images)

            st.rerun()


# =====================================================
# VIDEOS DE FONDO
# =====================================================

def bg_video_section(
    key: str,
    height_px: int,
    fallback_text: str,
):

    """
    Franja de fondo para loops de TouchDesigner.

    Si existe el video, lo reproduce automáticamente.

    Si no existe, muestra un placeholder heat map.
    """

    filename = BG_VIDEOS.get(key)


    path = (
        ASSETS / filename
        if filename
        else None
    )


    if path and path.exists():

        data = base64.b64encode(
            path.read_bytes()
        ).decode()


        ext = path.suffix.lstrip(".")


        st.markdown(
            f"""
            <div
                class="bgvideo-wrap"
                style="height:{height_px}px;"
            >

                <video
                    autoplay
                    muted
                    loop
                    playsinline
                >

                    <source
                        src="data:video/{ext};base64,{data}"
                        type="video/{ext}"
                    >

                </video>

            </div>
            """,

            unsafe_allow_html=True,
        )


    else:

        st.markdown(
            f"""
            <div
                class="bgvideo-wrap"
                style="height:{height_px}px;"
            >

                <div class="heat-placeholder"></div>

                <div class="bgvideo-label">

                    🎬 Espacio para loop
                    de TouchDesigner

                    <br>

                    <span
                        style="
                            font-weight:400;
                            opacity:0.85;
                        "
                    >
                        coloca tu archivo en
                        assets/{filename}
                    </span>

                </div>

            </div>
            """,

            unsafe_allow_html=True,
        )


# =====================================================
# SECCIÓN HERO
# =====================================================

def section_hero():

    with st.container(key="hero"):

        anchor("inicio")


        bg_video_section(
            "hero",
            height_px=460,
            fallback_text="hero",
        )


        st.markdown(
            f"""
            <div
                style="
                    position:relative;
                    padding:70px 60px 80px 60px;
                    background:var(--void);
                    color:var(--cream);
                    overflow:hidden;
                "
            >

                <div class="sunburst"></div>

                <div
                    class="halftone-block tr"
                    style="color:var(--amber);"
                ></div>


                <div
                    style="
                        position:relative;
                        z-index:2;
                    "
                >

                    <div class="kicker">
                        {SITE['nombre']}
                    </div>


                    <div
                        class="heat-display display-xl"
                        style="
                            {echo_style(
                                [
                                    'var(--amber)',
                                    'var(--ember)',
                                    'var(--crimson)'
                                ]
                            )}
                        "
                    >

                        {SITE['titulo_hero_1']}

                        <br>

                        {SITE['titulo_hero_2']}

                    </div>


                    <p
                        class="body-lg"
                        style="margin-top:26px;"
                    >
                        {SITE['tagline']}
                    </p>

                </div>

            </div>
            """,

            unsafe_allow_html=True,
        )


# =====================================================
# SECCIÓN SOBRE MÍ
# =====================================================

def section_about():

    with st.container(key="about"):

        anchor("sobre-mi")


        col1, col2 = st.columns(
            [1.1, 1],
            gap="large",
        )


        with col1:

            st.markdown(
                f"""
                <div
                    class="heat-display display-lg"
                    style="
                        {echo_style(
                            [
                                'var(--void)',
                                'var(--amber)'
                            ]
                        )}
                    "
                >
                    {ABOUT['titulo']}
                </div>
                """,

                unsafe_allow_html=True,
            )


            # Usamos st.markdown directamente
            # para que los **negritas** funcionen correctamente.

            st.markdown(
                ABOUT["texto"]
            )


        with col2:

            show_media(
                ABOUT["imagen"],
                "tu foto de perfil",
            )


# =====================================================
# SECCIÓN HERRAMIENTAS
# =====================================================

def section_tools():

    with st.container(key="tools"):

        anchor("herramientas")


        st.markdown(
            f"""
            <div
                class="heat-display display-lg"
                style="
                    {echo_style(
                        [
                            "var(--crimson)",
                            "var(--plum)"
                        ]
                    )}
                "
            >
                HERRAMIENTAS
            </div>
            """,

            unsafe_allow_html=True,
        )


        chips = []


        for tool in TOOLS:

            logo_path = (
                ASSETS
                / "tools"
                / tool["archivo"]
            )


            if logo_path.exists():

                encoded_logo = base64.b64encode(
                    logo_path.read_bytes()
                ).decode()


                icon_html = (
                    f'<img '
                    f'src="data:image/png;base64,{encoded_logo}" '
                    f'style="height:22px;">'
                )


            else:

                icon_html = "◆"


            chips.append(
                f"""
                <span class="tool-chip">
                    {icon_html}
                    {tool["nombre"]}
                </span>
                """
            )


        st.markdown(
            f"""
            <div style="margin-top:30px;">
                {"".join(chips)}
            </div>
            """,

            unsafe_allow_html=True,
        )


# =====================================================
# GRID DE PROYECTOS
# =====================================================

def project_grid(
    items,
    columns=2,
):

    cols = st.columns(
        columns,
        gap="large",
    )


    for idx, item in enumerate(items):

        with cols[idx % columns]:

            with st.container(
                key=f"card-{slugify(item['titulo'])}-{idx}"
            ):

                label = (
                    f"N°{idx + 1:02d}"
                    f"  ·  "
                    f"{item['titulo']}"
                )


                with st.expander(
                    label,
                    expanded=False,
                ):

                    # =================================================
                    # SI TIENE GALERÍA → CARRUSEL
                    # SI NO → MEDIA NORMAL
                    # =================================================

                    galeria = item.get(
                        "galeria",
                        [],
                    )


                    if galeria:

                        show_carousel(
                            galeria,

                            item["titulo"],

                            key=(
                                f"{slugify(item['titulo'])}"
                                f"-{idx}"
                            ),
                        )


                    elif item.get("archivo"):

                        show_media(
                            item["archivo"],
                            item["titulo"],
                        )


                    # =================================================
                    # INFORMACIÓN
                    # =================================================

                    st.markdown(
                        f"**{item['resumen']}**"
                    )


                    meta = []


                    if item.get("rol"):

                        meta.append(
                            f"**Rol:** {item['rol']}"
                        )


                    if item.get("herramientas"):

                        meta.append(
                            f"**Herramientas:** "
                            f"{item['herramientas']}"
                        )


                    if meta:

                        st.markdown(
                            " &nbsp;|&nbsp; ".join(meta)
                        )


                    if item.get("resultado"):

                        st.markdown(
                            item["resultado"]
                        )


                    if item.get("enlace"):

                        st.markdown(
                            f"""
                            [Ver proyecto ↗](
                                {item['enlace']}
                            )
                            """
                        )


# =====================================================
# SECCIÓN INMERSIVOS
# =====================================================

def section_immersive():

    with st.container(key="immersive"):

        anchor("inmersivos")


        st.markdown(
            f"""
            <div
                class="heat-display display-lg"
                style="
                    {echo_style(
                        [
                            "var(--ember)",
                            "var(--amber)"
                        ]
                    )}
                "
            >
                INMERSIVOS
            </div>
            """,

            unsafe_allow_html=True,
        )


        st.markdown(
            """
            <p
                class="body-md"
                style="margin:20px 0 44px 0;"
            >
                Proyectos que combinan diseño,
                tecnología y narrativa para crear
                experiencias que se recorren,
                no solo se miran.
            </p>
            """,

            unsafe_allow_html=True,
        )


        project_grid(
            INMERSIVOS
        )


# =====================================================
# DIVIDER
# =====================================================

def section_divider():

    with st.container(key="divider"):

        bg_video_section(
            "divider",
            height_px=200,
            fallback_text="divider",
        )


# =====================================================
# SECCIÓN INTERFACES
# =====================================================

def section_interfaces():

    with st.container(key="interfaces"):

        anchor("interfaces")


        st.markdown(
            f"""
            <div
                class="heat-display display-lg"
                style="
                    {echo_style(
                        [
                            "var(--crimson)",
                            "var(--amber)"
                        ]
                    )}
                "
            >
                INTERFACES
            </div>
            """,

            unsafe_allow_html=True,
        )


        st.markdown(
            "<div style='height:34px;'></div>",
            unsafe_allow_html=True,
        )


        project_grid(
            INTERFACES
        )


# =====================================================
# SECCIÓN VISUAL
# =====================================================

def section_visual():

    with st.container(key="visual"):

        anchor("visual")


        st.markdown(
            f"""
            <div
                class="heat-display display-lg"
                style="
                    {echo_style(
                        [
                            "var(--plum)",
                            "var(--crimson)"
                        ]
                    )}
                "
            >
                VISUAL
            </div>
            """,

            unsafe_allow_html=True,
        )


        st.markdown(
            "<div style='height:34px;'></div>",
            unsafe_allow_html=True,
        )


        # Visual usa 3 columnas
        # y cada proyecto puede tener su propio carrusel.

        project_grid(
            VISUAL,
            columns=3,
        )


# =====================================================
# SECCIÓN INVESTIGACIÓN
# =====================================================

def section_research():

    with st.container(key="research"):

        anchor("investigacion")


        st.markdown(
            f"""
            <div
                class="heat-display display-lg"
                style="
                    {echo_style(
                        [
                            "var(--crimson)",
                            "var(--plum)"
                        ]
                    )}
                "
            >
                INVESTIGACIÓN
            </div>
            """,

            unsafe_allow_html=True,
        )


        st.markdown(
            "<div style='height:34px;'></div>",
            unsafe_allow_html=True,
        )


        project_grid(
            INVESTIGACION
        )


# =====================================================
# SECCIÓN CONTACTO
# =====================================================

def section_contact():

    with st.container(key="contact"):

        anchor("contacto")


        bg_video_section(
            "footer",
            height_px=380,
            fallback_text="footer",
        )


        links_html = "".join(
            f"""
            <a
                class="cta-btn"
                href="{link['url']}"
                target="_blank"
            >
                {link['nombre']}
            </a>
            """

            for link in CONTACT["links"]
        )


        st.markdown(
            f"""
            <div
                style="
                    position:relative;
                    padding:60px 60px 80px 60px;
                    background:var(--void);
                    color:var(--cream);
                    overflow:hidden;
                "
            >

                <div
                    class="halftone-block bl"
                    style="color:var(--amber);"
                ></div>


                <div
                    style="
                        position:relative;
                        z-index:2;
                    "
                >

                    <div
                        class="heat-display display-xl"
                        style="
                            {echo_style(
                                [
                                    'var(--amber)',
                                    'var(--ember)',
                                    'var(--crimson)'
                                ]
                            )}
                        "
                    >

                        {CONTACT['titulo_1']}

                        <br>

                        {CONTACT['titulo_2']}

                    </div>


                    <p
                        class="body-lg"
                        style="
                            margin:24px 0 28px 0;
                        "
                    >
                        {CONTACT['texto']}
                    </p>


                    <a
                        class="cta-btn"
                        href="mailto:{CONTACT['email']}"
                    >
                        ✉ {CONTACT['email']}
                    </a>


                    {links_html}

                </div>

            </div>
            """,

            unsafe_allow_html=True,
        )


# =====================================================
# RENDER
# =====================================================

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
