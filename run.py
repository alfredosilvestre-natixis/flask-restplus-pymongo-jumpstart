import app

from flask import redirect

application = app.App.create_app(flask_config_name='production')


@application.route("/")
def index():
    return redirect('/api/')


if __name__ == '__main__':
    application.run()
