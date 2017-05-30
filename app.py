import os
from subprocess import Popen

from flask import Flask

app = Flask(__name__)

PROGRAM_PROCESS = None

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/start/<string:name>")
def enable(name):
    global PROGRAM_PROCESS

    if PROGRAM_PROCESS:
        PROGRAM_PROCESS.terminate()

    program = os.getcwd() + '/programs/' + name + '.py'

    if not os.path.isfile(program):
        return "program not found", 404

    PROGRAM_PROCESS = Popen(['/usr/local/bin/python3', program])

    return "ok", 200


@app.route("/stop")

def disable():
    global PROGRAM_PROCESS
    if PROGRAM_PROCESS:
        PROGRAM_PROCESS.terminate()
    return "disabled", 200


if __name__ == "__main__":
    app.run()
