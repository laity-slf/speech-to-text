# 启动说明
        1、安装python>=3.7(建议版本3.7.12)
        2、安装c++ 编译环境
           ubuntu: sudo apt instal build-essential
           centos: sudo yum install gcc gcc-c++
           others:conda install -y -c gcc_linux-64=8.4.0 gxx_linux-64=8.4.0
        3、创建虚拟环境
        4、安装依赖包(确保在PaddleSpeech 根目录上)：
           pip install pytest-runner -i https://pypi.tuna.tsinghua.edu.cn/simple
           gpu版本(需全局安装cuda、cudnn):
           cuda10.2:
           python3 -m pip install paddlepaddle-gpu==2.3.0 -i https://mirror.baidu.com/pypi/simple
           cuda11.2:
           python -m pip install paddlepaddle-gpu==2.3.0.post112 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
           安装其余依赖
           pip install . -i https://pypi.tuna.tsinghua.edu.cn/simple
           cpu版本:
           pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
           pip install paddlespeech -i https://pypi.tuna.tsinghua.edu.cn/simple
        5、运行serving/app.py

# 接口返回说明
ASR接口
        
        请求类型：post 
        功能：输入一个音频文件（MP4或者WAV）的地址，返回语音识别后的结果
        请求输入输出参数如下：
        请求参数说明：
        path：音频文件的地址
        add_pun：是否使用标点符号恢复（1代表恢复，0代表不恢复），默认进行恢复。
        
输入

        {
            "path":"/home/shanhoo3/slf/workspace/asr_paddlespeech/audio_file/inforec-20220101-1a34a5b01c9f22406426e975f804bb06.wav",
            "add_punc":0
        }

输出

        {
            "data": "大太太怒斥唐庭山做得太绝，他可是你的兄弟啊，你们也是一起生活了二十几年的兄弟，兄弟，你知道吗？唐庭山忍不住报出所有真相，他连续两次想要我的命啊，他还把我亲生弟弟杀死，还害死了我亲生母亲，这叫兄弟吗？一夜之间沦为乞丐，亲爱文怪，唐庭山太狠，我跟你无冤无仇，你干吗连我也要迁为其中啊，收到我跟你不相上下。金艾文当初把唐庭山扫别出门，还对他百般羞辱，落井下时连车也不准他开走，这会儿倒撇的一干二净，唐庭山不但要给自己报仇。",
            "msg": "success",
            "status": 200
        }


# 调用方式

	    测试环境式例（文章生成）：curl -H "Accept: application/json" -H "Content-type: application/json" -X POST  -d ' {"path":"/home/shanhoo3/slf/workspace/asr_paddlespeech/audio_file/inforec-20220101-1a34a5b01c9f22406426e975f804bb06.wav","add_punc":0}'  http://localhost:5071/nlp/asr
