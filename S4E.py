from flask import Flask, request, render_template, jsonify
import subprocess
import re
from prompt import prompt

app = Flask(__name__)

MODEL_NAME = "llama3"  # Model adını tek bir yerde tanımlayın

def run_model(prompt):
    print("Model çalıştırılıyor:", prompt)
    command = f'ollama run {MODEL_NAME} "{prompt}"'
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        stdout = result.stdout.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print("Komut çalıştırılırken hata oluştu:", e.stderr.decode("utf-8"))
        return None

    print("Model yanıtı:", stdout)
    return stdout



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    user_prompt = request.form.get("prompt")
    if not user_prompt:
        return "Prompt boş olamaz.", 400

    full_prompt = prompt(user_prompt)
    print("Tam Prompt:", full_prompt)
    model_response = run_model(full_prompt)

    if model_response is None:
        return "Model çalıştırılırken bir hata oluştu.", 500

    return render_template("index.html", response=model_response, prompt=user_prompt)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)