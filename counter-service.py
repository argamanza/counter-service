#!flask/bin/python
from flask import Flask, request
import os

app = Flask(__name__)
counter = 0
counter_file = "/app/data/counter.txt"


def counter_read():
    try:
        with open(counter_file, "r") as f:
            return f.readline().strip()
    except IOError:
        print("Counter file not accessible or missing, returning 0")
        return 0


def counter_increment():
    os.makedirs(os.path.dirname(counter_file), exist_ok=True)
    if not os.path.exists(counter_file):
        print("Counter file doesn't exist, creating new one.")
        with open(counter_file, "w") as f:
            f.write("1")
    else:
        current = int(counter_read())

        with open(counter_file, "w") as f:
            f.write(str(current + 1))

    print(f"Incremented counter to {counter_read()}")


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        counter_increment()

    return str(f"Our counter is: {counter_read()} ")


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
