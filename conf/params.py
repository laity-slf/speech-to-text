import argparse
import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def parse_args():
    parser = argparse.ArgumentParser(description='text summary service')
    parser.add_argument('--log_path', default=basedir + '/log/asr.log', type=str, required=False, help='日志路径')
    parser.add_argument('--asr_config',
                        default=None, type=str,
                        required=False, help='asr配置文件')
    parser.add_argument('--asr_checkpoints',
                        default=None, type=str, required=False, help='asr模型文件')
    parser.add_argument('--punc_config', default=None,
                        type=str, required=False, help='标点恢复配置文件')
    parser.add_argument('--punc_checkpoints',
                        default=None, type=str,
                        required=False, help='标点恢复模型文件')
    parser.add_argument('--punc_vocab',
                        default=None, type=str,
                        required=False, help='标点恢复词表')         
    args = parser.parse_args()
    return args
