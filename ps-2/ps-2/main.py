from validator import validate_payload
from calculations import factorial
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/factorial', methods = ["GET"])
def cal_factorial():
    try:
        data = request.json
        is_valid = validate_payload(data)
        if isinstance(is_valid, bool):
            return jsonify({
                "factorial": factorial(data["value"])
            })
        else:
            return jsonify(is_valid)
    except Exception as e:
        return jsonify({
            "status": 400, 
            "message": "Some error occurred. Please try again! ",
            "description": str(e)
        })

if __name__ == '__main__':
    app.run()
