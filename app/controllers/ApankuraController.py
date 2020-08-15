from flask import Blueprint, render_template, abort, request, jsonify
import ibm_db_dbi as db
import requests
import logging

blueprint = Blueprint('apankura_blueprint', __name__)


@blueprint.route('/service/liveness', methods=['GET'])
def service_liveness():
    host = request.args.get('host')
    port = request.args.get('port')
    target = "http://{}:{}/apankura/liveness".format(host, port)
    response = dict()
    response["target"] = target
    try:
        logging.info("connect to {}".format(target))
        response = requests.get(target)
        if response.status_code != 200:
            raise ValueError(target)
        return jsonify(response)
    except Exception as e:
        raise ValueError(target) from e


@blueprint.route('/pods/liveness', methods=['GET'])
def pods_liveness():
    pods = request.args.get('pods')
    port = request.args.get('port')
    hosts = pods.split(",")
    response = dict()
    response["target"] = pods
    try:
        for host in hosts:
            target = "http://{}:{}/apankura/liveness".format(host, port)
            logging.info("connect to {}".format(target))
            response = requests.get(target)
            if response.status_code != 200:
                raise ValueError(target)
        return jsonify(response)
    except Exception as e:
        raise ValueError(hosts) from e

