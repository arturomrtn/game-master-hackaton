# app.py - Microservicio de combate para Knave (Flask)

from flask import Flask, request, jsonify
from combat import simulate_combat

app = Flask(__name__)

@app.route("/combat", methods=["POST"])
def combat():
    data = request.get_json()
                                                            
    try:
        result = simulate_combat(
            player=data["player"],
            enemy=data["enemy"]
        )
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
