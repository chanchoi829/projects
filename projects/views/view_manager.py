"""View file."""
import flask
import projects
import os


PACKAGE_DIR = os.path.dirname(os.path.dirname(__file__))
MANAGER_HTML = os.path.join(PACKAGE_DIR, "templates", "manager.html")


@projects.app.route('/manager', methods=['GET', 'POST'])
def show_manager():
    """Display / route."""
    context = {}
    return flask.render_template('manager.html', **context)
