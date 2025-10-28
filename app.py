# encoding=utf-8
from models.chatbot_model import ChatbotModel
from utils.app_init import before_init
from utils.helpers import load_all_scene_configs
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 实例化ChatbotModel
chatbot_model = ChatbotModel(load_all_scene_configs())

# AI对话接口：接收问题 → 调用机器人 → 返回答案
@app.route('/multi_question', methods=['POST'])
def api_multi_question():
    data = request.json # 每HTTP 请求进来（POST /multi_question），Flask 会自动解析这个请求，并把它的所有信息（URL、Headers、Body、参数等）封装到一个叫 request 的全局上下文对象中。
    question = data.get('question')
    if not question:
        return jsonify({"error": "No question provided"}), 400

    response = chatbot_model.process_multi_question(question)
    return jsonify({"answer": response})

# 网页入口：当用户用浏览器访问 http://localhost:5000/ 时，执行这个函数
@app.route('/', methods=['GET'])
def index():
    return send_file('./demo/user_input.html')# 把本地的 user_input.html 文件发送给浏览器


if __name__ == '__main__':
    before_init()
    app.run(port=5000, debug=True, use_reloader=False)

"""
用户浏览器                          Flask 后端
     │                                   │
     ├─────── GET / ────────────────→    │
     │                                   │
     ←────── HTML 页面 ───────────────    │
     │                                   │
     │ 用户输入 "我想改航班"                │
     │ 点击“提问”                         │
     │                                   │
     ├──── POST /multi_question ──────→  │
     │       {question: "我想改航班"}      │
     │                                   │
     │ 调用 chatbot_model 处理            │
     │                                   │
     ←───── {"answer": "..."} ────────── │
     │                                   │
     │ 显示回答                           │
     └───────────────────────────────────┘
"""