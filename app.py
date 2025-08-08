import os
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    user_input = request.form.get("text")
    source_lang = request.form.get("source_lang")
    target_lang = request.form.get("target_lang")
    target_style = request.form.get("style")

    if not OPENROUTER_API_KEY:
        return render_template("index.html", translated_text="❌ API key missing.", user_input=user_input)

    if not source_lang or not target_lang or not target_style:
        return render_template("index.html", translated_text="⚠️ Please select all options.", user_input=user_input)

    # Build a smart prompt
    prompt = (
        f"Translate the following text from {source_lang} to {target_lang}, and rewrite it in a {target_style} style. "
        f"Ensure the original meaning and tone are preserved:\n\n"
        f"{user_input}"
    )

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "system", "content": "You are a creative multilingual translator with a deep understanding of tone and style."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        translated = result['choices'][0]['message']['content']
    else:
        translated = f"❌ Error {response.status_code}: {response.text}"

    return render_template(
        "index.html",
        translated_text=translated,
        user_input=user_input,
        source_lang=source_lang,
        target_lang=target_lang,
        style=target_style
    )

if __name__ == "__main__":
    app.run(debug=True)
