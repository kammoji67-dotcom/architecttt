
    import streamlit as st

st.set_page_config(
    page_title="ArchSketch Atlas",
    page_icon="🏛",
    layout="wide"
)

import base64
from pathlib import Path

# ── Load images from local files ──────────────────────────────────────────────
def img_to_base64(path):
    with open(path, "rb") as f:
        ext = Path(path).suffix.lower().replace(".", "")
        mime = "jpeg" if ext == "jpg" else ext
        return f"data:image/{mime};base64,{base64.b64encode(f.read()).decode()}"

SKETCHES = [
    {
        "id": "AS-0001",
        "title": "Milan Duomo - Gothic Cathedral",
        "type": "arch",
        "style": "Gothic Revival",
        "technique": "Pencil + Ink Wash",
        "location": "Milan, Italy",
        "file": "download__1_.webp"
    },
    {
        "id": "AS-0002",
        "title": "Fantasy Castle - Medieval Fortress",
        "type": "arch",
        "style": "Romanesque / Fantasy",
        "technique": "Fine Liner Pen",
        "location": "Loire Valley, France",
        "file": "8dbc040517627df2c231b1960a11ea9d.jpg"
    },
    {
        "id": "AS-0003",
        "title": "Garden Waterfall - Natural Scene",
        "type": "scene",
        "style": "Naturalistic Landscape",
        "technique": "Graphite Pencil",
        "location": "Kyoto, Japan",
        "file": "9f8bb1bb3eab80672f50a9fe7d808d6f.jpg"
    },
    {
        "id": "AS-0004",
        "title": "Grand Hall - Interior Perspective",
        "type": "interior",
        "style": "Neoclassical",
        "technique": "Ballpoint Pen",
        "location": "St. Petersburg, Russia",
        "file": "44a492f4a756219233f5d44513dce581.jpg"
    },
    {
        "id": "AS-0005",
        "title": "Puddle Reflection - Urban Building",
        "type": "urban",
        "style": "Surrealism / Urban",
        "technique": "Pencil Hatching",
        "location": "London, UK",
        "file": "13e6ba8b4488499b447f514839f5b6cd.jpg"
    },
    {
        "id": "AS-0006",
        "title": "Underground Station - Metro Platform",
        "type": "urban",
        "style": "Industrial / Atmospheric",
        "technique": "Charcoal",
        "location": "Paris, France",
        "file": "556b93371196faa770e3897d82d10df0.jpg"
    },
    {
        "id": "AS-0007",
        "title": "Old Town Alley - Cobblestone Street",
        "type": "urban",
        "style": "Mediterranean Urban",
        "technique": "Pencil Sketch",
        "location": "Dubrovnik, Croatia",
        "file": "292b02037f648f6c696718a4366a1739.webp"
    },
    {
        "id": "AS-0008",
        "title": "Lisbon Tram - Street Reflection",
        "type": "urban",
        "style": "Urban Realism",
        "technique": "Graphite + Ink",
        "location": "Lisbon, Portugal",
        "file": "df7589de976634ae0a97952fab719619.jpg"
    },
    {
        "id": "AS-0009",
        "title": "Chess King - 3D Object Study",
        "type": "3d",
        "style": "Object Study / 3D",
        "technique": "Charcoal + Blending",
        "location": "Study Exercise",
        "file": "e867ecffda0b09b5f24ddcd8dd89d59b.webp"
    }
]

TYPE_LABELS = {
    "arch": "Architecture",
    "scene": "Landscape",
    "urban": "Urban",
    "interior": "Interior",
    "3d": "3D Object"
}

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.title("ArchSketch Atlas")
st.sidebar.markdown("A sketch library for beginner architects.")
st.sidebar.markdown("---")

page = st.sidebar.radio("Navigate", ["Gallery", "Streamlit Guide", "GitHub Setup"])

st.sidebar.markdown("---")
st.sidebar.markdown("**Filter**")

type_options = ["All", "Architecture", "Landscape", "Urban", "Interior", "3D Object"]
selected_type = st.sidebar.selectbox("Category", type_options)
search_query = st.sidebar.text_input("Search", placeholder="style, location, technique...")

# ── Filter ────────────────────────────────────────────────────────────────────
def filter_sketches(sketches, type_filter, query):
    result = sketches
    if type_filter != "All":
        result = [s for s in result if TYPE_LABELS[s["type"]] == type_filter]
    if query:
        q = query.lower()
        result = [
            s for s in result
            if q in s["title"].lower()
            or q in s["style"].lower()
            or q in s["location"].lower()
            or q in s["technique"].lower()
        ]
    return result

