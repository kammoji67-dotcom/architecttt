import streamlit as st
import json
import pandas as pd

st.set_page_config(
    page_title="ArchSketch Atlas",
    page_icon="🏛",
    layout="wide"
)

SKETCHES = [
    {
        "id": "AS-0001", "type": "arch",
        "title": "Milan Duomo - Gothic Cathedral",
        "subtitle": "Pencil technical illustration with architectural annotations",
        "location": "Milan, Italy", "lat": 45.4642, "lon": 9.1900,
        "style": "Gothic Revival", "technique": "Pencil + Ink Wash", "period": "14th Century",
        "tags": ["cathedral", "gothic", "spires", "dome", "ornamental"],
        "image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500&q=80"
    },
    {
        "id": "AS-0002", "type": "arch",
        "title": "Fantasy Castle - Medieval Fortress",
        "subtitle": "Pen sketch of a fairytale castle with arched bridge and towers",
        "location": "Loire Valley, France", "lat": 47.6609, "lon": 0.8799,
        "style": "Romanesque / Fantasy", "technique": "Fine Liner Pen", "period": "12th Century Inspired",
        "tags": ["castle", "medieval", "towers", "bridge", "fantasy"],
        "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&q=80"
    },
    {
        "id": "AS-0003", "type": "scene",
        "title": "Garden Waterfall - Natural Scene",
        "subtitle": "Graphite landscape study with cascading water and stepping stones",
        "location": "Kyoto, Japan", "lat": 35.0116, "lon": 135.7681,
        "style": "Naturalistic Landscape", "technique": "Graphite Pencil", "period": "Contemporary",
        "tags": ["waterfall", "garden", "rocks", "nature", "reflection"],
        "image": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=500&q=80"
    },
    {
        "id": "AS-0004", "type": "interior",
        "title": "Grand Hall - Interior Perspective",
        "subtitle": "Ballpoint pen one-point perspective of a palatial neoclassical interior",
        "location": "St. Petersburg, Russia", "lat": 59.9311, "lon": 30.3609,
        "style": "Neoclassical", "technique": "Ballpoint Pen", "period": "18th Century",
        "tags": ["interior", "columns", "stairs", "perspective", "ballpoint"],
        "image": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=500&q=80"
    },
    {
        "id": "AS-0005", "type": "urban",
        "title": "Puddle Reflection - Urban Building",
        "subtitle": "Surreal pencil drawing of a Victorian building mirrored in a rain puddle",
        "location": "London, UK", "lat": 51.5074, "lon": -0.1278,
        "style": "Surrealism / Urban", "technique": "Pencil Hatching", "period": "Contemporary",
        "tags": ["reflection", "puddle", "building", "surreal", "urban"],
        "image": "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=500&q=80"
    },
    {
        "id": "AS-0006", "type": "urban",
        "title": "Underground Station - Metro Platform",
        "subtitle": "Charcoal drawing of a vaulted metro station with atmospheric lighting",
        "location": "Paris, France", "lat": 48.8566, "lon": 2.3522,
        "style": "Industrial / Atmospheric", "technique": "Charcoal", "period": "Contemporary",
        "tags": ["metro", "tunnel", "train", "atmosphere", "arches"],
        "image": "https://images.unsplash.com/photo-1569960193803-0d7eb58f5b8e?w=500&q=80"
    },
    {
        "id": "AS-0007", "type": "urban",
        "title": "Old Town Alley - Cobblestone Street",
        "subtitle": "Pencil sketch of a narrow Mediterranean alleyway with worn steps",
        "location": "Dubrovnik, Croatia", "lat": 42.6507, "lon": 18.0944,
        "style": "Mediterranean Urban", "technique": "Pencil Sketch", "period": "17th Century Context",
        "tags": ["alley", "cobblestone", "steps", "arch", "mediterranean"],
        "image": "https://images.unsplash.com/photo-1467803738586-46b7eb7b16a1?w=500&q=80"
    },
    {
        "id": "AS-0008", "type": "urban",
        "title": "Lisbon Tram - Street Reflection",
        "subtitle": "Graphite study of a vintage tram with a dramatic wet-street reflection",
        "location": "Lisbon, Portugal", "lat": 38.7169, "lon": -9.1395,
        "style": "Urban Realism", "technique": "Graphite + Ink", "period": "Contemporary",
        "tags": ["tram", "street", "reflection", "lisbon", "vintage"],
        "image": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?w=500&q=80"
    },
    {
        "id": "AS-0009", "type": "3d",
        "title": "Chess King - 3D Object Study",
        "subtitle": "Detailed charcoal drawing of a chess king piece - an exercise in form and shadow",
        "location": "Study Exercise", "lat": 0.0, "lon": 0.0,
        "style": "Object Study / 3D", "technique": "Charcoal + Blending", "period": "Contemporary",
        "tags": ["chess", "3d", "object", "shading", "form"],
        "image": "https://images.unsplash.com/photo-1529699211952-734e80c4d42b?w=500&q=80"
    }
]

