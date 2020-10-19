"""
Package initializer.

"""
import flask

app = flask.Flask(__name__)  # pylint: disable=invalid-name

import projects.api  # noqa: E402  pylint: disable=wrong-import-position
import projects.views
