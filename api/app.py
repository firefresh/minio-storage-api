# -*- coding: utf-8; -*-
from flask import Flask, request, jsonify, current_app
from utils import logger
from logic import implementation as imple
from logic.implementation import save_file, get_file, remove_file
import os


logger = logger.get_logger('app')

app = Flask(__name__)

@app.get("/alive")
def is_alive():
    logger.info('INIT is_alive')
    return "Is alive!"


@app.post("/fm/save_file")
def save_file():
    logger.info('INIT save_file [POST]')
    file = request.files.get("file")
    name = file.filename
    object_name = imple.save_file(file, name)
    logger.info('END save_file, [POST]')
    return jsonify(result=True, message={'id':object_name}), 200


@app.get("/fm/get_file/<object_name>")
def get_file(object_name):
    logger.info('INIT get_file [GET]')
    data = imple.get_file(object_name)
    logger.info('END get_file [GET]')
    return jsonify(result=True, message={'file':data}), 200


@app.delete("/fm/remove_file/<object_name>")
def remove_file(object_name):
    logger.info('INIT remove_file [DELETE]')
    imple.remove_file(object_name)
    logger.info('END remove_file [DELETE]')
    return jsonify(success=True, result="La operacion se ha realizado con exito"), 200

def init():
    logger.info('INIT')
    app.debug = True
    app.app_context().push()
    app.run("0.0.0.0", os.getenv("APP_PORT", 5004))

if __name__ == '__main__':
    init()