# 导入requests库，用来发送网络请求（和大模型服务器通信）
import requests


# 定义一个聊天函数，输入prompt（你的问题），返回大模型的回答
def chat_with_qwen(prompt):
    # 通义千问的API地址（固定不变）
    url = (
        "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    )
    # 请求头：带上你的API Key，告诉服务器你是谁
    headers = {"Authorization": "Bearer sk-e097c74fd06241588e3e5ab3ae64289f"}
    # 请求体：告诉模型用哪个版本，以及你的问题
    body = {
        "model": "qwen-turbo",  # 用最快的通义千问版本
        "input": {"messages": [{"role": "user", "content": prompt}]},
    }
    # 发送POST请求给大模型服务器
    response = requests.post(url, json=body, headers=headers)
    # 返回服务器的响应结果
    return response.json()


# 测试函数：调用聊天函数，传入问题
if __name__ == "__main__":
    # 你的第一个问题
    question = (
        "总结一下：今天天气很好，我去公园散步，看到了很多花，还有小朋友在放风筝。"
    )
    result = chat_with_qwen(question)
    # 调用函数，得到回答
    # answer = chat_with_qwen(question)
    clean_answer = result["output"]["text"]
    # 打印回答
    print("大模型回答：", clean_answer)
