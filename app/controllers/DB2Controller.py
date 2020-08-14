from flask import Blueprint, render_template, abort, request, jsonify
import ibm_db_dbi as db

blueprint = Blueprint('db2_blueprint', __name__)


@blueprint.route('/connect', methods=['GET'])
def connect():
    database = request.args.get('database') or "sutdb"
    host = request.args.get('host') or "localhost"
    port = request.args.get('port') or "50000"
    username = request.args.get('username') or "db2inst1"
    password = request.args.get('password') or "admin123"
    cs = "DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;QUERYTIMEOUT=10;CONNECTIONTIMEOUT=10;UID={};PWD={};".format(
        database, host, port, username, password)

    conn = None
    try:
        print("connect to {}".format(cs))
        conn = db.connect(cs, "", "")
        cursor = conn.cursor()
        cursor.execute("SELECT service_level FROM  TABLE(sysproc.env_get_inst_info()) as INSTANCEINFO")
        response = dict()
        for r in cursor.fetchall():
            response["version"] = r[0]
        return jsonify(response)
    except Exception as e:
        raise ValueError(cs) from e
    finally:
        if conn:
            try:
                conn.close()
            except Exception as ee:
                raise ValueError(cs) from ee








