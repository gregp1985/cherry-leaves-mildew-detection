import streamlit as st


def page_project_hypothesis_body():

    st.title("Project Hypothesis")

    st.write(
        "This section outlines the key hypotheses for the project and how each was validated "
        "through analysis and model performance."
    )

    # --- Hypothesis 1 ---
    with st.expander("Hypothesis 1: Visual Differences Exist", expanded=True):

        st.write(
            "Cherry leaves affected by powdery mildew have visible differences in colour and texture "
            "compared to healthy leaves."
        )

        st.write("**Validation:**")
        st.write("- Average images showed lighter, patchy regions in infected leaves")
        st.write("- Variability images highlighted irregular patterns")
        st.write("- Image montage confirmed visible fungal markings")

        st.success("Conclusion: Visual differences between classes were clearly identified.")

    st.markdown("---")

    # --- Hypothesis 2 ---
    with st.expander("Hypothesis 2: A CNN Model Can Learn These Patterns"):

        st.write(
            "A Convolutional Neural Network (CNN) can learn the visual differences between healthy "
            "and infected leaves."
        )

        st.write("**Validation:**")
        st.write("- The model achieved 99% accuracy on unseen test data")
        st.write("- The confusion matrix showed strong classification performance")
        st.write("- Loss and accuracy curves confirmed effective learning without overfitting")

        st.success("Conclusion: The model successfully learned and generalised the patterns.")

    st.markdown("---")

    # --- Hypothesis 3 ---
    with st.expander("Hypothesis 3: The Model Can Be Applied in a Real-World Tool"):

        st.write(
            "The trained model can be integrated into an interactive dashboard to support "
            "real-time decision-making."
        )

        st.write("**Validation:**")
        st.write("- The Streamlit dashboard allows users to upload images")
        st.write("- Predictions are returned instantly with probability scores")
        st.write("- The deployed Heroku application functions correctly with real test images")

        st.success("Conclusion: The model was successfully deployed and functions as intended.")

    # --- Final Summary ---
    st.header("Overall Conclusion")

    st.write(
        "All three hypotheses were validated through visual analysis, model performance, "
        "and successful deployment. This confirms that machine learning can effectively "
        "support the identification of powdery mildew in cherry leaves."
    )