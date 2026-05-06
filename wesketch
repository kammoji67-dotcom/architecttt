<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ArchSketch Atlas — Learn Architecture Through Sketches</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --ink:#1a1714;--paper:#faf8f4;--stone:#8b8278;--rust:#b85c38;
  --line:#d4cfc8;--highlight:#f0ebe3;--accent:#7c5c3e;
  --grid-paper:repeating-linear-gradient(0deg,transparent,transparent 27px,#e8e2d8 28px),
               repeating-linear-gradient(90deg,transparent,transparent 27px,#e8e2d8 28px);
}
body{font-family:'DM Sans',sans-serif;background:var(--paper);color:var(--ink);min-height:100vh}

/* NAV */
.nav{display:flex;align-items:center;justify-content:space-between;padding:16px 28px;border-bottom:1px solid var(--line);background:var(--paper);position:sticky;top:0;z-index:100}
.logo{font-family:'Playfair Display',serif;font-size:18px;letter-spacing:-0.3px}
.logo span{color:var(--rust);font-style:italic}
.nav-links{display:flex;gap:20px}
.nav-link{font-size:12px;letter-spacing:1px;text-transform:uppercase;color:var(--stone);cursor:pointer;padding:4px 0;border-bottom:1px solid transparent;transition:all 0.2s;text-decoration:none;background:none;border-top:none;border-left:none;border-right:none;font-family:'DM Sans',sans-serif}
.nav-link:hover,.nav-link.active{color:var(--ink);border-bottom-color:var(--rust)}

/* HERO */
.hero{padding:48px 28px 36px;display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:center;border-bottom:1px solid var(--line)}
.hero-text h1{font-family:'Playfair Display',serif;font-size:42px;line-height:1.1;letter-spacing:-1px;margin-bottom:16px}
.hero-text h1 em{color:var(--rust);font-style:italic}
.hero-text p{font-size:14px;color:var(--stone);line-height:1.7;max-width:400px;margin-bottom:24px}
.hero-badges{display:flex;gap:8px;flex-wrap:wrap}
.badge{font-family:'DM Mono',monospace;font-size:10px;padding:4px 10px;border:1px solid var(--line);border-radius:2px;color:var(--stone);background:var(--highlight)}
.badge.active{background:var(--rust);color:#fff;border-color:var(--rust)}
.hero-coords{background:var(--grid-paper);border:1px solid var(--line);border-radius:4px;padding:20px;font-family:'DM Mono',monospace;font-size:12px}
.coord-title{font-size:10px;letter-spacing:2px;text-transform:uppercase;color:var(--stone);margin-bottom:12px}
.coord-row{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px dashed var(--line);color:var(--ink)}
.coord-row:last-of-type{border:none}
.coord-val{color:var(--rust)}

/* TABS */
.tabs{display:flex;border-bottom:1px solid var(--line);padding:0 28px;background:var(--paper);overflow-x:auto}
.tab{font-size:12px;letter-spacing:0.5px;padding:14px 0;margin-right:28px;cursor:pointer;border-bottom:2px solid transparent;color:var(--stone);transition:all 0.2s;white-space:nowrap;background:none;border-top:none;border-left:none;border-right:none;font-family:'DM Sans',sans-serif}
.tab:hover{color:var(--ink)}
.tab.active{color:var(--ink);border-bottom-color:var(--rust)}

/* SECTIONS */
.section{padding:28px;display:none}
.section.active{display:block}

/* GALLERY */
.gallery-controls{display:flex;gap:8px;margin-bottom:20px;flex-wrap:wrap}
.filter-btn{font-size:11px;padding:5px 12px;border:1px solid var(--line);border-radius:2px;background:transparent;cursor:pointer;color:var(--stone);font-family:'DM Sans',sans-serif;transition:all 0.15s}
.filter-btn:hover,.filter-btn.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px}
.card{border:1px solid var(--line);border-radius:3px;overflow:hidden;cursor:pointer;transition:all 0.2s;background:var(--paper)}
.card:hover{border-color:var(--rust);transform:translateY(-2px)}
.card-img{width:100%;height:185px;object-fit:cover;display:block;filter:grayscale(10%)}
.card-info{padding:10px 12px}
.card-title{font-size:12px;font-weight:500;margin-bottom:4px}
.card-meta{font-family:'DM Mono',monospace;font-size:10px;color:var(--stone);line-height:1.6}
.card-type{display:inline-block;font-size:9px;padding:2px 7px;border-radius:2px;margin-bottom:6px;letter-spacing:0.5px;font-weight:500}
.t-arch{background:#f0e8df;color:#7c5c3e}
.t-scene{background:#e8f0e8;color:#3e5c3e}
.t-urban{background:#e8ecf0;color:#3e4e5c}
.t-interior{background:#f0e8f0;color:#5c3e5c}
.t-3d{background:#f0f0e0;color:#5c5c2e}

/* MODAL */
.modal-bg{display:none;position:fixed;inset:0;background:rgba(26,23,20,0.85);z-index:200;align-items:center;justify-content:center;padding:16px}
.modal-bg.open{display:flex}
.modal{background:var(--paper);border-radius:4px;max-width:780px;width:100%;max-height:90vh;overflow-y:auto;display:grid;grid-template-columns:1fr 1fr;position:relative}
.modal-img-wrap{background:#1a1714;display:flex;align-items:center;justify-content:center;min-height:320px;border-radius:4px 0 0 4px;overflow:hidden}
.modal-img{width:100%;height:100%;object-fit:contain;max-height:520px}
.modal-detail{padding:28px 24px;overflow-y:auto}
.modal-type-label{font-size:9px;letter-spacing:2px;text-transform:uppercase;color:var(--rust);margin-bottom:8px}
.modal-title{font-family:'Playfair Display',serif;font-size:22px;margin-bottom:4px;line-height:1.2}
.modal-subtitle{font-size:13px;color:var(--stone);margin-bottom:20px;line-height:1.5}
.coord-block{background:var(--grid-paper);border:1px solid var(--line);border-radius:3px;padding:14px;margin-bottom:16px}
.cb-label{font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--stone);margin-bottom:8px}
.cb-row{display:flex;justify-content:space-between;font-family:'DM Mono',monospace;font-size:11px;padding:5px 0;border-bottom:1px dashed var(--line)}
.cb-row:last-child{border:none}
.cb-key{color:var(--stone)}
.cb-val{color:var(--rust);font-weight:500}
.tags-list{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:16px}
.tag{font-size:10px;padding:3px 8px;border:1px solid var(--line);border-radius:2px;color:var(--stone)}
.copy-btn{font-family:'DM Mono',monospace;font-size:11px;padding:9px 14px;background:var(--ink);color:#fff;border:none;border-radius:2px;cursor:pointer;width:100%;margin-bottom:8px;transition:all 0.2s;letter-spacing:0.3px}
.copy-btn:hover{opacity:0.75}
.copy-btn.alt{background:var(--highlight);color:var(--ink);border:1px solid var(--line)}
.copy-btn.alt:hover{background:var(--line)}
.copy-btn.success{background:#3e6e3e}
.close-btn{position:absolute;top:12px;right:14px;font-size:24px;cursor:pointer;color:var(--stone);background:none;border:none;z-index:10;line-height:1}
.close-btn:hover{color:var(--ink)}

/* GUIDE / STEPS */
.guide-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:28px}
.guide-card{border:1px solid var(--line);border-radius:3px;padding:20px}
.guide-num{font-family:'Playfair Display',serif;font-size:40px;color:var(--line);margin-bottom:8px;line-height:1}
.guide-title{font-size:14px;font-weight:500;margin-bottom:6px}
.guide-desc{font-size:12px;color:var(--stone);line-height:1.7}
.code-block{background:#1e1b18;color:#c8c0b4;font-family:'DM Mono',monospace;font-size:12px;padding:16px 18px;border-radius:3px;margin:10px 0 22px;line-height:1.7;white-space:pre;overflow-x:auto;border:1px solid #2e2b28}
.kw{color:#e8a07a}.str{color:#90c09a}.cm{color:#6a6058}.fn{color:#7ab0d8}
.section-title{font-family:'Playfair Display',serif;font-size:28px;margin-bottom:8px}
.section-sub{font-size:13px;color:var(--stone);margin-bottom:24px;line-height:1.7;max-width:600px}
.step-label{font-size:10px;letter-spacing:2px;text-transform:uppercase;color:var(--rust);margin-bottom:4px}
.step-title{font-size:16px;font-weight:500;margin-bottom:8px}
.step-body{font-size:13px;color:var(--stone);line-height:1.7;margin-bottom:4px}

/* SEARCH */
.search-bar{display:flex;gap:10px;margin-bottom:20px}
.search-input{flex:1;padding:9px 14px;border:1px solid var(--line);border-radius:2px;font-family:'DM Sans',sans-serif;font-size:13px;background:var(--paper);color:var(--ink);outline:none}
.search-input:focus{border-color:var(--rust)}
.search-btn{padding:9px 20px;background:var(--rust);color:#fff;border:none;border-radius:2px;font-size:12px;cursor:pointer;font-family:'DM Sans',sans-serif;letter-spacing:0.5px}
.search-btn:hover{background:var(--accent)}

/* ABOUT */
.about-grid{display:grid;grid-template-columns:1.2fr 1fr;gap:32px;align-items:start}
.about-text p{font-size:14px;color:var(--stone);line-height:1.8;margin-bottom:16px}
.about-text h3{font-family:'Playfair Display',serif;font-size:18px;margin:20px 0 8px;color:var(--ink)}
.stat-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px}
.stat-card{border:1px solid var(--line);border-radius:3px;padding:16px;text-align:center}
.stat-num{font-family:'Playfair Display',serif;font-size:32px;color:var(--rust);display:block}
.stat-label{font-size:11px;color:var(--stone);letter-spacing:0.5px}
.empty-state{text-align:center;padding:48px;color:var(--stone);grid-column:1/-1}
.empty-state span{font-size:32px;display:block;margin-bottom:8px}

/* RESPONSIVE */
@media(max-width:640px){
  .hero{grid-template-columns:1fr}
  .hero-text h1{font-size:30px}
  .guide-grid{grid-template-columns:1fr}
  .modal{grid-template-columns:1fr}
  .modal-img-wrap{min-height:220px;border-radius:4px 4px 0 0}
  .about-grid{grid-template-columns:1fr}
  .nav-links{gap:12px}
}
</style>
</head>
<body>

<!-- NAV -->
<nav class="nav">
  <div class="logo">Arch<span>Sketch</span> Atlas</div>
  <div class="nav-links">
    <button class="nav-link active" onclick="switchSection('gallery')">Gallery</button>
    <button class="nav-link" onclick="switchSection('guide')">Streamlit</button>
    <button class="nav-link" onclick="switchSection('github')">GitHub</button>
    <button class="nav-link" onclick="switchSection('about')">About</button>
  </div>
</nav>

<!-- HERO -->
<div class="hero">
  <div class="hero-text">
    <h1>Study Architecture<br>Through <em>Sketches</em></h1>
    <p>A curated library of architectural drawings — each tagged with real-world coordinates, style, and technique. Perfect for beginners building their Streamlit portfolio on GitHub.</p>
    <div class="hero-badges">
      <span class="badge active">Streamlit Ready</span>
      <span class="badge active">GitHub Friendly</span>
      <span class="badge">9 Sketch Types</span>
      <span class="badge">Lat / Lng Tagged</span>
    </div>
  </div>
  <div class="hero-coords">
    <div class="coord-title">// Sample Coordinate Entry</div>
    <div class="coord-row"><span>latitude</span><span class="coord-val">45.4642° N</span></div>
    <div class="coord-row"><span>longitude</span><span class="coord-val">9.1900° E</span></div>
    <div class="coord-row"><span>location</span><span class="coord-val">Milan Duomo, Italy</span></div>
    <div class="coord-row"><span>style</span><span class="coord-val">Gothic Revival</span></div>
    <div class="coord-row"><span>technique</span><span class="coord-val">Pencil + Ink</span></div>
    <div class="coord-row"><span>dataset_id</span><span class="coord-val">AS-0001</span></div>
    <div style="margin-top:10px;font-size:10px;color:var(--stone);font-family:'DM Mono',monospace">// click any card to copy JSON for Streamlit</div>
  </div>
</div>

<!-- TABS -->
<div class="tabs">
  <button class="tab active" onclick="switchSection('gallery')">Sketch Gallery</button>
  <button class="tab" onclick="switchSection('guide')">Streamlit Guide</button>
  <button class="tab" onclick="switchSection('github')">GitHub Setup</button>
  <button class="tab" onclick="switchSection('about')">About</button>
</div>

<!-- ===== GALLERY ===== -->
<div id="section-gallery" class="section active">
  <div class="search-bar">
    <input class="search-input" id="searchInput" type="text" placeholder="Search by title, style, location, technique..." oninput="filterCards()">
    <button class="search-btn" onclick="filterCards()">Search</button>
  </div>
  <div class="gallery-controls">
    <button class="filter-btn on" onclick="setFilter('all',this)">All</button>
    <button class="filter-btn" onclick="setFilter('arch',this)">Architecture</button>
    <button class="filter-btn" onclick="setFilter('scene',this)">Landscapes</button>
    <button class="filter-btn" onclick="setFilter('urban',this)">Urban</button>
    <button class="filter-btn" onclick="setFilter('interior',this)">Interior</button>
    <button class="filter-btn" onclick="setFilter('3d',this)">3D Object</button>
  </div>
  <div class="gallery" id="gallery"></div>
</div>

<!-- ===== STREAMLIT GUIDE ===== -->
<div id="section-guide" class="section">
  <div class="section-title">Build with Streamlit</div>
  <div class="section-sub">Create your own interactive architectural sketch explorer. Follow these steps — no prior web experience needed. Just Python and curiosity.</div>

  <div class="guide-grid">
    <div class="guide-card"><div class="guide-num">01</div><div class="guide-title">Install Streamlit</div><div class="guide-desc">Install via pip in your terminal. Works on Windows, Mac, and Linux. Python 3.8+ required.</div></div>
    <div class="guide-card"><div class="guide-num">02</div><div class="guide-title">Create your app file</div><div class="guide-desc">One Python file is all you need. Streamlit turns Python scripts into interactive web apps instantly.</div></div>
    <div class="guide-card"><div class="guide-num">03</div><div class="guide-title">Add sketch data</div><div class="guide-desc">Use JSON or CSV with lat/lng columns. Copy the coordinate JSON from each sketch card on this site.</div></div>
    <div class="guide-card"><div class="guide-num">04</div><div class="guide-title">Deploy for free</div><div class="guide-desc">Push to GitHub then deploy at share.streamlit.io — free for public repositories with one click.</div></div>
  </div>

  <div class="step-label">Step 1 — Installation</div>
  <div class="step-title">Install required packages</div>
  <div class="step-body">Open your terminal and run the following commands:</div>
  <div class="code-block"><span class="cm"># Create a project folder</span>
mkdir archsketch-app && cd archsketch-app

<span class="cm"># Install dependencies</span>
pip install streamlit pandas pillow requests

<span class="cm"># Verify Streamlit installed correctly</span>
streamlit hello</div>

  <div class="step-label">Step 2 — Your First App</div>
  <div class="step-title">Create app.py</div>
  <div class="step-body">Create a file called app.py and paste this starter code:</div>
  <div class="code-block"><span class="kw">import</span> streamlit <span class="kw">as</span> st
<span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">import</span> json

<span class="cm"># Page configuration</span>
st.<span class="fn">set_page_config</span>(
    page_title=<span class="str">"ArchSketch Atlas"</span>,
    page_icon=<span class="str">"🏛"</span>,
    layout=<span class="str">"wide"</span>
)

st.<span class="fn">title</span>(<span class="str">"🏛 ArchSketch Atlas"</span>)
st.<span class="fn">markdown</span>(<span class="str">"Explore architectural sketches with geo-coordinates"</span>)

<span class="cm"># Load your JSON dataset (exported from ArchSketch Atlas)</span>
<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"sketches.json"</span>) <span class="kw">as</span> f:
    data = json.<span class="fn">load</span>(f)

df = pd.<span class="fn">DataFrame</span>(data)

<span class="cm"># Sidebar filters</span>
style = st.sidebar.<span class="fn">selectbox</span>(
    <span class="str">"Filter by style"</span>,
    [<span class="str">"All"</span>] + df[<span class="str">"style"</span>].<span class="fn">unique</span>().<span class="fn">tolist</span>()
)
<span class="kw">if</span> style != <span class="str">"All"</span>:
    df = df[df[<span class="str">"style"</span>] == style]

<span class="cm"># Map view with coordinates</span>
st.<span class="fn">subheader</span>(<span class="str">"📍 Locations on Map"</span>)
st.<span class="fn">map</span>(df[[<span class="str">"lat"</span>, <span class="str">"lon"</span>]])

<span class="cm"># Gallery grid (3 columns)</span>
st.<span class="fn">subheader</span>(<span class="str">"🖼 Sketch Gallery"</span>)
cols = st.<span class="fn">columns</span>(3)
<span class="kw">for</span> i, row <span class="kw">in</span> df.<span class="fn">iterrows</span>():
    <span class="kw">with</span> cols[i % 3]:
        st.<span class="fn">image</span>(row[<span class="str">"image_url"</span>], caption=row[<span class="str">"title"</span>], use_column_width=<span class="kw">True</span>)
        st.<span class="fn">markdown</span>(<span class="fn">f</span><span class="str">"`{row['lat']:.4f}°, {row['lon']:.4f}°`"</span>)
        st.<span class="fn">caption</span>(row[<span class="str">"style"</span>] + <span class="str">" · "</span> + row[<span class="str">"technique"</span>])</div>

  <div class="step-label">Step 3 — Run locally</div>
  <div class="step-title">Launch your app</div>
  <div class="code-block"><span class="cm"># Run in your terminal from the project folder</span>
streamlit run app.py

<span class="cm"># App opens automatically at:</span>
<span class="str">http://localhost:8501</span></div>
</div>

<!-- ===== GITHUB ===== -->
<div id="section-github" class="section">
  <div class="section-title">Deploy on GitHub</div>
  <div class="section-sub">Push your Streamlit app to GitHub and share it with the world — for free. The whole process takes under 10 minutes.</div>

  <div class="step-label">Step 1 — Initialize Git</div>
  <div class="step-title">Set up your local repository</div>
  <div class="code-block"><span class="cm"># Initialize git in your project folder</span>
git init
git add .
git commit -m <span class="str">"Initial commit: ArchSketch Atlas app"</span></div>

  <div class="step-label">Step 2 — Create requirements.txt</div>
  <div class="step-title">List your dependencies</div>
  <div class="step-body">Streamlit Cloud needs this file to install packages automatically:</div>
  <div class="code-block"><span class="cm"># requirements.txt — save in your project root</span>
streamlit==1.32.0
pandas==2.1.0
pillow==10.0.0
requests==2.31.0</div>

  <div class="step-label">Step 3 — Push to GitHub</div>
  <div class="step-title">Upload your code</div>
  <div class="code-block"><span class="cm"># Add your GitHub remote (replace with your username/repo)</span>
git remote add origin https://github.com/YOUR_USERNAME/archsketch-atlas.git

<span class="cm"># Push your code</span>
git branch -M main
git push -u origin main</div>

  <div class="step-label">Step 4 — Deploy on Streamlit Cloud</div>
  <div class="step-title">One-click deployment</div>
  <div class="step-body">Go to share.streamlit.io, sign in with GitHub, select your repository, and click Deploy. Your app will be live within minutes.</div>
  <div class="code-block"><span class="cm"># Your app will be live at:</span>
https://YOUR_USERNAME-archsketch-atlas-app-XXXX.streamlit.app

<span class="cm"># Recommended folder structure:</span>
archsketch-atlas/
  ├── app.py             <span class="cm"># main Streamlit app</span>
  ├── requirements.txt   <span class="cm"># dependencies</span>
  ├── sketches.json      <span class="cm"># coordinate data (copy from gallery)</span>
  └── README.md          <span class="cm"># project description</span></div>

  <div class="step-label">Step 5 — README Template</div>
  <div class="step-title">Describe your project</div>
  <div class="code-block"><span class="cm"># README.md</span>
# 🏛 ArchSketch Atlas

An interactive explorer of architectural sketches with real-world
geo-coordinates. Built with Streamlit and Python.

## Features
- 📍 Map view of sketch locations worldwide
- 🖼 Gallery with style and technique filters
- 📋 JSON data export for each sketch
- 🔍 Search by style, location, or technique

## Run Locally
<span class="str">```bash</span>
pip install -r requirements.txt
streamlit run app.py
<span class="str">```</span>

## Deploy
Visit share.streamlit.io and connect your GitHub repo.</div>
</div>

<!-- ===== ABOUT ===== -->
<div id="section-about" class="section">
  <div class="section-title">About ArchSketch Atlas</div>
  <div class="about-grid">
    <div class="about-text">
      <p>ArchSketch Atlas is a learning resource for architecture students and beginners. Every sketch in the library is tagged with real-world geographic coordinates, architectural style, drawing technique, and contextual notes — making them ready to use in Streamlit data applications.</p>
      <h3>Why Coordinates Matter</h3>
      <p>Architecture is rooted in place. Knowing the latitude and longitude of a building allows you to cross-reference sketches with satellite maps, climate data, historical records, and urban context. When you learn to draw a Gothic cathedral, understanding it sits at 45.4642°N, 9.1900°E in Milan changes how you see the design.</p>
      <h3>Perfect for Beginners</h3>
      <p>This project is designed to be your first real dataset. The JSON format is simple, the coordinates are accurate, and every sketch includes enough metadata to build a meaningful Streamlit app that you can put on your portfolio from day one.</p>
      <h3>How to Use the Data</h3>
      <p>Click any sketch in the gallery to see its full coordinate entry and copy it as JSON or CSV. Paste into your sketches.json file and load it into your Streamlit app.</p>
    </div>
    <div>
      <div class="stat-grid">
        <div class="stat-card"><span class="stat-num">9</span><span class="stat-label">Sketch Types</span></div>
        <div class="stat-card"><span class="stat-num">5</span><span class="stat-label">Countries</span></div>
        <div class="stat-card"><span class="stat-num">100%</span><span class="stat-label">Free to Use</span></div>
        <div class="stat-card"><span class="stat-num">JSON</span><span class="stat-label">Export Format</span></div>
      </div>
      <div style="border:1px solid var(--line);border-radius:3px;padding:16px;">
        <div style="font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--stone);margin-bottom:12px;font-family:'DM Mono',monospace">// Coordinate Schema</div>
        <div style="font-family:'DM Mono',monospace;font-size:11px;color:var(--ink);line-height:2.2">
          <span style="color:var(--stone)">dataset_id</span>: <span style="color:var(--rust)">string</span><br>
          <span style="color:var(--stone)">lat</span>: <span style="color:var(--rust)">float</span> <span style="color:var(--stone)">(decimal degrees)</span><br>
          <span style="color:var(--stone)">lon</span>: <span style="color:var(--rust)">float</span> <span style="color:var(--stone)">(decimal degrees)</span><br>
          <span style="color:var(--stone)">location</span>: <span style="color:var(--rust)">string</span><br>
          <span style="color:var(--stone)">style</span>: <span style="color:var(--rust)">string</span><br>
          <span style="color:var(--stone)">technique</span>: <span style="color:var(--rust)">string</span><br>
          <span style="color:var(--stone)">period</span>: <span style="color:var(--rust)">string</span><br>
          <span style="color:var(--stone)">tags</span>: <span style="color:var(--rust)">array[string]</span><br>
          <span style="color:var(--stone)">image_url</span>: <span style="color:var(--rust)">string</span>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- MODAL -->
<div class="modal-bg" id="modalBg" onclick="closeModal(event)">
  <div class="modal" id="modal">
    <button class="close-btn" onclick="closeModalDirect()">×</button>
    <div class="modal-img-wrap">
      <img class="modal-img" id="modalImg" src="" alt="">
    </div>
    <div class="modal-detail">
      <div class="modal-type-label" id="modalType"></div>
      <div class="modal-title" id="modalTitle"></div>
      <div class="modal-subtitle" id="modalSubtitle"></div>
      <div class="coord-block">
        <div class="cb-label">// Coordinate Data</div>
        <div class="cb-row"><span class="cb-key">lat</span><span class="cb-val" id="mLat"></span></div>
        <div class="cb-row"><span class="cb-key">lon</span><span class="cb-val" id="mLon"></span></div>
        <div class="cb-row"><span class="cb-key">location</span><span class="cb-val" id="mLoc"></span></div>
        <div class="cb-row"><span class="cb-key">style</span><span class="cb-val" id="mStyle"></span></div>
        <div class="cb-row"><span class="cb-key">technique</span><span class="cb-val" id="mTech"></span></div>
        <div class="cb-row"><span class="cb-key">period</span><span class="cb-val" id="mPeriod"></span></div>
        <div class="cb-row"><span class="cb-key">dataset_id</span><span class="cb-val" id="mId"></span></div>
      </div>
      <div class="tags-list" id="mTags"></div>
      <button class="copy-btn" id="copyJsonBtn" onclick="copyJSON()">Copy JSON for Streamlit ↗</button>
      <button class="copy-btn alt" id="copyCsvBtn" onclick="copyCSV()">Copy CSV Row ↗</button>
    </div>
  </div>
</div>

<script>
const SKETCHES = [
  {
    id:"AS-0001", type:"arch",
    title:"Milan Duomo — Gothic Cathedral",
    subtitle:"Pencil technical illustration with architectural annotations and construction grid",
    location:"Milan, Italy", lat:45.4642, lon:9.1900,
    style:"Gothic Revival", technique:"Pencil + Ink Wash", period:"14th Century",
    tags:["cathedral","gothic","spires","dome","ornamental","Italy"],
    image:"https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=500&q=80"
  },
  {
    id:"AS-0002", type:"arch",
    title:"Fantasy Castle — Medieval Fortress",
    subtitle:"Pen sketch of a fairytale castle with arched bridge and clustered towers",
    location:"Loire Valley, France", lat:47.6609, lon:0.8799,
    style:"Romanesque / Fantasy", technique:"Fine Liner Pen", period:"12th Century Inspired",
    tags:["castle","medieval","towers","bridge","fantasy","France"],
    image:"https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&q=80"
  },
  {
    id:"AS-0003", type:"scene",
    title:"Garden Waterfall — Natural Scene",
    subtitle:"Graphite landscape study with cascading water, mossy rocks and stepping stones",
    location:"Kyoto, Japan", lat:35.0116, lon:135.7681,
    style:"Naturalistic Landscape", technique:"Graphite Pencil", period:"Contemporary",
    tags:["waterfall","garden","rocks","nature","reflection","Japan"],
    image:"https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=500&q=80"
  },
  {
    id:"AS-0004", type:"interior",
    title:"Grand Hall — Interior Perspective",
    subtitle:"Ballpoint pen one-point perspective of a palatial neoclassical interior with columns",
    location:"St. Petersburg, Russia", lat:59.9311, lon:30.3609,
    style:"Neoclassical", technique:"Ballpoint Pen", period:"18th Century",
    tags:["interior","columns","stairs","perspective","ballpoint","Russia"],
    image:"https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=500&q=80"
  },
  {
    id:"AS-0005", type:"urban",
    title:"Puddle Reflection — Urban Building",
    subtitle:"Surreal pencil drawing of a Victorian building inverted and mirrored in a rain puddle",
    location:"London, UK", lat:51.5074, lon:-0.1278,
    style:"Surrealism / Urban", technique:"Pencil Hatching", period:"Contemporary",
    tags:["reflection","puddle","building","surreal","urban","London"],
    image:"https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=500&q=80"
  },
  {
    id:"AS-0006", type:"urban",
    title:"Underground Station — Metro Platform",
    subtitle:"Charcoal drawing of a vaulted metro station with atmospheric lighting and trains",
    location:"Paris, France", lat:48.8566, lon:2.3522,
    style:"Industrial / Atmospheric", technique:"Charcoal", period:"Contemporary",
    tags:["metro","tunnel","train","atmosphere","arches","Paris"],
    image:"https://images.unsplash.com/photo-1569960193803-0d7eb58f5b8e?w=500&q=80"
  },
  {
    id:"AS-0007", type:"urban",
    title:"Old Town Alley — Cobblestone Street",
    subtitle:"Pencil sketch of a narrow Mediterranean alleyway with worn steps and hanging laundry",
    location:"Dubrovnik, Croatia", lat:42.6507, lon:18.0944,
    style:"Mediterranean Urban", technique:"Pencil Sketch", period:"17th Century Context",
    tags:["alley","cobblestone","steps","arch","mediterranean","Croatia"],
    image:"https://images.unsplash.com/photo-1467803738586-46b7eb7b16a1?w=500&q=80"
  },
  {
    id:"AS-0008", type:"urban",
    title:"Lisbon Tram — Street Reflection",
    subtitle:"Graphite study of a vintage tram turning a corner with a dramatic wet-street reflection",
    location:"Lisbon, Portugal", lat:38.7169, lon:-9.1395,
    style:"Urban Realism", technique:"Graphite + Ink", period:"Contemporary",
    tags:["tram","street","reflection","lisbon","vintage","Portugal"],
    image:"https://images.unsplash.com/photo-1558981403-c5f9899a28bc?w=500&q=80"
  },
  {
    id:"AS-0009", type:"3d",
    title:"Chess King — 3D Object Study",
    subtitle:"Detailed charcoal drawing of a chess king piece on a board — an exercise in form and shadow",
    location:"Study Exercise", lat:0.0, lon:0.0,
    style:"Object Study / 3D", technique:"Charcoal + Blending", period:"Contemporary",
    tags:["chess","3d","object","shading","form","still life"],
    image:"https://images.unsplash.com/photo-1529699211952-734e80c4d42b?w=500&q=80"
  }
];

const TYPE_LABELS = {arch:"Architecture", scene:"Landscape", urban:"Urban", interior:"Interior", "3d":"3D Object"};
const TYPE_CLASSES = {arch:"t-arch", scene:"t-scene", urban:"t-urban", interior:"t-interior", "3d":"t-3d"};

let currentFilter = "all";
let currentSearch = "";
let activeSketch = null;

function renderGallery() {
  const gallery = document.getElementById("gallery");
  const q = currentSearch.toLowerCase();
  const filtered = SKETCHES.filter(s => {
    const matchType = currentFilter === "all" || s.type === currentFilter;
    const matchSearch = !q
      || s.title.toLowerCase().includes(q)
      || s.style.toLowerCase().includes(q)
      || s.location.toLowerCase().includes(q)
      || s.technique.toLowerCase().includes(q)
      || s.tags.some(t => t.toLowerCase().includes(q));
    return matchType && matchSearch;
  });
  if (filtered.length === 0) {
    gallery.innerHTML = '<div class="empty-state"><span>✏️</span>No sketches found. Try a different search term.</div>';
    return;
  }
  gallery.innerHTML = filtered.map(s => `
    <div class="card" onclick="openModal('${s.id}')">
      <img class="card-img" src="${s.image}" alt="${s.title}" loading="lazy"
           onerror="this.src='https://via.placeholder.com/400x185/1a1714/faf8f4?text=Sketch'">
      <div class="card-info">
        <span class="card-type ${TYPE_CLASSES[s.type]}">${TYPE_LABELS[s.type]}</span>
        <div class="card-title">${s.title}</div>
        <div class="card-meta">
          ${s.location}<br>
          ${s.lat.toFixed(4)}°, ${s.lon.toFixed(4)}°
        </div>
      </div>
    </div>
  `).join("");
}

function setFilter(f, btn) {
  currentFilter = f;
  document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("on"));
  btn.classList.add("on");
  renderGallery();
}

function filterCards() {
  currentSearch = document.getElementById("searchInput").value;
  renderGallery();
}

function openModal(id) {
  const s = SKETCHES.find(x => x.id === id);
  if (!s) return;
  activeSketch = s;
  document.getElementById("modalImg").src = s.image;
  document.getElementById("modalImg").alt = s.title;
  document.getElementById("modalType").textContent = TYPE_LABELS[s.type];
  document.getElementById("modalTitle").textContent = s.title;
  document.getElementById("modalSubtitle").textContent = s.subtitle;
  document.getElementById("mLat").textContent = s.lat.toFixed(6) + "°";
  document.getElementById("mLon").textContent = s.lon.toFixed(6) + "°";
  document.getElementById("mLoc").textContent = s.location;
  document.getElementById("mStyle").textContent = s.style;
  document.getElementById("mTech").textContent = s.technique;
  document.getElementById("mPeriod").textContent = s.period;
  document.getElementById("mId").textContent = s.id;
  document.getElementById("mTags").innerHTML = s.tags.map(t => `<span class="tag">${t}</span>`).join("");
  const jb = document.getElementById("copyJsonBtn");
  jb.textContent = "Copy JSON for Streamlit ↗";
  jb.className = "copy-btn";
  document.getElementById("copyCsvBtn").textContent = "Copy CSV Row ↗";
  document.getElementById("modalBg").classList.add("open");
  document.body.style.overflow = "hidden";
}

function closeModal(e) {
  if (e.target === document.getElementById("modalBg")) closeModalDirect();
}

function closeModalDirect() {
  document.getElementById("modalBg").classList.remove("open");
  document.body.style.overflow = "";
}

function copyJSON() {
  if (!activeSketch) return;
  const payload = JSON.stringify({
    dataset_id: activeSketch.id,
    title: activeSketch.title,
    lat: activeSketch.lat,
    lon: activeSketch.lon,
    location: activeSketch.location,
    style: activeSketch.style,
    technique: activeSketch.technique,
    period: activeSketch.period,
    type: activeSketch.type,
    tags: activeSketch.tags,
    image_url: activeSketch.image
  }, null, 2);
  navigator.clipboard.writeText(payload).then(() => {
    const btn = document.getElementById("copyJsonBtn");
    btn.textContent = "✓ JSON Copied!";
    btn.classList.add("success");
    setTimeout(() => {
      btn.textContent = "Copy JSON for Streamlit ↗";
      btn.classList.remove("success");
    }, 2500);
  }).catch(() => alert("Please copy manually: " + payload));
}

function copyCSV() {
  if (!activeSketch) return;
  const header = "dataset_id,title,lat,lon,location,style,technique,period,type,image_url";
  const row = [
    activeSketch.id,
    '"' + activeSketch.title + '"',
    activeSketch.lat,
    activeSketch.lon,
    '"' + activeSketch.location + '"',
    '"' + activeSketch.style + '"',
    '"' + activeSketch.technique + '"',
    '"' + activeSketch.period + '"',
    activeSketch.type,
    '"' + activeSketch.image + '"'
  ].join(",");
  navigator.clipboard.writeText(header + "\n" + row).then(() => {
    const btn = document.getElementById("copyCsvBtn");
    btn.textContent = "✓ CSV Copied!";
    setTimeout(() => { btn.textContent = "Copy CSV Row ↗"; }, 2500);
  }).catch(() => alert("Copy manually:\n" + header + "\n" + row));
}

function switchSection(id) {
  document.querySelectorAll(".section").forEach(s => s.classList.remove("active"));
  document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
  document.querySelectorAll(".nav-link").forEach(l => l.classList.remove("active"));
  const sec = document.getElementById("section-" + id);
  if (sec) sec.classList.add("active");
  document.querySelectorAll(".tab, .nav-link").forEach(el => {
    const oc = el.getAttribute("onclick") || "";
    if (oc.includes("'" + id + "'")) el.classList.add("active");
  });
}

document.addEventListener("keydown", e => {
  if (e.key === "Escape") closeModalDirect();
});

renderGallery();
</script>
</body>
</html>
