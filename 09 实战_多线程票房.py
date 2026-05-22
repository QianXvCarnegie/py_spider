import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import time

# 单线程

# def get_intel(year):
#     session = requests.session()
#     session.headers = {
#         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#         "accept-encoding": "gzip, deflate",
#         "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#         "cache-control": "no-cache",
#         "connection": "keep-alive",
#         "cookie": "__51cke__=; Hm_lvt_b6d45668276623ae0dd56fcf7dad2ead=1777201129,1779412029; HMACCOUNT=26DA1A8A6170BDF8; __tins__4287866=%7B%22sid%22%3A%201779412028864%2C%20%22vd%22%3A%208%2C%20%22expires%22%3A%201779414142541%7D; __51laig__=8; Hm_lpvt_b6d45668276623ae0dd56fcf7dad2ead=1779412343",
#         "host": "www.boxofficecn.com",
#         "pragma": "no-cache",
#         "upgrade-insecure-requests": "1",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
#     }
#
#     f = open(f"{year}", mode='w', encoding="utf-8")
#     url = f'http://www.boxofficecn.com/boxoffice{year}'
#
#     resp = session.get(url)
#
#     tree = etree.HTML(resp.text)
#     trs = tree.xpath("//div[@class='entry-content']//tbody/tr")[1:]
#     for tr in trs:
#         xv =''.join(tr.xpath("./td[1]/text()"))
#         yea = "".join(tr.xpath('./td[2]/text()'))
#         name = "".join(tr.xpath('./td[3]//text()'))
#         money = "".join(tr.xpath('./td[4]/text()'))
#         info = f"{xv} {yea} {name} {money}\n"
#         f.write(info)
#     print(f"{year}年已完成")
#
# def main():
#     for i in range(1995, 2011):
#         get_intel(i)
#
# if __name__ == '__main__':
#     tm1 = time.time()
#     main()
#     tm2 = time.time()
#     print(tm2 - tm1)
#     # 15.125568628311157   放里面
#     # 16.48629856109619   放里面
#     # 20.58874273300171   不放里面
#     # 15.92319941520691  session.headers放在模块里面明显更快


# 多线程


def get_intel(year):
    session = requests.session()
    session.headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "cookie": "__51cke__=; Hm_lvt_b6d45668276623ae0dd56fcf7dad2ead=1777201129,1779412029; HMACCOUNT=26DA1A8A6170BDF8; __tins__4287866=%7B%22sid%22%3A%201779412028864%2C%20%22vd%22%3A%208%2C%20%22expires%22%3A%201779414142541%7D; __51laig__=8; Hm_lpvt_b6d45668276623ae0dd56fcf7dad2ead=1779412343",
        "host": "www.boxofficecn.com",
        "pragma": "no-cache",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
    }

    f = open(f"{year}", mode='w', encoding="utf-8")
    url = f'http://www.boxofficecn.com/boxoffice{year}'

    resp = session.get(url)

    tree = etree.HTML(resp.text)
    trs = tree.xpath("//div[@class='entry-content']//tbody/tr")[1:]
    for tr in trs:
        xv =''.join(tr.xpath("./td[1]/text()"))
        yea = "".join(tr.xpath('./td[2]/text()'))
        name = "".join(tr.xpath('./td[3]//text()'))
        money = "".join(tr.xpath('./td[4]/text()'))
        info = f"{xv} {yea} {name} {money}\n"
        f.write(info)
    print(f"{year}年已完成")

def main():
    with ThreadPoolExecutor() as t:
        for i in range(1995, 2011):
            t.submit(get_intel, i)

if __name__ == '__main__':
    tm1 = time.time()
    main()
    tm2 = time.time()
    print(tm2 - tm1)
    # 12.999629497528076
    # 13.249379396438599
    # 多线程确实快，目前只差两秒多是因为爬的内容少