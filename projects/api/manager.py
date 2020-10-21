"""REST API for running simulation."""
import os
import re
import flask
import projects
import subprocess
from subprocess import Popen, PIPE, STDOUT, run
import sys
import socket
import time


PACKAGE_DIR = os.path.dirname(os.path.dirname(__file__))
MANAGER_FILENAME = os.path.join(PACKAGE_DIR, 'static', 'c++', 'manager')
OUTPUT_FILENAME = os.path.join(PACKAGE_DIR, 'var', 'man_output.txt')


@projects.app.route('/api/manager', methods=["GET"])
def run_manager():
    """Run simulation."""
    output = open(OUTPUT_FILENAME, "w")
    proc = Popen([MANAGER_FILENAME], bufsize = 1, universal_newlines=1, stdin=PIPE, stdout=output)
        # Setup a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 2500))

    sock.listen(5)
    sock.settimeout(1)
    times = 0
    while True:
        time.sleep(0.2)
        try:
            clientsocket, address = sock.accept()
        except socket.timeout:
            continue

        message_chunks = []

        # While loop for reading a client's message if
        # this server receives one
        while True:
            time.sleep(0.2)
            data = clientsocket.recv(4096)
            if not data:
                break;

            message_chunks.append(data)

        # Decode data into a json file
        message_bytes = b''.join(message_chunks)
        message_str = message_bytes.decode("utf-8")
        command = ""
        entered = False
        for a in message_str:
            if a == ":":
                entered = True
            elif a != "}" and entered and a != "\"":
                command += a
        command += "\n"
        proc.stdin.write(command)
        f = open(OUTPUT_FILENAME, "r")
        sock_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_send.connect(("localhost", 2800))
        f.close()

        is_quit = ""
        for a in command:
            if a >= 'a' and a <= 'z':
                is_quit += a

        if is_quit == "qq":
            output.close()
            context = {}
            context["output"] = "Quit"
            sock_send.sendall("Quit".encode("utf-8"))
            return flask.jsonify(**context)
        else:
            sock_send.sendall("Done".encode("utf-8"))



    return "Finished"
