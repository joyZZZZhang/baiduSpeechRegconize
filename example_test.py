import base64
import urllib
import requests
import json

API_KEY = "MrDbZCeiFV9ljw58kHDwH8iA"
SECRET_KEY = "TxsMHM3fa1k7RZ4GnScQfn6lGQose0HE"


def main():
    url = "https://vop.baidu.com/server_api"

    payload = json.dumps({
        "format": "wav",
        "rate": 16000,
        "channel": 1,
        "cuid": "1R21mHHqmfLRolkqMQhdQjM9IdLuN0h1",
        "token": get_access_token(),
        "dev_pid": 1537,
        "speech": get_file_content_as_base64("Chinese_test.wav"),
        "len": 27773
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
