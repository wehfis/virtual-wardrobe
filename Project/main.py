from flask_login import login_required

from website import create_app
from flask import Flask, render_template

app = create_app()

@app.errorhandler(400)
@login_required
def bad_request_error(error):
    description = "The server cannot or will not process the request due to an apparent client error."
    error_code = "400"
    return render_template('error.html', error=error, description=description), 400


@app.errorhandler(401)
@login_required
def unauthorized_error(error):
    description = "The request has not been applied because it lacks valid authentication credentials for the target resource."
    error_code = "401"
    return render_template('error.html', error=error, description=description), 401


@app.errorhandler(403)
@login_required
def forbidden_error(error):
    description = "The server understood the request but refuses to authorize it."
    error_code = "403"
    return render_template('error.html', error=error, description=description), 403


@app.errorhandler(404)
@login_required
def not_found_error(error):
    description = "The requested resource could not be found but may be available in the future."
    error_code = "404"
    return render_template('error.html', error_code=error_code ,error=error, description=description), 404


@app.errorhandler(Exception)
@login_required
def handle_error(error):
    description = "An unexpected error occurred."
    error_code = "UNKNOWN"
    return render_template('error.html', error=error, description=description), 500


# turn off in production
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
