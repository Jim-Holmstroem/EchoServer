from flask import Flask, request
app = Flask('EchoServer')


@app.route("/", methods=['POST', ])
def echo():
    return request.get_data()

if __name__ == '__main__':
    from os import environ as env
    import sys

    port = int(
        sys.argv[1] if len(sys.argv) > 1 else env.get('PORT') if 'PORT' in env else '5000'
    )

    app.run(
        host='0.0.0.0',
        port=port,
    )
