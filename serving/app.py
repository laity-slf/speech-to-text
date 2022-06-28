import sys
import os
from flask import Flask, request, jsonify
sys.path.insert(0, sys.path[0] + '/../')
sys.path.insert(0, sys.path[0] + '/commons/')
from model.speechtotext import initial_model, asr_infer, pun_restoration
from commons.content_wash import filter_tags
from conf.params import parse_args
from commons.get_logger import get_logger
import logging
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/nlp/asr', methods=['POST'])
def asr():
    try:
        data = request.get_json()
        audio_file = data.get('path')
        flag = data.get('add_pun') if data.get('add_pun') is not None else True
        app.logger.info('成功接收path: ' + audio_file)
        # 过滤掉html符号
        content = filter_tags(audio_file)
        app.logger.info('过滤掉html： ' + content)
        # 是否存在文件
        audio_file = os.path.abspath(audio_file)
        if not os.path.isfile(audio_file):
            raise Exception('Invalid audio_file')
        # TODO 要做的操作
        text = asr_infer(asr_model, audio_file=audio_file)
        res = pun_restoration(pun_model, text) if flag else text
        return jsonify(status=200, data=res, msg="success")

    except Exception as e:
        app.logger.info(e)
        return jsonify(status=112001, msg='fail')

# 执行
if __name__ == "__main__":
    args = parse_args()
    logger = get_logger(args.log_path)
    handler = logging.FileHandler(args.log_path)
    asr_model, pun_model = initial_model(args)
    logger.info('模型加载成功')
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    app.run(
        host='0.0.0.0',
        port=5071
    )
