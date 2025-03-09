from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/test')
def test_api():
    return jsonify({'message': 'Backend is running!'})

if __name__ == '__main__':
    app.run(debug=True)
