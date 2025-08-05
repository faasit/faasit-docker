from flask import Flask, request, jsonify, make_response
import requests

app = Flask(__name__)

@app.post("/")
def forward():
    data = request.json()
    url = data['url']
    payload = data['data']

    resp = requests.post(url, data=payload)
    return make_response(resp.content, resp.status_code, resp.headers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)