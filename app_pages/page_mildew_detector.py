import streamlit as st
from PIL import Image
import pandas as pd

from src.machine_learning import load_model, predict_image


def page_mildew_detector_body():

    st.title("Mildew Detector")

    st.write(
        "Upload cherry leaf images to predict whether they are healthy "
        "or affected by powdery mildew."
    )

    # Load model once
    model = load_model()

    # File uploader
    uploaded_files = st.file_uploader(
        "Upload Images",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )

    results = []

    if uploaded_files:

        for file in uploaded_files:
            image = Image.open(file)

            st.image(image, caption=file.name)

            label, prob = predict_image(model, image)

            st.write(f"Prediction: **{label}** ({prob:.2%})")

            results.append({
                "Image": file.name,
                "Prediction": label,
                "Probability": prob
            })

        # Results table
        df = pd.DataFrame(results)
        st.dataframe(df)

        # Download button
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download Results",
            data=csv,
            file_name="predictions.csv",
            mime="text/csv"
        )