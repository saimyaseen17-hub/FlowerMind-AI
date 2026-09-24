import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json
from pathlib import Path


# ==================================================
# Page Configuration
# ==================================================

st.set_page_config(
    page_title="FlowerMind AI",
    page_icon="🌸",
    layout="centered"
)


# ==================================================
# Load External CSS
# ==================================================

BASE_DIR = Path(__file__).parent

css_file = BASE_DIR / "style.css"

with open(css_file, "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# ==================================================
# Load V4 Model
# ==================================================

@st.cache_resource
def load_model():

    model_path = BASE_DIR / "flower_model_v4.keras"

    return tf.keras.models.load_model(
        model_path
    )


model = load_model()


# ==================================================
# Load Class Names
# ==================================================

@st.cache_data
def load_class_names():

    class_file = BASE_DIR / "class_names_v4.json"

    with open(
        class_file,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


class_names = load_class_names()


# ==================================================
# Header
# ==================================================

st.title("🌸 FlowerMind AI")

st.caption(
    "Smart Flower Classification Powered by Artificial Intelligence"
)

st.divider()


# ==================================================
# Upload Image
# ==================================================

st.subheader("📷 Upload Your Flower")

uploaded_file = st.file_uploader(
    "Choose a flower image",
    type=[
        "jpg",
        "jpeg",
        "png"
    ],
    help="Upload a clear flower image for better prediction."
)


# ==================================================
# Prediction
# ==================================================

if uploaded_file is not None:

    # ----------------------------------------------
    # Open Image
    # ----------------------------------------------

    image = Image.open(
        uploaded_file
    ).convert("RGB")


    # ----------------------------------------------
    # Display Image
    # ----------------------------------------------

    st.image(
        image,
        caption="Uploaded Flower",
        use_container_width=True
    )

    st.divider()


    # ----------------------------------------------
    # Predict Button
    # ----------------------------------------------

    if st.button(
        "🔍 Predict Flower",
        use_container_width=True
    ):

        with st.spinner(
            "FlowerMind AI is analyzing..."
        ):

            # Resize image
            img = image.resize(
                (224, 224)
            )

            # Convert to NumPy
            img_array = np.array(
                img
            ).astype("float32")

            # Add batch dimension
            img_array = np.expand_dims(
                img_array,
                axis=0
            )

            # Prediction
            prediction = model.predict(
                img_array,
                verbose=0
            )[0]


            # --------------------------------------
            # Get Prediction
            # --------------------------------------

            predicted_index = np.argmax(
                prediction
            )

            predicted_class = class_names[
                predicted_index
            ]

            confidence = (
                prediction[predicted_index] * 100
            )


        # ------------------------------------------
        # Result
        # ------------------------------------------

        st.subheader("🤖 AI Prediction")

        result_col1, result_col2 = st.columns(2)

        with result_col1:

            st.success(
                f"🌸 {predicted_class.title()}"
            )

        with result_col2:

            st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )


        st.divider()


        # ------------------------------------------
        # Probabilities
        # ------------------------------------------

        st.subheader("📊 Prediction Probabilities")

        sorted_indices = np.argsort(
            prediction
        )[::-1]


        for index in sorted_indices:

            flower = class_names[index]

            probability = float(
                prediction[index]
            )

            percentage = (
                probability * 100
            )

            st.write(
                f"**{flower.title()}** — "
                f"{percentage:.2f}%"
            )

            st.progress(
                probability
            )


else:

    st.info(
        "👆 Upload a flower image above to begin."
    )


# ==================================================
# Footer
# ==================================================

st.divider()

st.caption(
    "🌸 FlowerMind AI"
)

st.caption(
    "Made by Muhammad Saim"
)