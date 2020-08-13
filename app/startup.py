from flask import Flask

from app.controllers.DB2Controller import blueprint as db2_blueprint
app = Flask(__name__)
app.register_blueprint(db2_blueprint, url_prefix="/db2")


@app.route('/')
def hello_world():
    return 'whistle!'


if __name__ == '__main__':
    app.run(debug=True)