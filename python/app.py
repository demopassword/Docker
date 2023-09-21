from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/healthz')
def healthz():
    return jsonify(status='ok')

@app.route('/version')
def version():
    return jsonify(api_version='v1')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)