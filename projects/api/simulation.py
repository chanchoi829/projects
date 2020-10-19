"""REST API for running simulation."""
import os
import re
import flask
import projects
import subprocess
from subprocess import Popen, PIPE, STDOUT
import sys
import socket
import time
from io import StringIO


PACKAGE_DIR = os.path.dirname(os.path.dirname(__file__))
SHIP_FILENAME = os.path.join(PACKAGE_DIR, 'static', 'ship')
OUTPUT_FILENAME = os.path.join(PACKAGE_DIR, 'var', 'sim_output.txt')
OUTPUT = open(OUTPUT_FILENAME, "w")


@projects.app.route('/api', methods=["GET"])
def run_simulation():
    """Run simulation."""
    proc = subprocess.Popen([SHIP_FILENAME], bufsize = 1, universal_newlines=1, stdin=PIPE, stdout=OUTPUT)
        # Setup a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 3000))

    sock.listen(5)
    sock.settimeout(1)

    while True:
        time.sleep(0.25)
        try:
            clientsocket, address = sock.accept()
        except socket.timeout:
            continue

        message_chunks = []

        # While loop for reading a client's message if
        # this server receives one
        while True:
            time.sleep(0.25)
            data = clientsocket.recv(4096)
            if not data:
                break

            message_chunks.append(data)

        # Decode data into a json file
        message_bytes = b''.join(message_chunks)
        message_str = message_bytes.decode("utf-8")
        command = ""
        entered = False
        for a in message_str:
            if a is ":":
                entered = True
            elif a is not "}" and entered and a is not "\"":
                command += a
        command += "\n"
        proc.stdin.write(command)
        f = open(OUTPUT_FILENAME, "r")
        sock_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_send.connect(("localhost", 6000))
        sock_send.sendall(f.read().encode("utf-8"))

    return "Finished"
