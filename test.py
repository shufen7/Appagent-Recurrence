import openai

openai.api_key = "sk-Ded7q0qdW7lwvTe54a7a53A3363e4b0e8eCe7b9182809a5d"  # 你的真实 API key
openai.api_base = "https://api3.apifans.com/v1"

try:
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hello, can you read me?"}]
    )
    print("✅ API 正常，返回内容：")
    print(response["choices"][0]["message"]["content"])
except Exception as e:
    print("❌ 出错了：", e)
