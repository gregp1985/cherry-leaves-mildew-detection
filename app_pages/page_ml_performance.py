import streamlit as st


def page_ml_performance_body():
    st.title("ML Performance")

    st.write(
        "This page shows the model evaluation results and confirms whether the model "
        "met the agreed business requirement."
    )

    st.header("Business Success Metric")
    st.write("The agreed performance target was **97% prediction accuracy**.")

    st.header("Model Result")
    st.success("The model achieved **99% test accuracy**, exceeding the required target.")

    st.header("Accuracy Curve")
    st.image("outputs/plots/accuracy_plot.png")

    st.header("Loss Curve")
    st.image("outputs/plots/loss_plot.png")

    st.header("Confusion Matrix")
    st.image("outputs/plots/confusion_matrix.png")

    st.header("Conclusion")
    st.write(
        "The model successfully answers the predictive business requirement by classifying "
        "cherry leaves as healthy or affected by powdery mildew with performance above "
        "the required threshold."
    )