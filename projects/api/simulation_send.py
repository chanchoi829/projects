"""REST API for sending/receving."""
import os
import re
import flask
import projects
import subprocess
import sys
import socket
import time


PACKAGE_DIR = os.path.dirname(os.path.dirname(__file__))
OUTPUT_FILENAME = os.path.join(PACKAGE_DIR, 'var', 'sim_output.txt')


@projects.app.route('/api/simulation/<string:command>', methods=["GET"])
def recv_send(command):
    """Receive send receive."""
    context = {}
    # Setup a socket for sending a register message
    sock_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    sock_send.connect(("localhost", 3000))
    # Setup a socket to for receiving a message from the master
    sock_recv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_recv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_recv.bind(('localhost', 6000))
    sock_recv.listen(5)
    sock_recv.settimeout(1)

    # Send a register message
    register_message = '{"command": "'+ command + '"}'
    sock_send.sendall(register_message.encode('utf-8'))
    sock_send.close()
    while True:
        time.sleep(0.2)
        try:
            master_socket, address = sock_recv.accept()
        except socket.timeout:
            continue

        message_chunks = []

        while True:
            time.sleep(0.2)
            data = master_socket.recv(4096)
            if data:
                # Decode data into a json file
                message_chunks.append(data)
                message_bytes = b''.join(message_chunks)
                message_str = message_bytes.decode("utf-8")
                context = {}
                if message_str == "Quit":
                    context["output"] = "Click to continue"
                else:
                    f = open(OUTPUT_FILENAME, "r")
                    context["output"] = f.read()
                    f.close()
                return flask.jsonify(**context)

    return flask.jsonify(**context)
