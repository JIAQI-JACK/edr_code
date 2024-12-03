import time
from flask import Blueprint, request

main_bp = Blueprint("main", __name__)


@main_bp.route('/check_system', methods=['GET', 'POST'])
def check():
    requests_data = request.json or request.args or request.form or {}
    logger.info('main->check: requests_data:{}'.format(requests_data))

    result = {
        "datetime": datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d HH:MM:SS'),
        "info": 'ok',
    }
    return jsonify(result)
