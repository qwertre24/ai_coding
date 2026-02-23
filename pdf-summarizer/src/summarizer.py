from openai import OpenAI
from src.config import API_KEY, API_BASE_URL, DEFAULT_MODEL, SUMMARY_PROMPT


def summarize(content, api_key=None, model=None, prompt=None):
    if api_key is None:
        api_key = API_KEY
    if model is None:
        model = DEFAULT_MODEL
    if prompt is None:
        prompt = SUMMARY_PROMPT
    
    client = OpenAI(
        base_url=API_BASE_URL,
        api_key=api_key
    )
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"请严格按格式输出，少于100字，不要代码：\n\n{content}"}
        ]
    )
    
    return response.choices[0].message.content
