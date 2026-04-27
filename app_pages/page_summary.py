import streamlit as st


def page_summary_body():
    st.title("Project Summary")

    st.header("Project Background")
    st.write(
        "Farmy & Foods is concerned about powdery mildew affecting cherry plantations. "
        "Manual inspection is time-consuming and not scalable, as employees currently spend "
        "around 30 minutes inspecting each tree."
    )

    st.header("Dataset")
    st.write(
        "The dataset contains cherry leaf images divided into two classes: "
        "**healthy** and **powdery_mildew**."
    )

    st.header("Business Requirements")
    st.write(
        "1. Conduct a visual study to differentiate healthy cherry leaves from leaves affected by powdery mildew."
    )
    st.write(
        "2. Build a machine learning system that predicts whether a cherry leaf is healthy or affected by powdery mildew."
    )

    st.header("Dashboard Pages")
    st.write(
        "- **Leaf Visualiser**: presents the visual study findings.\n"
        "- **Mildew Detector**: allows image upload and live prediction.\n"
        "- **Project Hypothesis**: explains and validates the project hypothesis.\n"
        "- **ML Performance**: shows model evaluation results."
    )