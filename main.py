#!/usr/bin/env python

import flask
import logging
from pathlib import Path
import random

log = logging.getLogger(__name__)

app = flask.Flask(__name__)

def choose_image():
    images = list(Path("static/images").glob("*.jpg"))
    log.info(f"images: {images}")
    img = random.choice(images)
    return img

@app.route('/')
def home():
    img = choose_image()
    return flask.render_template('home.html', pic=img)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='localhost', port=8080, debug=True)
