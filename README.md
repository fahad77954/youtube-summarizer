# 🎥 AI-Powered YouTube Video Summarizer

A lightning-fast web application built with **Python** and **Streamlit** that extracts transcripts from YouTube videos and generates comprehensive, concise summaries using the **Groq API**.

---

## 🚀 Features

* **Instant Transcript Extraction:** Automatically pulls transcripts from YouTube URLs.
* **High-Speed AI Summarization:** Powered by Groq's ultra-fast LLM inference to deliver insights in seconds.
* **Clean & Interactive UI:** Built using Streamlit for an effortless and responsive user experience.
* **Secure Credential Handling:** Utilizes Streamlit Secrets to safely manage API keys in production.

---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Language:** Python
* **AI/LLM Inference:** Groq SDK
* **Transcript Parsing:** YouTube Transcript API

---

## 💻 Local Installation & Setup

If you want to clone and run this project locally on your machine, follow these simple steps:

### 1. Clone the Repository

```bash
git clone https://github.com/fahad77954/youtube-summarizer.git
cd youtube-summarizer

```

### 2. Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt

```

### 3. Configure Your Secrets

Create a `.streamlit` directory in your root folder and add a `secrets.toml` file to store your API key securely:

```toml
GROQ_API_KEY = "your_groq_api_key_here"

```

### 4. Run the App Locally

Start the local Streamlit development server:

```bash
streamlit run u_tube_summarizer.py

```

---

## 📂 Project Structure

```text
youtube-summarizer/
├── u_tube_summarizer.py    # Main Streamlit application script
├── requirements.txt        # Python package dependencies
├── .gitignore              # Excluded cache and secret files
└── README.md               # Project documentation

```
