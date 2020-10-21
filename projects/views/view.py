"""View file."""
import flask
import projects
import os


PACKAGE_DIR = os.path.dirname(os.path.dirname(__file__))
SIMULATION_HTML = os.path.join(PACKAGE_DIR, "templates", "simulation.html")


@projects.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Display / route."""
    context = {}
    return flask.render_template("simulation.html", **context)
