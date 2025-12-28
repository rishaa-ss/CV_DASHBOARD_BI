import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="CV | Rishaa SureshKumar",
    page_icon="📄",
    layout="wide"
)

# ==================================================
# CSS
# ==================================================
st.markdown("""
<style>
/* ---------- SECTION TITLES (NEON GLOW) ---------- */
h1, h2, h3, h4, h5, h6 {
    font-weight:900;
    color: #33ffff; /* Soft neon for headings */
    text-shadow:
        0 0 2px #33ffff,
        0 0 4px #33ffff,
        0 0 6px #33ffff;
}

/* ---------- HERO TITLE / PERSONAL NAME ---------- */
.hero-title {
    font-weight:900;
    font-size:2rem;
    line-height:1.1;
    color: #ffffff; /* Normal white, no neon */
    text-shadow: none;
}

/* ---------- KPI / CARD STYLING ---------- */
.kpi-wrap {
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:16px;
    margin-top:14px;
}
.kpi {
    border:1px solid #2e3136;
    border-radius:14px;
    padding:14px;
    background:rgba(255,255,255,0.02);
}
.kpi .t { font-size:0.9rem; opacity:.75; }
.kpi .v { font-size:1.05rem; font-weight:700; }

/* ---------- MODERNIZED SIDEBAR ---------- */
[data-testid="stSidebar"] {
    background-color: #1f1f23;
    color: #fff;
    border-radius: 12px;
    padding: 20px;
    font-family: 'Arial', sans-serif;
}
[data-testid="stSidebar"] .stButton>button {
    background: linear-gradient(90deg, #33ffff, #33ff99);
    border: none;
    color: #000;
    font-weight: 600;
    border-radius: 8px;
    transition: all 0.3s ease;
}
[data-testid="stSidebar"] .stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 8px #33ffff;
}
[data-testid="stSidebar"] a {
    text-decoration: none;
    color: #33ffff;
    transition: all 0.3s ease;
}
[data-testid="stSidebar"] a:hover {
    color: #33ff99;
    text-shadow: 0 0 4px #33ffff;
}

/* ---------- MODERN CARDS ---------- */
.card {
    background-color: #1f1f23;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 16px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.5);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.7);
}
.card h3 {
    font-weight:700;
    color: #33ffff;
}
.card p {
    color: #ffffff;
    margin: 4px 0;
}

/* ---------- PIE CHART CONTAINER ---------- */
.chart-card {
    background-color: #1f1f23;
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.5);
    margin-top: 16px;
}

/* ---------- RESPONSIVE KPI ---------- */
@media (max-width:900px){
    .kpi-wrap { grid-template-columns:1fr; }
}

/* ---------- SPACER ---------- */
.spacer { height: 12px; }
</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================
with st.sidebar:
    st.title("ABOUT ME")
    st.caption("Data Apprenticeship • 2025")

    st.link_button("GitHub", "https://github.com/rishaa-ss")
    st.link_button("LinkedIn", "https://www.linkedin.com/in/rishaa-sureshkumar-b954a1292")
    st.link_button("Email", "mailto:rishaa.ssk@gmail.com")
    st.markdown("---")  # Horizontal line
    page = st.radio(
        "EXPLORE MORE",
        [
            "👤 Profile & Contact",
            "🛠 Skills",
            "📁 Academic Projects",
            "🌍 Languages & Life"
        ]
    )
    # ---------- Footer ----------
    st.markdown("---")  # Horizontal line
    st.markdown(
        "This dashboard was created under the supervision of [Sir Mano Mathew](https://www.linkedin.com/in/mano-mathew)",
        unsafe_allow_html=True
    )

# ==================================================
# 👤 PROFILE & CONTACT
# ==================================================
if page == "👤 Profile & Contact":
    left, right = st.columns([1, 2], gap="large")

    with left:
        photo_path = Path("linkedin_pp .png")
        if photo_path.exists():
            st.image(str(photo_path), use_container_width=True)
        else:
            st.info("Add your photo: facecard.jpg")
            
        pdf_path = Path("CV_Apprenticeship_2025_Rishaa SURESHKUMAR.pdf")
        if pdf_path.exists():
            st.download_button(
                "⬇️ Download my CV (PDF)",
                pdf_path.read_bytes(),
                file_name="Rishaa_CV_2025.pdf",
                mime="application/pdf",
                use_container_width=True
            ) 
            
    with right:
        st.markdown("<div class='hero-title'>Rishaa SureshKumar</div>", unsafe_allow_html=True)
        st.subheader(" 📍 Paris · 🔍 Data Apprenticeship Candidate  ·👩🏻‍💻 Engineering in Marketing & Data") 
        st.write("""
        Second-year **Engineering student at EFREI Paris**, specializing in
        **Marketing & Data**.  
        Actively seeking a **data apprenticeship** to apply analytical,
        technical, and business skills to real-world projects.
        """)

        st.info("""
        **Work-study rhythm**  
        Sep–Dec: 1w company / 2w school  
        Jan–Mar: 2w company / 1w school  
        From April: Full-time in company
        """)

    # ---------- WORK EXPERIENCE ----------
    st.markdown("## 💼 Work Experience")

    with st.expander(" Larsen & Toubro Construction — Data Analytics Intern (2024)"):
        st.write("""
        **Chennai, India — 2 months**

        • Analyzed diesel & raw material impact on ductile iron pipe pricing  
        • Built diameter-specific pricing models  
        • Data cleaning, EDA & visualization using Python  
        • Market segmentation using Machine Learning
        """)

    with st.expander(" Saint-Gobain Digital & IT — Observation Internship (2022)"):
        st.write("""
        **Courbevoie, France — 1 week**

        • HR: Assisted in recruitment, scheduling interviews, onboarding, and maintained employee records.  
        • Audio Visual: Observed AV setup, testing, and troubleshooting during events.  
        • Cybersecurity: Monitored network traffic and supported security protocols  
        • Mail Service: Managed incoming mail and internal deliveries.  
        • Badge Service: Created and managed employee ID badges and access.  
        """)

    with st.expander(" Saint-Gobain Consulting Information Organisation — Observation Internship (2018)"):
        st.write("""
        **Courbevoie, France — 1 week**

        • Observation of sales and delivery management processes.  
        • Testing of internal applications and identification of errors.  
        • Participation in meetings on production planning.  
        • Discovery of SAP integration and the aquisitions of the company.  
        """)

    # ---------- EDUCATION ----------
    st.markdown("## 🎓 Education")

    education = pd.DataFrame({
        "Institution": [
            "EFREI Paris",
            "Ecole Européenne Paris La Défense",
            "Collège Georges Pompidou"
        ],
        "Degree": [
            "Engineering – Marketing & Data",
            "European Baccalaureate",
            "National Diploma"
        ],
        "Years": [
            "2023 – 2026",
            "2019 – 2023",
            "2016 – 2019"
        ]
    })

    st.dataframe(education, use_container_width=True, hide_index=True)

# ==================================================
# 📁 PROJECTS
# ==================================================
elif page == "📁 Academic Projects":
    

    with st.container(border=True):
        st.markdown("### ✈️ Flight Management System")
        st.caption("Python · JSON")
        st.write("""
        Developed a flight management system allowing users to **add, display, save, and load flights**
        using JSON for persistent data storage, with structured input handling.
        """)

    with st.container(border=True):
        st.markdown("### 🚕 NYC Uber Trip Analysis")
        st.caption("Python · Pandas · Seaborn · Matplotlib")
        st.write("""
        Performed exploratory data analysis on NYC Uber trips to identify **usage patterns,
        peak hours, and trends**, supported by data visualizations.
        """)

    with st.container(border=True):
        st.markdown("### 🎮 Hangman Game")
        st.caption("Python")
        st.write("""
        Built a **text-based Hangman game** implementing game logic,
        loops, conditionals, and user interaction.
        """)

    with st.container(border=True):
        st.markdown("### 🎨 Rebranding Project")
        st.caption("Figma · UX/UI")
        st.write("""
        Created a new **visual identity and interactive mockups**
        for web and mobile interfaces.
        """)

    with st.container(border=True):
        st.markdown("### 🌐 Web Development Projects")
        st.caption("HTML · CSS · PHP · MySQL · WordPress")
        st.write("""
        Designed websites and developed a **client registration system**
        with validation, search, deletion, and database integration.
        """)  

# ==================================================
# 🛠 SKILLS
# ==================================================
elif page == "🛠 Skills":
    

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        with st.container(border=True):
            st.subheader("🛠 Hard Skills")
            st.markdown("""
            **Programming & Data**
            - Python *(Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn, TensorFlow)*
            - PHP / MySQL  
            - HTML & CSS  

            **Data & BI**
            - Power BI  
            - Office 365 *(Advanced Excel, Word, PowerPoint)*  

            **AI & Data Science**
            - Artificial Intelligence & Data Science *(basics)*  
            - Machine Learning · Deep Learning · Neuroscience foundations  

            **Digital & Design**
            - WordPress · SEO / SEA  
            - Figma *(UX/UI)*  
            - Adobe Suite *(Photoshop, Premiere Pro)*
            """)

    with col2:
        with st.container(border=True):
            st.subheader("🤝 Soft Skills")
            st.markdown("""
            - Trilingual  
            - Open-minded  
            - Curious  
            - Strong communication  
            - Analytical mindset
            """)

        with st.container(border=True):
            st.subheader("🧠 Working Style")
            st.markdown("""
            - Autonomous & reliable  
            - Detail-oriented  
            - Business-oriented mindset  
            - Fast learner
            """)

# ==================================================
# 🌍 LANGUAGES & LIFE (SOFT NEON TITLES)
# ==================================================
elif page == "🌍 Languages & Life":
    
    c1, c2 = st.columns(2, gap="large")

    # ---------- Educational & Social Life ----------
    with c1:
        st.markdown('''
        <div class="card">
            <h3 style="color:#f0f0f0; text-shadow:0 0 2px #33ffff, 0 0 4px #33ffff;">🎓 Educational & Social Life</h3>
            • University Ambassador<br>
            • Volunteering<br>
            • Student projects & teamwork
        </div>
        ''', unsafe_allow_html=True)

    # ---------- Interests ----------
    with c2:
        st.markdown('''
        <div class="card">
            <h3 style="color:#f0f0f0; text-shadow:0 0 2px #33ffff, 0 0 4px #33ffff;">🎭 Interests</h3>
            💃 Dance<br>
            🎬 Cinema<br>
            🎵 Music<br>
            ✈️ Travel
        </div>
        ''', unsafe_allow_html=True)

    # ---------- Language Proficiency ----------
    st.markdown('<div class="chart-card"><h3 style="color:#f0f0f0; text-shadow:0 0 2px #33ffff, 0 0 4px #33ffff;">🗣 Language Proficiency</h3></div>', unsafe_allow_html=True)

    languages = {
        "French": 100,
        "English": 100,
        "Tamil": 100,
        "Spanish": 60
    }

    # Colorful pie chart
    fig = px.pie(
        names=list(languages.keys()),
        values=list(languages.values()),
        hole=0.55,
        color_discrete_sequence=["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9"]
    )

    fig.update_layout(
        showlegend=True,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(size=14)
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success("✨ Business Intelligence Academic Project")
