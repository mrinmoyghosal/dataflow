# compose_flask/app.py
from flask import Flask
from mgq import MgqClient


app = Flask(__name__)


@app.route('/')
def hello():
    client = MgqClient("tcp://broker:5555")
    response = ""
    for i in range(10000):
        response += "," + client.send_message("work", "hello"+str(i))
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9080, debug=True)
