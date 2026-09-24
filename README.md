# 🌸 FlowerMind AI

**FlowerMind AI** is an AI-powered flower classification application that identifies flowers from uploaded images using a deep learning model based on **EfficientNetB0**.

The application provides a predicted flower class along with the model's confidence and class-wise prediction probabilities.

## ✨ Features

* 🌸 Flower image classification
* 🤖 EfficientNetB0 deep learning model
* 📷 Upload JPG, JPEG, and PNG images
* 🎯 Prediction confidence score
* 📊 Class-wise probability results
* ⚡ Simple and user-friendly Streamlit interface
* 🚀 Ready for web deployment

## 🌺 Supported Flower Classes

The model currently classifies:

* Daisy
* Dandelion
* Rose
* Sunflower
* Tulip

## 🧠 Model

**Architecture:** EfficientNetB0
**Input Size:** 224 × 224 pixels
**Framework:** TensorFlow / Keras
**Task:** Multi-class image classification

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Pillow
* Streamlit

## 📁 Project Structure

```text
FlowerMind-AI/
│
├── app.py
├── style.css
├── flower_model_v4.keras
├── class_names_v4.json
└── requirements.txt
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/FlowerMind-AI.git
```

### 2. Open the project folder

```bash
cd FlowerMind-AI
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📷 How to Use

1. Open FlowerMind AI.
2. Upload a flower image.
3. Click **Predict Flower**.
4. The AI will display the predicted flower.
5. View the confidence score and class probabilities.

## 📊 Prediction Output

The application displays:

* **Predicted Flower**
* **Confidence Percentage**
* **Prediction Probabilities** for all supported classes

## 👨‍💻 Author

**Muhammad Saim**

AI Engineering | Machine Learning | Deep Learning

---

⭐ If you find this project useful, consider giving the repository a star.

**🌸 FlowerMind AI — Helping AI recognize the beauty of flowers.**