TYPE_LABELS = {
    "arch": "Architecture",
    "scene": "Landscape",
    "urban": "Urban",
    "interior": "Interior",
    "3d": "3D Object"
}

# ── Sidebar ──────────────────────────────────────────────────────────────────
st.sidebar.title("ArchSketch Atlas")
st.sidebar.markdown("A sketch library with real-world coordinates for beginner architects.")
st.sidebar.markdown("---")

page = st.sidebar.radio("Navigate", ["Gallery", "Map View", "Streamlit Guide", "GitHub Setup"])

st.sidebar.markdown("---")
st.sidebar.markdown("**Filter Sketches**")

type_options = ["All"] + sorted(set(TYPE_LABELS[s["type"]] for s in SKETCHES))
selected_type = st.sidebar.selectbox("Category", type_options)

search_query = st.sidebar.text_input("Search", placeholder="style, location, technique...")

# ── Filter data ───────────────────────────────────────────────────────────────
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
            or any(q in tag for tag in s["tags"])
        ]
    return result

filtered = filter_sketches(SKETCHES, selected_type, search_query)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: GALLERY
# ══════════════════════════════════════════════════════════════════════════════
if page == "Gallery":
    st.title("Sketch Gallery")
    st.markdown(f"Showing **{len(filtered)}** sketch{'es' if len(filtered) != 1 else ''}")
    st.markdown("---")

    if not filtered:
        st.info("No sketches match your search. Try clearing the filters.")
    else:
        cols = st.columns(3)
        for i, sketch in enumerate(filtered):
            with cols[i % 3]:
                st.image(sketch["image"], use_container_width=True)
                st.markdown(f"**{sketch['title']}**")
                st.caption(f"{TYPE_LABELS[sketch['type']]} | {sketch['style']}")
                st.caption(f"Technique: {sketch['technique']}")
                st.caption(f"📍 {sketch['location']}")
                st.code(f"lat: {sketch['lat']:.4f}  lon: {sketch['lon']:.4f}", language=None)

                with st.expander("Full coordinate data"):
                    payload = {
                        "dataset_id": sketch["id"],
                        "title": sketch["title"],
                        "lat": sketch["lat"],
                        "lon": sketch["lon"],
                        "location": sketch["location"],
                        "style": sketch["style"],
                        "technique": sketch["technique"],
                        "period": sketch["period"],
                        "type": sketch["type"],
                        "tags": sketch["tags"],
                        "image_url": sketch["image"]
                    }
                    st.json(payload)
                st.markdown("---")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: MAP VIEW
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Map View":
    st.title("Map View")
    st.markdown("Geographic locations of all sketches in the library. Each pin represents a real building or site.")
    st.markdown("---")

    map_data = [s for s in filtered if not (s["lat"] == 0.0 and s["lon"] == 0.0)]

    if not map_data:
        st.warning("No mappable locations in your current filter selection.")
    else:
        df = pd.DataFrame([{"lat": s["lat"], "lon": s["lon"], "title": s["title"]} for s in map_data])
        st.map(df[["lat", "lon"]])
        st.markdown("---")
        st.subheader("Location Reference")
        for s in map_data:
            col1, col2, col3 = st.columns([2, 1, 1])
            col1.markdown(f"**{s['title']}**  \n{s['location']}")
            col2.markdown(f"`{s['lat']:.4f}° N`")
            col3.markdown(f"`{s['lon']:.4f}° E`")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: STREAMLIT GUIDE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Streamlit Guide":
    st.title("Build with Streamlit")
    st.markdown("Follow these steps to build your own architectural sketch explorer. No web experience needed.")
    st.markdown("---")

    st.subheader("Step 1 - Install Streamlit")
    st.code("""# Open your terminal and run:
mkdir archsketch-app
cd archsketch-app
pip install streamlit pandas pillow requests

# Verify installation:
streamlit hello""", language="bash")

    st.subheader("Step 2 - Create app.py")
    st.markdown("Create a file called `app.py` in your project folder:")
    st.code("""import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="ArchSketch Atlas", page_icon="🏛", layout="wide")
st.title("🏛 ArchSketch Atlas")

# Load your JSON dataset
with open("sketches.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Sidebar filter
style = st.sidebar.selectbox("Filter by style", ["All"] + df["style"].unique().tolist())
if style != "All":
    df = df[df["style"] == style]

# Map view
st.subheader("Locations on Map")
st.map(df[["lat", "lon"]])

# Gallery grid
st.subheader("Sketch Gallery")
cols = st.columns(3)
for i, row in df.iterrows():
    with cols[i % 3]:
        st.image(row["image_url"], caption=row["title"], use_container_width=True)
        st.code(f"lat: {row['lat']:.4f}  lon: {row['lon']:.4f}", language=None)
        st.caption(row["style"] + " | " + row["technique"])""", language="python")

    st.subheader("Step 3 - Save your sketch data")
    st.markdown("Create `sketches.json` by expanding any sketch card in the Gallery tab and copying the JSON.")
    st.code("""# sketches.json structure:
[
  {
    "dataset_id": "AS-0001",
    "title": "Milan Duomo - Gothic Cathedral",
    "lat": 45.4642,
    "lon": 9.1900,
    "location": "Milan, Italy",
    "style": "Gothic Revival",
    "technique": "Pencil + Ink Wash",
    "period": "14th Century",
    "type": "arch",
    "tags": ["cathedral", "gothic", "spires"],
    "image_url": "https://..."
  }
]""", language="json")

    st.subheader("Step 4 - Run your app")
    st.code("streamlit run app.py", language="bash")
    st.success("Your app opens automatically at http://localhost:8501")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: GITHUB SETUP
