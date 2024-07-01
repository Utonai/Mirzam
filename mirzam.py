import re
import sys
import time
import json
import requests

################################################################
# 记得认真看完所有注释内容调整完再使用，有空看看源码，总共也没几行（
################################################################

# 日志文件的路径
LOG_FILE = "mirzam.log"

# 提交成功标记，如果服务器返回的提示中包含这些内容，日志中不会记录此次提交相关内容（已经拿分了还记啥啊
SUCCESS_TAG = "提交成功"

# 提交失败标记，如果服务器返回的提示中包含这些内容，日志中会直接标记为"FAILED"
FAILURE_TAG = ["已经提交", "提交的key错误", "提交失败", "已过期"]

# 时延，单位为秒，用于防止提交速度过快，有需求再改
OFFSET = 0

################################################################

def log(flag, message):
    localtime = time.strftime("%H:%M:%S", time.localtime())
    f = open(LOG_FILE, "a")
    f.write(localtime + "\t" + flag + "\t" + message + "\n")
    f.close()


def failure_detect(m):
    for tag in FAILURE_TAG:
        if tag in m:
            return True
    return False


def submit(flag):
    try:
        ################################################################
        addr = "http://192.168.100.1/Title/TitleView/savecomprecord"
        postdata = {"flag": flag, }
        headers = {"User-Agent": "Beta Canis Majoris", }
        cookies = {"RA": 95.67493869, "Dec": -17.95591772, }
        response = requests.post(addr, data=postdata, headers=headers, cookies=cookies, verify=False, timeout=3)
        ################################################################
        # ↑↑↑小孩子不懂事，写着玩的，记得按实际需求改↑↑↑

        # print(response.text)

        # 遇到编码问题可以调整一下试试
        # response.encoding = "utf-8"

        result = response.text
        # result需要的内容大概是像“提交flag成功”、“submit success”这样的服务器返回的提示
        # 这里按实际情况调整，比如服务器返回的内容包在一串json里就可以像下面这样
        # result = json.loads(response.text)["msg"]

        message = ""  # No news is good news :)
        if failure_detect(result):
            message = "FAILED"
        elif SUCCESS_TAG not in result:
            message = result

        return message

    except Exception as e:
        message = "EXCEPTION: " + str(e)
        return message


def mirzam(txt):
    """
    梦开始的地方（？

    :param txt: 包含符合flag格式内容子串的一坨字符串
    :type txt: string
    :return: 成功的话返回空字符串，失败的话返回具体情况
    :rtype: string
    """

    # 从txt中正则符合flag{xxxxx}格式的字符串，不需要正则功能的话可以把下面这一小块代码替换成 flag = txt
    match = re.search("flag{.+?}", txt)
    if match:
        flag = match.group()
    else:
        return txt + " - Not a flag"
    
    message = submit(flag)

    if message:  # Bad news :(
        log(flag, message)
        message = flag + " - " + message

    if OFFSET:
        time.sleep(OFFSET)

    return message


def main():
    # 测试用，调用方法："python mirzam.py flag{114514}"
    print(mirzam(sys.argv[1]))


if __name__ == '__main__':
    main()
