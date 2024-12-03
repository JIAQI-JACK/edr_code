# encoding=utf8
# author: sophia
# create_time: 2024/12/02 10:58
# file: main_api.py
import time
from flask import Blueprint, request
from app.api.api_utils import catch_api_exception
from app.api.api_msg import ApiResponseError, api_status_msg

main_bp = Blueprint("main", __name__)


@main_bp.route('/info', methods=['GET', 'POST'])
@catch_api_exception()
def reformat():

    result = {
        "time": time.time(),
    }
    return result
