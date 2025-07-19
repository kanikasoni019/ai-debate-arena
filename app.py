from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    prompt = f"Analyze this debate argument:\n\n'{data['text']}'\n\nGive sentiment score (0–100), logic strength (0–100), and persuasion rating (0–100) as JSON."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4 if available
        messages=[{"role": "user", "content": prompt}]
    )
    content = response.choices[0].message.content
    try:
        result = eval(content.strip())
        return jsonify(result)
    except:
        return jsonify({"sentiment": 50, "logic": 50, "persuasion": 50})

if __name__ == "__main__":
    app.run(debug=True)
