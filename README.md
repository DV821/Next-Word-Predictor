
# 🧠 Next Word Predictor Using LSTM & GRU

This project implements a deep learning-based **Next Word Prediction** system using both **LSTM** and **GRU** architectures. The models are trained on Shakespeare's *Hamlet* and deployed via a user-friendly **Streamlit** web application for real-time prediction.

---

## 🚀 Project Overview

### 1. Data Collection
- **Dataset**: Shakespeare's *Hamlet* is used for its linguistic complexity and structure.

### 2. Data Preprocessing
- Lowercasing and punctuation removal.
- Tokenization using Keras `Tokenizer`.
- Sequence generation and padding for uniform input lengths.
- Data split into training and validation sets.

### 3. Model Architectures

#### 🔹 LSTM Model
- Embedding → LSTM layer → Dropout → LSTM Layer → Dense with Softmax.
- Captures long-term dependencies in word sequences.

#### 🔹 GRU Model
- Embedding → GRU layer → Dropout → GRU Layer → Dense with Softmax.
- Faster training and fewer parameters with comparable performance.

### 4. Model Training
- Optimizer: Adam
- Loss Function: Categorical Crossentropy
- Metric: Accuracy

### 5. Model Evaluation
- Both models evaluated on validation data.
- Side-by-side comparisons show LSTM performs slightly better than GRU in accuracy.

### 6. Deployment
- A **Streamlit** app (`app.py`) allows users to input a sequence of words and get predictions from LSTM model.

---

## 📁 Repository Structure

```
Next-Word-Predictor/
│
├── hamlet.txt                     # source data
├── model_lstm.keras               # Trained LSTM model
├── model_gru.keras                # Trained GRU model
├── tokenizer.pickle               # Tokenizer used for both models
├── experiments.ipynb              # Data processing, training & evaluation
├── app.py                         # Streamlit interface
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## ▶️ Getting Started

### 🔧 Prerequisites

Make sure you have Python 3.7+ installed.

Install dependencies:

```bash
pip install -r requirements.txt
```

### 🏃 Run the Streamlit App

```bash
streamlit run app.py
```

- Select either the **LSTM** or **GRU** model.
- Input a word sequence to receive a predicted next word.

---

## 🧪 Example

**Input:**
```
To be or not to
```

**Predicted Next Word (LSTM):**
```
be
```

**Predicted Next Word (GRU):**
```
heare
```

---

## 📌 Key Technologies

- Python
- TensorFlow
- NLTK
- Streamlit

---

