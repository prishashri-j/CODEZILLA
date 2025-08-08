# 🐉 Codezilla

Codezilla is a Python-based project designed to bring together powerful scripts, utilities, and solutions under one repository.  
It’s built with clarity, modularity, and reusability in mind — making it easy to extend and adapt for various use cases.

---

## 📂 Project Structure
creative-translator/
│
├── app.py                 # Main Flask backend
├── .env                   # Stores API key securely
├── requirements.txt       # Python dependencies
│
├── templates/
│    └── index.html        # Frontend UI

3. Requirements
Before running, ensure you have:
Python 3.8+ installed
pip package manager
OpenRouter API key from: https://openrouter.ai

5. How It Works
User enters text in the input box.
Selects:
Source Language (e.g., English)
Target Language (e.g., French)
Creative Style (e.g., Poetic, Formal, Humorous)
Backend sends a request to OpenRouter API with style instructions.
API returns translated + styled text.
Output is displayed instantly in the browser.


