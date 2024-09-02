# test_requests.py
import requests

try:
    response = requests.get('https://httpbin.org/get')
    response.raise_for_status()  # 这将检查异常
    print("请求成功!")
    print(response.json())  # 打印响应内容
except requests.RequestException as e:
    print(f"请求失败: {e}")
print("hello")