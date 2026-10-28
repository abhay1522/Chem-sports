import runpy
from pathlib import Path
import streamlit as st

PAGES = {
    "🏁 Home": "home.py",
    "📘 Theory": "theory.py",
    "🧬 Molecular Visualization": "visualization.py",
    "📊 Molecular Properties Report": "properties.py",
    "📈 Structure–Property Analysis": "analysis.py",
    "📝 Assessment": "assessment.py",
    "🏆 Final Project Report": "report.py",
}
choice = st.sidebar.radio("🏎️ Chem Garage menu", list(PAGES))
runpy.run_path(str(Path(__file__).parent / PAGES[choice]), run_name="__main__")
