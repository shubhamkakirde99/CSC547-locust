from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    i = 0
    for i in range(100000000):
        i += 1
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
