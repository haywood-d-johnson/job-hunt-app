from flask import Flask, jsonify
from api.jobs import jobs_bp

app = Flask(__name__)

app.register_blueprint(jobs_bp, url_prefix='/api/jobs')

@app.route('/api/test')
def test_api():
    return jsonify({'message': 'Backend is running!'})

if __name__ == '__main__':
    app.run(debug=True)
