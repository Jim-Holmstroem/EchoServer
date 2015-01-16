import os

from flask import Flask, request
app = Flask('EchoServer')


@app.route("/", methods=['POST', ])
def echo():
    return request.get_data()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
    )
