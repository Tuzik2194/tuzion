from flask import Flask, send_from_directory
import json

app = Flask(__name__)

def load_text():
    with open("data/text.json", "r", encoding="utf-8") as f:
        return json.load(f)

def render_page(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    text = load_text()

    for key, value in text.items():
        html = html.replace(f"${{{key}}}", str(value))

    return html

@app.route("/")
def home():
    return render_page("main_page/index.html")

@app.route("/games")
def games():
    return render_page("games_page/index.html")

@app.route("/games/minesweeper")
def minesweeper():
    return render_page("games/minesweeper/index.html")

@app.route("/weather")
def weather():
    return render_page("weather_page/index.html")

@app.route("/dev")
def dev():
    return render_page("dev_page/index.html")

@app.route("/rules")
def rules():
    return render_page("rules_page/index.html")

# стилі
@app.route("/main_page/style.css")
def main_style():
    return send_from_directory("main_page", "style.css")

@app.route("/games_page/style.css")
def games_style():
    return send_from_directory("games_page", "style.css")

@app.route("/games/minesweeper/style.css")
def minesweeper_style():
    return send_from_directory("games/minesweeper", "style.css")

@app.route("/weather_page/style.css")
def weather_style():
    return send_from_directory("weather_page", "style.css")

@app.route("/dev_page/style.css")
def dev_style():
    return send_from_directory("dev_page", "style.css")

@app.route("/rules_page/style.css")
def rules_style():
    return send_from_directory("rules_page", "style.css")

# скрипт
@app.route("/script.js")
def script():
    return send_from_directory("data", "script.js")

# 🔊 ЗВУКИ (НОВЕ)
@app.route("/sounds/<game>/<filename>")
def sounds(game, filename):
    return send_from_directory(f"data/sounds/{game}", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
