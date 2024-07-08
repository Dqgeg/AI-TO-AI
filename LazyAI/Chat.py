import requests

log_file = None

def set_log_file_path(path):
    global log_file
    log_file = path

def chat(ip, prompt, token, character_id):
    url = f"{ip}/gemini/chat"
    payload = {
        "prompt": prompt,
        "character_id": character_id
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        response_text = response.text.strip()  # 直接获取响应文本
        log_to_file(response_text, 'LazyAI')
        return response_text
    else:
        print("LazyAI 请求失败:", response.text)
        return None

def log_to_file(response_text, source):
    global log_file
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"{source}: {response_text}\n")
        f.write("===================================================================\n\n")
