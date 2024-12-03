
class ApiResponseError(Exception):
    """
    error type
    """

    def __init__(self, *args, extra_msg=None, data=None):
        self.extra_msg = extra_msg
        self.data = data
        super(ApiResponseError, self).__init__(*args)


class ApiStatusMsg(object):
    """
    api status message
    """
    status_msg = {
        'success': {'code': 200, 'msg': 'success', 'status': 1},
        'processing': {'code': 200, 'msg': 'processing', 'status': 2},

        'handle_error': {'code': 500, 'msg': 'handle error', 'status': 3},
        'func_error': {'code': 500, 'msg': 'func error', 'status': 4},
        'lack_params': {'code': 500, 'msg': 'lack params', 'status': 5},
        'error_params': {'code': 500, 'msg': 'error params', 'status': 6},
        'error_result': {'code': 500, 'msg': 'error result', 'status': 7},
    }

    def __init__(self):
        self.__dict__ = self.status_msg


api_status_msg = ApiStatusMsg()
