"""REST API for running simulation."""
import os
import re
import flask
import projects
import subprocess
import sys


PACKAGE_DIR = os.path.dirname(os.path.dirname(__file__))
SHIP_FILENAME = os.path.join(PACKAGE_DIR, 'api', 'ship')


@projects.app.route('/', methods=["GET"])
def run_simulation():
    """Run simulation."""
    with subprocess.Popen([SHIP_FILENAME], stdout=subprocess.PIPE) as proc:
        return(proc.stdout.read())
    return "Finished"
