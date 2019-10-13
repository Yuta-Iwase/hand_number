from flask import Flask, request
import base64
from io import BytesIO
from datetime import datetime
import webbrowser
from PIL import Image
from hand_number_class import Hand_num

hand_num = Hand_num()
app = Flask(__name__)

# index.htmlを返信
@app.route('/', methods=['GET'])
def index():
    with open('index.html', 'r', encoding='utf-8') as html:
        return html.read()

# 数字推定APIを稼働
@app.route('/api/image', methods=['POST'])
def image():
    req = request.form['img']
    req_dec = base64.b64decode(req.split(',')[-1])
    img = Image.open(BytesIO(req_dec))
    img.save('image.png')
    num_class = hand_num.estimate()[0]
    timestamp = '[' + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + ']'
    print(timestamp + 'from ' + request.remote_addr + ' > predict:' + str(num_class))
    return str(num_class)

# その他ファイルを返信
@app.route('/<file>', methods=['GET'])
def file_receive(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return f.read()
    except: 
        return ''
try:
    url = "127.0.0.1:8080"
    browser = webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s')
    browser.open(url)
except:
    pass

host = '0.0.0.0'
port = 8080
app.run(host=host, port=port, threaded=True)