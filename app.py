from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/dataUsage/<user_id>", methods=["GET"])
def data_usage():
    user_id = request.args.get("user_id")
 
    return jsonify({
        "plan": "Monthly 10GB",
        "total_data_mb": 10240,
        "used_data_mb": 7345,
        "remaining_data_mb": 2895,
        "renewal_date": "2025-06-01"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
