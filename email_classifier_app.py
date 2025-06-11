# 🧠 Email Classifier Web App with Streamlit

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# ----------------------
# 📚 1. Prepare Sample Data
# ----------------------
data = {
    'email': [
        "Win a free vacation now!",
        "Can you review the attached contract?",
        "Hey! Wanna hang out this weekend?",
        "Don't miss out on this special offer!",
        "Please schedule a meeting with the client.",
        "Final reminder: your invoice is due.",
        "Urgent: server is down, need immediate help",
        "Lunch at mom’s tomorrow?",
        "Exclusive deal just for you",
        "Reminder: dentist appointment at 4pm",
        "Hi Team, attached is the agenda for tomorrow’s call.",  # ← new work example
        "The meeting will be in Conference Room A at 11AM.",     # ← another work email
    ],
    'label': [
        'Spam', 'Work', 'Personal', 'Promotions', 'Work',
        'Urgent', 'Urgent', 'Personal', 'Promotions', 'Personal',
        'Work', 'Work'
    ]
}
df = pd.DataFrame(data)

# ----------------------
# 🧠 2. Train the Classifier
# ----------------------
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['email'])
y = df['label']

model = MultinomialNB()
model.fit(X, y)

# ----------------------
# 🎨 3. Streamlit UI
# ----------------------
st.set_page_config(page_title="Email Classifier", layout="centered")

st.title("📧 Email Classifier")
st.write("Paste an email message below to automatically categorize it.")

email_input = st.text_area("✉️ Enter email content here:", height=200)

if st.button("Classify"):
    if email_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        test_X = vectorizer.transform([email_input])
        prediction = model.predict(test_X)[0]
        st.success(f"📂 **Predicted Category:** `{prediction}`")
