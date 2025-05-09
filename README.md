# 🎭 Emotion Detector Web App

This is a dynamic and lightweight web application that analyzes the **emotional tone** of any text using the **NRCLex** lexicon. It is built using **Flask** and deployed as a real-time emotion detection tool. Great for analyzing sentiments in messages, feedback, or social media posts!

---

## 🚀 Features

- 🔍 Accepts **user input at runtime**
- 🧠 Uses **NRCLex** for emotion detection
- 📊 Displays **top emotions** and complete **emotion scores**
- 💻 Fully **dynamic web interface** with live form processing
- 🌈 Styled with a modern and clean UI (CSS included)
- ⚙️ Lightweight and easy to deploy

---

## 📸 Screenshots

| Input Screen | Emotion Output |
|--------------|----------------|
| ![Input](https://github.com/Mohanrajx/Image/blob/3025e70dd9f4ad2401acae30441f30f09bd61c44/ip.png) | ![Output](https://github.com/Mohanrajx/Image/blob/3deb90c4d0326410f1b436090a55cb312e175e1e/op.png) |

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Python, Flask
- **NLP:** NRCLex (based on NRC Emotion Lexicon)
- **Deployment:** Localhost or Render/Heroku (optional)

---

## 🧪 How It Works

1. Enter any sentence in the text box.
2. Click “Analyze”.
3. The app processes the input using NRCLex and returns:
   - Top 2–3 detected emotions
   - All emotion scores in a list

---

## 🗂️ Project Structure

```

Mohanrajx/ntest/
├── app.py                 # Main Flask backend
├── requirements.txt       # Dependencies
├── templates/
│   └── index.html         # HTML layout
├── static/
│   └── style.css          # UI styling

````

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/your-username/emotion-detector-web.git
cd emotion-detector-web
````

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate   # or venv\\Scripts\\activate on Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

### 4️⃣ Run the App

```bash
python app.py
```

Visit 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📚 About NRCLex

NRCLex is a Python library based on the NRC Emotion Lexicon developed by the National Research Council of Canada. It categorizes English words into 8 primary emotions:

* Joy, Trust, Fear, Surprise, Sadness, Disgust, Anger, Anticipation

---

## 🧠 Future Enhancements

* [ ] Add emotion score **visual charts**
* [ ] Enable **multilingual input**
* [ ] Add **streaming API** for chatbot integration
* [ ] Live frontend update using **JavaScript/AJAX**

---

## 👨‍💻 Author

- **G Mohanraj**
   - Department of AI & DS
   📧 [gm@iitm.ac.in](mailto:gm@kingston.ac.in)
---

