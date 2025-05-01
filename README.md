# 🧠 Webpage Q&A App using Langchain + Google Gemini

This app allows you to enter any webpage URL and ask questions based on its content.  
It uses **Langchain**, **Google Gemini**, and **Streamlit**, and supports JavaScript-rendered pages using Selenium.

---

## 🚀 How to Run This App

1. **Clone the repository**:

   ```bash
   git clone https://github.com/siddique0786/Ask_Questions_from_Any_Webpage.git
   cd your-repo-name

2. **Create a virtual environment**: 
      ```bash
      python -m venv venv
      source venv/bin/activate 
              or 
      On Windows: venv\Scripts\activate

3. **Install the required packages**: 
    ```bash
       pip install -r requirements.txt

4. **Make sure you have a .env file with your Gemini API key**:
      ```bash
      GEMINI_API_KEY=your_google_gemini_api_key

5. **Run the app**:
     ```bash
     streamlit run app.py

