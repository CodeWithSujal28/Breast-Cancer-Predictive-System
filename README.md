# 🩺 Breast Cancer Prediction Web App

A **machine learning–based web application** that predicts whether a breast tumor is **Benign** or **Malignant** using medical features.
The model is trained with proper evaluation techniques and deployed using **Flask** with a clean **Dark/Light mode UI**.

---

## 🚀 Features

* 🔍 Predicts **Benign (1)** or **Malignant (0)** breast cancer
* 🧠 Machine Learning model: **Logistic Regression**
* 🎯 **Feature Selection**: Reduced input features from **31 to 6**
* 📊 Model evaluation using:

  * Cross-validation
  * Accuracy
  * Confusion matrix
  * Classification report
* 🌗 **Dark & Light Mode** UI
* 🔄 New Prediction / Refresh button
* 🎨 Clean, modern, and responsive design

---

## 🧠 Machine Learning Workflow

1. Data preprocessing
2. Feature selection using **SelectKBest (ANOVA F-test)**
3. Feature scaling using **StandardScaler**
4. Model training with **Logistic Regression**
5. Model evaluation and selection
6. Model deployment using **Flask**

---

## 🧪 Selected Input Features

The model uses only the **top 6 most important features**:

* Perimeter Mean
* Concave Points Mean
* Radius Worst
* Perimeter Worst
* Area Worst
* Concave Points Worst

This makes the application **user-friendly** and practical for real-world use.

---

## 🖥️ Tech Stack

* **Python**
* **Flask**
* **Scikit-learn**
* **Pandas**
* **NumPy**
* **HTML, CSS**
* **Joblib**

---

## 📁 Project Structure

```
breast-cancer-prediction/
│
├── app.py
├── model/
│   ├── breast_cancer_model.pkl
│   ├── scaler.pkl
│   └── feature_selector.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

1. **Clone the repository**

```bash
git clone https://github.com/your-username/breast-cancer-prediction.git
cd breast-cancer-prediction
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Flask app**

```bash
python app.py
```

4. **Open in browser**

```
http://127.0.0.1:5000
```

---

## ⚠️ Disclaimer

This project is created **for educational purposes only**.
It is **not a replacement for professional medical diagnosis**.

---

## 👨‍💻 Author

**Sujal Mondal**

---

⭐ If you like this project, don’t forget to **star the repository**!
