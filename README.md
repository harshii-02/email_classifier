
# 📧 Email Classifier Web App

This project is a simple machine learning web application built using **Streamlit** that classifies email messages into categories such as **Work**, **Personal**, **Promotions**, **Spam**, and **Urgent**.

It uses a **Naive Bayes classifier** trained on a small sample dataset and performs **text classification** using **TF-IDF vectorization**.

---

## 🚀 Features

- ✅ Simple and interactive UI using Streamlit
- 🧠 Real-time prediction of email category
- 🗂 Categorizes emails into:
  - Work
  - Personal
  - Promotions
  - Spam
  - Urgent

---

## 🛠 Technologies Used

- Python 3.x
- Streamlit
- scikit-learn
- pandas

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/harshii-02/email-classifier.git
cd email-classifier-app

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
````

If `requirements.txt` does not exist, install manually:

```bash
pip install streamlit scikit-learn pandas
```

---

## 🧪 Running the App

```bash
streamlit run email_classifier_app.py
```

Then open your browser and navigate to `http://localhost:8501`.

---

## 📁 File Structure

```
email_classifier_app.py       # Main Streamlit app
README.md                     # Project description
requirements.txt              # Dependencies (optional)
```

---

## 📬 Example Input

```
Hi team, please review the attached agenda for tomorrow’s meeting.

Predicted Category: Work
```





