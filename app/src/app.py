from crypt import methods
from flask import Flask, request, Response
import json


app = Flask(__name__)


@app.route('/api/echo', methods=['POST'])
def hello_world():
    data = request.json
    return Response(response=json.dumps(data), status=200, mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
