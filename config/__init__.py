print("Config package initialized.")

DEBUG = True

# MODEL ------------------------------------------------------------------------

# 模型支持OpenAI规范接口
GPT_URL = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'
MODEL = 'glm-4.5-flash'
API_KEY = '6bef3f6bcff94c16a4e9b0ae1cc492f6.M6BeONHpdpImLaxn'
SYSTEM_PROMPT = 'You are a helpful assistant.'

# GPT_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
# MODEL = 'qwen3-max'
# API_KEY = 'sk-ce8d16460fb24dcd93a69e400a7cbb1f'
# SYSTEM_PROMPT = 'You are a helpful assistant.'
# MODEL ------------------------------------------------------------------------

# CONFIGURATION ------------------------------------------------------------------------

# 意图相关性判断阈值0-1
RELATED_INTENT_THRESHOLD = 0.5

# CONFIGURATION ------------------------------------------------------------------------