# ══════════════════════════════════════════════════════════════════════════════
elif page == "GitHub Setup":
    st.title("Deploy on GitHub")
    st.markdown("Push your Streamlit app to GitHub and deploy it live for free in under 10 minutes.")
    st.markdown("---")

    st.subheader("Step 1 - Initialize Git")
    st.code("""git init
git add .
git commit -m "Initial commit: ArchSketch Atlas app" """, language="bash")

    st.subheader("Step 2 - Create requirements.txt")
    st.markdown("Save this as `requirements.txt` in your project root:")
    st.code("""streamlit==1.32.0
pandas==2.1.0
pillow==10.0.0
requests==2.31.0""", language="text")

    st.subheader("Step 3 - Push to GitHub")
    st.code("""# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/archsketch-atlas.git
git branch -M main
git push -u origin main""", language="bash")

    st.subheader("Step 4 - Deploy on Streamlit Cloud")
    st.markdown("""
1. Go to **share.streamlit.io**
2. Sign in with your GitHub account
3. Click **New app**
4. Select your repository and set the main file to `wesketch.py`
5. Click **Deploy**

Your app will be live at:
""")
    st.code("https://YOUR_USERNAME-archsketch-atlas-app-XXXX.streamlit.app", language="text")

    st.subheader("Recommended Folder Structure")
    st.code("""archsketch-atlas/
  |-- wesketch.py        # your main Streamlit app
  |-- requirements.txt   # dependencies
  |-- sketches.json      # coordinate data
  └── README.md          # project description""", language="text")

    st.subheader("README Template")
    st.code("""# ArchSketch Atlas

An interactive explorer of architectural sketches with real-world
geo-coordinates. Built with Streamlit and Python.

## Features
- Map view of sketch locations worldwide
- Gallery with style and technique filters
- JSON coordinate data for each sketch
- Search by style, location, or technique

## Run Locally
    pip install -r requirements.txt
    streamlit run wesketch.py

## Deploy
Visit share.streamlit.io and connect your GitHub repo.""", language="markdown")
