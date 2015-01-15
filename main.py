from flask import Flask, request


app = Flask('EchoServer')


@app.route("/", methods=['GET', 'POST'])
def echo():
    return request.data

if __name__ == '__main__':
    """
    usage: python main.py <port>
    """
    import sys
    app.run(port=sys.argv[1])
