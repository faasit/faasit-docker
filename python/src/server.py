from flask import Flask,request,jsonify,make_response
import requests

app = Flask(__name__)

# 配置python日志, 按照格式输出到标准输出
import logging
logger = logging.getLogger("faasit")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

formatter = logging.Formatter('[%(asctime)s] %(message)s')

handler.setFormatter(formatter)

logger.addHandler(handler)

# 从环境变量中读取代码文件
import sys
import os
import importlib
codeDir = os.environ.get('CODE_DIR', 'code')
codeName = os.environ.get('CODE_NAME', 'index')
downLoadFile = os.environ.get('FAASIT_CODE_DIR', 'code.zip')
sys.path.append(f'/{codeDir}')

import zipfile
def check_and_load_code():
    if not os.path.exists(f'/{codeDir}/{codeName}.py'):
        # 不使用代理下载代码，是一个zip，解压后放到指定目录
        code_url = f"http://10.102.131.24:80/data/uploads/{downLoadFile}"
        r = requests.get(code_url, stream=True, proxies={'http': None, 'https': None})
        with open('/tmp/code.zip', 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        with zipfile.ZipFile('/tmp/code.zip', 'r') as z:
            z.extractall('/code')
        
        

@app.route('/', methods=['POST', 'GET'])
async def local_invoke():
    try :
        req = request.get_json()
        event = req['event']
        metadata = req['metadata']
        logger.info(f"[INPUT] {req}")

        # 导入用户代码
        check_and_load_code()
        code = importlib.import_module(codeName)
        result = await code.handler(event,metadata)
        logger.info(f"[OUTPUT] {result}")

        resp = jsonify(result)
        return resp
    except Exception as e:
        logger.error(f"[ERROR] {e}")
        return make_response(jsonify({'error': str(e)}), 500)
    
@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000)