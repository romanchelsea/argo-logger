from flask import Flask, request

app = Flask(__name__)


@app.route('/argoDeployment', methods=['POST'])
def post_data():
    if request.method == 'POST':
        data = request.json
        print("Received data: ", data)
        return "Data received successfully", 200
    else:
        return "Invalid request method", 405


if __name__ == '__main__':
    app.run(debug=True)
