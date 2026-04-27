import streamlit as st


def page_ml_performance_body():
    st.title("ML Performance")

    st.write(
        "This page shows the model evaluation results and confirms whether the model "
        "met the agreed business requirement."
    )

    st.header("Business Success Metric")
    st.write("The Business Requirement was **97% prediction accuracy**.")

    st.header("Model Result")
    st.success("The model achieved **99% test accuracy**, exceeding the Business Requirement.")

    st.info("Expand each section below to explore the analysis.")

    with st.expander("Show Accuracy Curve"):
        st.header("Accuracy Curve")
        st.image("outputs/plots/accuracy_plot.png")
        st.write(
            "The accuracy curve shows how the model improved during training and validation."
        )

    with st.expander("Show Loss Curve"):
        st.header("Loss Curve")
        st.image("outputs/plots/loss_plot.png")
        st.write(
            "The loss curve helps show whether the model learned effectively and whether there were signs of overfitting."
        )

    with st.expander("Show Confusion Matrix"):
        st.header("Confusion Matrix")
        st.image("outputs/plots/confusion_matrix.png")
        st.write(
            "The confusion matrix shows how many test images were correctly or incorrectly classified."
        )

    st.header("Conclusion")
    st.write(
        "The model successfully answers the predictive business requirement by classifying "
        "cherry leaves as healthy or affected by powdery mildew with performance above "
        "the required threshold."
    )