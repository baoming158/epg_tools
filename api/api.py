import json

from flask import Blueprint, render_template

from rabbitmq.producer import sendMqMessage
from service.update_abs_id import do_modify

api = Blueprint('api', __name__,
                  template_folder='templates')

@api.route('/', methods=['GET'])
def index():
    return render_template('api/welcome.html')

#批量更新接口
@api.route("/update_abs", methods=['GET'])
def update_abs():
    file = "epg.txt"
    list = do_modify(file)
    mq_message = render_template('api/update_abs.html', list=list)

    mq_str = json.loads(mq_message)

    sendMqMessage(mq_message)

    print(mq_str)

    return render_template('api/update_abs.html', list=list)