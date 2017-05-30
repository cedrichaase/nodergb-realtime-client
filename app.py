import os
from subprocess import Popen

from flask import Flask
from flask import jsonify
from flask import Blueprint

app = Flask(__name__)

ctrl = Blueprint("ctrl", __name__)
mgmt = Blueprint("mgmt", __name__)


PROGRAM_PROCESS = None
PROGRAM_PATH = os.getcwd() + '/programs/'


def get_running_program():
    """
    :return: The name of the program that is currently running 
    """
    return PROGRAM_PROCESS.args[1].split('/')[-1][:-3] if PROGRAM_PROCESS else ""


def stop_running_program():
    global PROGRAM_PROCESS
    if PROGRAM_PROCESS:
        PROGRAM_PROCESS.terminate()
        PROGRAM_PROCESS = None


@app.route("/")
def hello():
    return "Hello World!"


@ctrl.route("/program")
def get_program():
    """
    Return the name of the program that is currently running
    
    :return: the name of the program
    """
    program = get_running_program()

    if not program:
        return "", 204

    return jsonify(program), 200


@ctrl.route("/program/<string:name>", methods=['PUT'])
def set_program(name):
    """
    Start execution of the program with given name
    
    :param name: name of the program to execute 
    :return: 
    """
    global PROGRAM_PROCESS
    global PROGRAM_PATH

    if PROGRAM_PROCESS:
        stop_running_program()

    program = PROGRAM_PATH + name + '.py'

    if not os.path.isfile(program):
        return jsonify("program not found"), 404

    PROGRAM_PROCESS = Popen(['/usr/local/bin/python3', program])

    return jsonify(get_running_program()), 200


@ctrl.route("/program", methods=['PUT'])
def stop_program():
    """
    Terminates the program that is currently running
    
    :return: 
    """
    global PROGRAM_PROCESS
    stop_running_program()
    return "", 204


@mgmt.route("/programs")
def get_programs():
    """
    Returns a list of available programs
    
    :return:
    """
    global PROGRAM_PATH
    programs = [x[0:-3] for x in os.listdir(PROGRAM_PATH) if x.endswith('.py')]
    return jsonify(programs), 200


app.register_blueprint(ctrl, url_prefix="/ctrl")
app.register_blueprint(mgmt, url_prefix="/mgmt")

if __name__ == "__main__":
    app.run()
