# 📝 Quiz Application

A simple and interactive **Quiz Application** built with **Python**, **UV**, and **Streamlit**.  
This app presents random questions about Pakistan and provides instant feedback on whether your answer is correct or not.  

---

## ✨ **Features**
- 🎯 **Random Questions**: Each round displays a random question.  
- 🖱️ **Multiple Choice Options**: Easy selection using radio buttons.  
- ⚡ **Instant Feedback**: Get **correct/incorrect** responses immediately.  
- 🔄 **Auto-Refresh**: New questions load automatically after 5 seconds.  
- 🌐 **Web Interface**: Powered by **Streamlit** for an interactive experience.

---

## 🛠 **Tech Stack**
- **Python 3.x** 🐍  
- **Streamlit** (for the web interface)  
- **UV** (for environment and dependency management)  

---

## ⚙️ **Installation & Setup**

### **1. Initialize a UV Environment**
```bash
uv init
````

### **2. Install Streamlit**

```bash
uv add streamlit
```

### **3. Activate the Virtual Environment**

```bash
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Mac/Linux
```

---

## 🚀 **Run the Application**

```bash
uv run streamlit run app.py
```

This will open the quiz in your default browser at:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 📂 **Project Structure**

```
quiz-app/
│── app.py        # Main application file
│── README.md     # Documentation
```

## 🎮 **How to Play**

1. A random question will appear with multiple-choice options.
2. Select your answer and click **"Submit Answer"**.
3. Get instant feedback (✅ Correct / ❌ Incorrect).
4. A new random question will load automatically after **5 seconds**.
