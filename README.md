# Adult-Salary-Predictor
# 💼 Adult Salary Prediction - Streamlit App

This project predicts whether a person earns more than $50K per year using demographic features like age, education, occupation, etc.

Built using **Python**, **Scikit-learn**, and **Streamlit**, it's a full pipeline from data preprocessing to deployment!

---

## 🚀 Features

- Cleaned and preprocessed Adult Income dataset
- Trained with **Random Forest** + **Hyperparameter Tuning**
- Final model selected using **RandomizedSearchCV**
- Deployed as an interactive **Streamlit Web App**
- Supports **user input** through the frontend
- Metrics used: **Accuracy**, **F1 Score**, and **Confusion Matrix**

---

## 🧠 Dataset Info

- Source: UCI Machine Learning Repository
- Goal: Classify whether income is >50K or <=50K
- Features: Age, Workclass, Education, Marital-status, Occupation, etc.

---

## 🧪 Tech Stack

- Python
- Pandas, NumPy, Scikit-learn
- Joblib (for model serialization)
- Streamlit (for deployment)
- Matplotlib / Seaborn (for EDA)

---

## 🖥️ Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/adult-salary-prediction.git
cd adult-salary-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