filtered = filter_sketches(SKETCHES, selected_type, search_query)

# ══════════════════════════════════════════════════════════════════════════════
# GALLERY
# ══════════════════════════════════════════════════════════════════════════════
if page == "Gallery":
    st.title("Sketch Gallery")
    st.markdown(f"Showing **{len(filtered)}** sketch{'es' if len(filtered) != 1 else ''}")
    st.markdown("---")

    if not filtered:
        st.info("No sketches match your filter. Try clearing the search.")
    else:
        cols = st.columns(3)
        for i, sketch in enumerate(filtered):
            with cols[i % 3]:
                # Load image directly from file sitting next to wesketch.py
                st.image(sketch["file"], use_container_width=True)
                st.markdown(f"**{sketch['title']}**")
                st.caption(f"{TYPE_LABELS[sketch['type']]}  |  {sketch['style']}")
                st.caption(f"Technique: {sketch['technique']}")
                st.caption(f"📍 {sketch['location']}")
                st.markdown("")

# ══════════════════════════════════════════════════════════════════════════════
# STREAMLIT GUIDE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Streamlit Guide":
    st.title("Build with Streamlit")
    st.markdown("Follow these steps to create your own architectural sketch app.")
    st.markdown("---")

    st.subheader("Step 1 - Install Streamlit")
    st.code("""mkdir archsketch-app
cd archsketch-app
pip install streamlit
streamlit hello""", language="bash")

    st.subheader("Step 2 - Create app.py")
    st.code("""import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Sketch App", layout="wide")
st.title("My Architecture Sketches")

img = Image.open("sketch1.jpg")
st.image(img, caption="My first sketch", use_container_width=True)

st.markdown("**Style:** Gothic Revival")
st.markdown("**Technique:** Pencil + Ink")
st.markdown("**Location:** Milan, Italy")""", language="python")

    st.subheader("Step 3 - Grid layout")
    st.code("""import streamlit as st
from PIL import Image

sketches = [
    {"file": "sketch1.jpg", "title": "Milan Duomo",     "style": "Gothic Revival"},
    {"file": "sketch2.jpg", "title": "Garden Waterfall","style": "Naturalistic"},
    {"file": "sketch3.jpg", "title": "Lisbon Tram",     "style": "Urban Realism"},
]

cols = st.columns(3)
for i, s in enumerate(sketches):
    with cols[i % 3]:
        st.image(Image.open(s["file"]), use_container_width=True)
        st.markdown(f"**{s['title']}**")
        st.caption(s["style"])""", language="python")

    st.subheader("Step 4 - Run")
    st.code("streamlit run app.py", language="bash")
    st.success("App opens at http://localhost:8501")

# ══════════════════════════════════════════════════════════════════════════════
# GITHUB SETUP
# ══════════════════════════════════════════════════════════════════════════════
elif page == "GitHub Setup":
    st.title("Deploy on GitHub")
    st.markdown("Push your app to GitHub and deploy it free on Streamlit Cloud.")
    st.markdown("---")

    st.subheader("Step 1 - Initialize Git")
    st.code("""git init
git add .
git commit -m "first commit" """, language="bash")

    st.subheader("Step 2 - requirements.txt")
    st.code("""streamlit==1.32.0
pillow==10.0.0""", language="text")

    st.subheader("Step 3 - Push to GitHub")
    st.code("""git remote add origin https://github.com/YOUR_USERNAME/my-sketch-app.git
git branch -M main
git push -u origin main""", language="bash")

    st.subheader("Step 4 - Deploy on Streamlit Cloud")
    st.markdown("""
1. Go to **share.streamlit.io**
2. Sign in with GitHub
3. Click **New app**
4. Select your repo, set main file to `wesketch.py`
5. Click **Deploy**
""")
    st.success("Your app goes live in minutes - completely free!")

    st.subheader("Folder Structure")
    st.code("""my-sketch-app/
  |-- wesketch.py
  |-- requirements.txt
  |-- download__1_.webp
  |-- 8dbc040517627df2c231b1960a11ea9d.jpg
  |-- 9f8bb1bb3eab80672f50a9fe7d808d6f.jpg
  |-- 44a492f4a756219233f5d44513dce581.jpg
  |-- 13e6ba8b4488499b447f514839f5b6cd.jpg
  |-- 556b93371196faa770e3897d82d10df0.jpg
  |-- 292b02037f648f6c696718a4366a1739.webp
  |-- df7589de976634ae0a97952fab719619.jpg
  └── e867ecffda0b09b5f24ddcd8dd89d59b.webp""", language="text")
