from flask import Flask
import logging
import sys
from app.controllers.DB2Controller import blueprint as db2_blueprint
from app.controllers.ApankuraController import blueprint as apankura_blueprint

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

app = Flask(__name__)
app.register_blueprint(db2_blueprint, url_prefix="/db2")
app.register_blueprint(apankura_blueprint, url_prefix="/apankura")


@app.route('/')
def hello_world():
    return 'whistle!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)