import os
import datetime
import requests
import json
from flask import make_response
from functools import wraps
from app.api.api_msg import ApiResponseError, api_status_msg


def catch_api_exception():
    """
    catch api error
    :param type:
    :return:
    """

    def _handle(func):
        @wraps(func)
        def __handle(*args, **kwargs):
            errno, msg, data = -1, '', ''
            try:
                data = func(*args, **kwargs)
                errno = 10000
                msg = 'success'
            except ApiResponseError as e:
                are = e.extra_msg
                errno = are['code']
                msg = are['msg']
                data = e.data
            except Exception as e:
                print(e)
                errno = api_status_msg.func_error['code']
                msg = api_status_msg.func_error['msg']
                data = str(e)
            finally:
                _res = {
                    'code': errno,
                    'message': msg,
                    'result': data
                }

                result = make_response(json.dumps(_res, ensure_ascii=False))
                result.headers['Content-Type'] = 'application/json'
                return result

        return __handle

    return _handle
