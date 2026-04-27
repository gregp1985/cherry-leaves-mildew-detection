import streamlit as st


def page_project_hypothesis_body():
    st.title("Project Hypothesis")

    st.header("Hypothesis")
    st.write(
        "Cherry leaves affected by powdery mildew have visible patterns that can be "
        "distinguished from healthy leaves through image analysis, and these patterns "
        "can be learned by a neural network classifier."
    )

    st.header("Validation")
    st.write(
        "The visual analysis showed differences in colour, texture, and visible fungal "
        "patches between healthy and infected leaves."
    )

    st.write(
        "The CNN model achieved 99% test accuracy, exceeding the agreed success metric "
        "of 97% accuracy."
    )

    st.success(
        "The hypothesis was validated by both the visual analysis and the machine learning model performance."
    )