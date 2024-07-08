import os
import time
from datetime import datetime
import env
from LazyAI.Select_character import select_characters
from LazyAI.Chat import chat, set_log_file_path as set_lazyai_log_file
from spark_model import spark_response, set_log_file_path as set_spark_log_file

ip = env.ip
token = env.token

# 创建日志文件路径
log_dir = 'log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
log_file = os.path.join(log_dir, f"conversation_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

# 设置 LazyAI 和 Spark 的日志文件路径
set_lazyai_log_file(log_file)
set_spark_log_file(log_file)

def main():
    character_id, character_name, character_greetings = select_characters(ip, token)
    print(f"选择的角色 NAME 是: {character_name}")

    prompt = input("请输入问候语：")

    while True:
        print("\n--- 调用 LazyAI ---")
        lazyai_reply = chat(ip, prompt, token, character_id)
        if lazyai_reply:
            print(f"LazyAI: {lazyai_reply}")

            print("\n--- 调用 Spark ---")
            spark_reply = spark_response(lazyai_reply)
            if spark_reply:
                print(f"Spark: {spark_reply}")

                prompt = spark_reply
                time.sleep(5)
            else:
                print("Spark 请求失败")
                break
        else:
            print("LazyAI 请求失败")
            break

if __name__ == "__main__":
    main()
