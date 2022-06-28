# coding:utf-8
import time
import os
import paddle
from .paddlespeech.cli.asr import ASRExecutor
from .paddlespeech.cli.text import TextExecutor


def initial_model(args):
    asr_executor = ASRExecutor()
    text_executor = TextExecutor()
    asr_executor(
        model='conformer_wenetspeech',
        lang='zh',
        sample_rate=16000,
        config= args.asr_config,
        # Set `config` and `ckpt_path` to None to use pretrained model.
        ckpt_path=args.asr_checkpoints,
        force_yes=False,
        device=paddle.get_device())
    text_executor(
        task='punc',
        model='ernie_linear_p3_wudao',
        lang='zh',
        config=args.punc_config,
        ckpt_path=args.punc_checkpoints,
        punc_vocab=args.punc_vocab,
        device=paddle.get_device())

    return asr_executor, text_executor


def asr_infer(asr_executor, audio_file: str):
    return asr_executor.read_to_infer(
        model='conformer_wenetspeech',
        lang='zh',
        sample_rate=16000,
        audio_file=audio_file,
        force_yes=False, )


def pun_restoration(text_executor, text: str):
    return text_executor.read_to_infer(text)

# are_ ,tex=initial_model()
#
# print(pun_restoration(tex,asr_infer(are_)))
