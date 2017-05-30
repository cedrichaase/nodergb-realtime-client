from subprocess import Popen


def run(name):
    Popen(['python3', name])