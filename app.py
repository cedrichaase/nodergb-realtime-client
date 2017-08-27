import os
from subprocess import Popen

from flask import Flask
from flask import request
from flask import jsonify
from flask import Blueprint
from flask_cors import CORS, cross_origin

app = Flask(__name__)

ctrl = Blueprint("ctrl", __name__)
mgmt = Blueprint("mgmt", __name__)


PROGRAM_PROCESS = None
PROGRAM_PATH = os.getcwd() + '/programs/'

def __get_program_path(name):
    return PROGRAM_PATH + name + '.py'

def __get_running_program():
    """
    :return: The name of the program that is currently running 
    """
    return PROGRAM_PROCESS.args[1].split('/')[-1][:-3] if PROGRAM_PROCESS else ""


def __stop_running_program():
    global PROGRAM_PROCESS
    if PROGRAM_PROCESS:
        PROGRAM_PROCESS.kill()
        PROGRAM_PROCESS = None


def __start_running_program(name):
    global PROGRAM_PROCESS
    global PROGRAM_PATH

    if PROGRAM_PROCESS:
        __stop_running_program()

    program = PROGRAM_PATH + name + '.py'

    PROGRAM_PROCESS = Popen(['/usr/bin/env', 'python3', program])


@app.route("/")
def hello():
    return "Hello World!"


@ctrl.route("/program")
def get_running_program():
    """
    Return the name of the program that is currently running
    
    :return: the name of the program
    """
    program = __get_running_program()

    if not program:
        return "", 204

    return jsonify(program), 200


@ctrl.route("/program/<string:name>", methods=['PUT'])
def set_running_program(name):
    """
    Start execution of the program with given name
    
    :param name: name of the program to execute 
    :return: 
    """
    program = __get_program_path(name)

    if not os.path.isfile(program):
        return jsonify("program not found"), 404

    __start_running_program(name)

    return jsonify(__get_running_program()), 200


@ctrl.route("/program/", methods=['PUT'])
def stop_running_program():
    """
    Terminates the program that is currently running
    
    :return: 
    """
    global PROGRAM_PROCESS
    __stop_running_program()
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


@mgmt.route("/program/<string:name>", methods=['GET'])
def get_program(name):
    program_path = __get_program_path(name)

    if not os.path.isfile(program_path):
        return jsonify("program not found"), 404

    with open(program_path, 'r') as program_file:
        program_content = program_file.read()

        if name == __get_running_program():
            __stop_running_program()

        return jsonify({
            'content': program_content,
            'name': name
        }), 200


@mgmt.route("/program/<string:name>", methods=['PUT'])
def update_program(name):
    body = request.get_json()
    program_path = __get_program_path(name)
    new_program_path = program_path

    if not os.path.isfile(program_path):
        return jsonify("program not found"), 404

    if 'name' in body and body["name"] != name:
        new_name = body["name"]

        new_program_path = __get_program_path(new_name)
        if os.path.isfile(new_program_path):
            return jsonify("program with that name exists already"), 400

        os.rename(program_path, new_program_path)
        os.remove(program_path)

    with open(program_path, 'w') as program_file:
        program_file.write(body["content"])

        return jsonify({
            'content': body["content"]
        }), 200


@mgmt.route("/program/<string:name>", methods=['POST'])
def add_program(name):
    body = request.get_json()
    program_path = __get_program_path(name)

    if os.path.isfile(program_path):
        return jsonify("program with that name exists already"), 400

    with open(program_path, 'w+') as program_file:
        program_file.write(body["content"])

        return jsonify({
            'content': body["content"]
        }), 201


@mgmt.route("/program/<string:name>", methods=['DELETE'])
def delete_program(name):
    program_path = __get_program_path(name)

    if not os.path.isfile(program_path):
        return jsonify("program not found"), 404

    os.remove(program_path)

    return jsonify(), 204


app.register_blueprint(ctrl, url_prefix="/ctrl")
app.register_blueprint(mgmt, url_prefix="/mgmt")
CORS(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
