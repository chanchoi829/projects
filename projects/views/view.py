"""View file."""
import flask
import projects


@projects.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Display / route."""
    context = {}
    return flask.render_template('simulation.html', **context)
