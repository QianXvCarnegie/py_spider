# 爬取大陆票房的历年票房: 名次  年份  电影名  票房
import traceback
from os import EX_OK

import requests
from lxml import etree
import os

def get_info(year):
    url = f"http://www.boxofficecn.com/boxoffice{year}"
    my_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "cookie": "__51cke__=; Hm_lvt_b6d45668276623ae0dd56fcf7dad2ead=1777201129; HMACCOUNT=90BE23EA50B15D8E; __tins__4287866=%7B%22sid%22%3A%201777201128559%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201777203100550%7D; __51laig__=3; Hm_lpvt_b6d45668276623ae0dd56fcf7dad2ead=1777201301",
        "host": "www.boxofficecn.com",
        "pragma": "no-cache",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
    }

    resp = requests.get(url, headers = my_headers)

    page = etree.HTML(resp.text)
    trs = page.xpath("//div[@class='entry-content']//tr")[1:]

    f = open(f"./movies_1/{year}.csv", mode="w", encoding = "utf-8")
    for tr in trs:
        num = "".join(tr.xpath("./td[1]//text()"))
        if not num:
            continue
        year = "".join(tr.xpath("./td[2]//text()"))
        if not year:
            continue
        name = "".join(tr.xpath("./td[3]//text()"))
        money = "".join(tr.xpath("./td[4]//text()"))

        st = f"{num}, {year}, {name}, {money}"
        f.write(st)
        f.write("\n")

    f.close()

# 创建文件夹
if not os.path.exists("./movies_1"):
    os.makedirs("./movies_1")

# 记录错误
f2 = open("error_record.txt", "w", encoding="utf-8")

for i in range(2015, 2026):
    try:
        get_info(i)
        print(i, "已完成")
    except Exception as e:
        print(i, "有问题有问题有问题")
        f2.write(str(i))
        f2.write("\n"*2)
        f2.write(str(traceback.format_exc()))
        f2.write("\n"*3)


