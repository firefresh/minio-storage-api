# -*- coding: utf-8; -*-
from minio import Minio
from minio.error import S3Error
from minio.error import InvalidResponseError
import os
from utils import logger
from datetime import datetime
import base64
import json

logger = logger.get_logger('implementation')

HOST=os.getenv('MINIO_HOST')
ACCESS_KEY=os.getenv('ACCESS_KEY')
SECRET_KEY=os.getenv('SECRET_KEY')
BUCKET_NAME=os.getenv('BUCKET_NAME')

client = client = Minio(
        HOST,
        access_key=ACCESS_KEY,
        secret_key=SECRET_KEY,
        secure=False
    )

if not client.bucket_exists(BUCKET_NAME):
    logger.info('Bucket not exists, creating...')
    client.make_bucket(BUCKET_NAME)
else:
    logger.info(f"Bucket {BUCKET_NAME} already exists")


def save_file(file_data, name):
    try:
        logger.info('INIT save_file')
        objectname = make_object_name(name)
        file_data.seek(0, os.SEEK_END)
        size = file_data.tell()
        file_data.seek(0,0)
        client.put_object(BUCKET_NAME, objectname, file_data, length=size)
        logger.info('END save_file')
        return objectname
    except InvalidResponseError as err:
        logger.exception(err)
    except Exception as ex:
        logger.exception(ex)


def get_file(objectname):
    try:
        logger.info('INIT get_file')
        response = client.get_object(BUCKET_NAME, objectname)
        response = base64.b64decode(response.data)
        logger.info('END get_file')
        return response
    except InvalidResponseError as err:
        logger.exception(err)
    except Exception as ex:
        logger.exception(ex)


def remove_file(objectname):
    try:
        logger.info('INIT remove_file')
        client.remove_object(BUCKET_NAME, objectname)
        logger.info('END remove_file')
    except InvalidResponseError as err:
        logger.exception(err)
    except Exception as ex:
        logger.exception(ex)

def make_object_name(name_string):
    try:
        object_name = str(name_string) + "-" + str(datetime.utcnow())
        object_name = base64.b64encode(object_name.encode("ascii"))
        object_name = object_name.decode("ascii") +"."+ name_string.split('.')[-1]
        logger.info(object_name)
        return object_name
    except Exception as ex:
        logger.exception(ex)