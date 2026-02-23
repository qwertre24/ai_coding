import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("OPENROUTER_API_KEY", "")

API_BASE_URL = "https://api.siliconflow.cn/v1"

DEFAULT_MODEL = "Qwen/Qwen2-7B-Instruct"

SUMMARY_PROMPT = """你是一个极简摘要助手。
【强制规则】
1. 输出必须少于100字
2. 完全禁止代码、示例、详细解释
3. 只输出核心概念

【输出格式】（严格按这个格式）
## [文档标题]
- 要点1
- 要点2
- 要点3
## 总结：[一句话]"""

SUPPORTED_EXTENSIONS = [".pdf", ".md"]

DEFAULT_OUTPUT = "summary.md"
