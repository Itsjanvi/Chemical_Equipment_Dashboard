from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    # Flask default 'templates' folder mein index.html dhoondta hai
    return render_template("index.html")

@app.route("/api/telemetry")
def get_telemetry():
    return jsonify({
        "reactor_temp": round(random.uniform(280.0, 350.0), 2),
        "pressure": round(random.uniform(40.0, 60.0), 2),
        "flow_rate": round(random.uniform(100.0, 200.0), 2),
        "vibration": round(random.uniform(1.0, 5.0), 2),
        "corrosion_index": round(random.uniform(0.01, 0.2), 3),
        "chart_values": [random.randint(290, 330) for _ in range(7)]
    })

if __name__ == "__main__":
    app.run(debug=True, port=5005)