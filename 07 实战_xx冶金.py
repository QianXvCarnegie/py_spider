"""
网址: http://www.metalinfo.cn/mi.html
目标数据:
    标题, 内容, 发布时间, 来源
"""

import requests

url = "http://www.metalinfo.cn/json/search/list"

my_data = {
    "pageSize": "20",
    "current": "1",
    "resourceType": "r_news",
    "facetFilter": "{}",
    "order": "desc",
    "sort": "sort_time"
}

my_headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "content-length": "86",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "Hm_lvt_204973c50a7ce5a180c8edd164761976=1721992303; HMACCOUNT=40D17769013D04CF; JSESSIONID=1E116168F82C2B499D1F35FBC00C899C; Hm_lpvt_204973c50a7ce5a180c8edd164761976=1722002339",
    "dnt": "1",
    "host": "www.metalinfo.cn",
    "origin": "http://www.metalinfo.cn",
    "pragma": "no-cache",
    "referer": "http://www.metalinfo.cn/mi.html",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
resp = requests.post(url, data=my_data, headers=my_headers)

# 剩下的就是汪峰的事情了....
dic = resp.json()

tid = '4de50205386c41af94409fdf8d2e1118'

for r in dic['result']['records']:
    detail = r['r_abstract_skos']
    real_time = r['real_time']
    release_url = r['release_url']
    title = r['title']

    rid = r['rid']

    # 此时. 想要拿到详情页的url, 单纯从json里面是不能直接拿到的.
    # 不要拘束于. 从上一个url返回的东西里面一定要拿到详情页的url
    # 我们可以自己去拼接出来一个详情页url
    # 中冶天工
    detail_page_url = f"http://www.metalinfo.cn/news/{rid}.html?rtype=r_news&columnId={tid}"
    # print("详情页的url", url)
    # 通过观察发现, 详情页的url 是没有什么用的....
    # 真实的数据是通过 http://www.metalinfo.cn/json/resource/detail
    # 返回的.
    # 只要请求到detail即可
    print("主页面访问完毕. 详情页开始请求")
    detail_url = "http://www.metalinfo.cn/json/resource/detail"
    my_params = {
        "rid": rid,
        "rtype": "r_news",
        "columnId": tid
    }

    detail_headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        # "content-length": "86",     # 请求体有多少内容, get请求是没有请求体的....77777 9999
        # "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": "Hm_lvt_204973c50a7ce5a180c8edd164761976=1721992303; HMACCOUNT=40D17769013D04CF; JSESSIONID=1E116168F82C2B499D1F35FBC00C899C; Hm_lpvt_204973c50a7ce5a180c8edd164761976=1722004196",
        "dnt": "1",
        "host": "www.metalinfo.cn",
        "pragma": "no-cache",
        "referer": detail_page_url,  # 当前这个请求是来自于哪个url 7779999
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    resp = requests.get(detail_url, params=my_params, headers=detail_headers)
    print(resp.text)

    break  # 测试一个. 直接break
