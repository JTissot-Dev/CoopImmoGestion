from flask import render_template


def page_forbidden(e):
    return render_template('403.html'), 403

