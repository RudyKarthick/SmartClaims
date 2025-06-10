from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze_claim():
    data = request.get_json()
    summary = data.get('summary', '')

    if not summary:
        return jsonify({'error': 'No summary provided'}), 400

    blob = TextBlob(summary)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    summary_lower = summary.lower()

    # Determine claim priority
    if polarity < -0.3:
        priority = "High"
    elif polarity < 0.3:
        priority = "Medium"
    else:
        priority = "Low"

    # Determine fraud risk
    fraud_risk = "High" if subjectivity > 0.8 else "Low"

    # Determine suggested action
    if "hospital" in summary_lower:
        action = "Investigate hospital records"
    elif "police report" in summary_lower or "police" in summary_lower:
        action = "Verify police report"
    elif "doctor" in summary_lower or "clinic" in summary_lower:
        action = "Request medical documentation"
    else:
        action = "Request more info"

    result = {
        "priority": priority,
        "fraudRisk": fraud_risk,
        "suggestedAction": action
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)
