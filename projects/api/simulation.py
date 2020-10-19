"""REST API for running simulation."""
import os
import re
import flask
import projects
import subprocess
import sys
import socket


PACKAGE_DIR = os.path.dirname(os.path.dirname(__file__))
SHIP_FILENAME = os.path.join(PACKAGE_DIR, 'static', 'ship')


@projects.app.route('/api', methods=["GET"])
def run_simulation():
    """Run simulation."""
    # Setup a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 3000))

    sock.listen(5)
    sock.settimeout(1)
    print('before while')
    while True:
        try:
            clientsocket, address = sock.accept()
        except socket.timeout:
            continue

        message_chunks = []

        # While loop for reading a client's message if
        # this server receives one
        while True:
            data = clientsocket.recv(4096)
            if not data:
                break

            message_chunks.append(data)

        # Decode data into a json file
        message_bytes = b''.join(message_chunks)
        message_str = message_bytes.decode("utf-8")
        print( message_str + 'received')
        send_message = message_str
        sock_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_send.connect(("localhost", 6000))
        sock_send.sendall(send_message.encode('utf-8'))

    with subprocess.Popen([SHIP_FILENAME], stdout=subprocess.PIPE) as proc:
        return(proc.stdout.read())
    return "Finished"
