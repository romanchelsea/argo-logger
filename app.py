import logging
from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG,  # Set the logging level
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

@app.route('/argoDeployment', methods=['POST'])
def post_data():
    if request.method == 'POST':
        data = request.json
        print("Received data: ", data)
        logger.info("Received data: %s", data)
        return "Data received successfully", 200
    else:
        return "Invalid request method", 405


if __name__ == '__main__':
    app.run(debug=True)
