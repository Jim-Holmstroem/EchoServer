from flask import Flask, request


app = Flask('EchoServer')


@app.route("/", methods=['GET', 'POST'])
def echo():
    return str(request.data)

if __name__ == '__main__':
    """
    usage: python main.py <port>
    """
    import sys
    app.run(port=int(sys.argv[1]))
