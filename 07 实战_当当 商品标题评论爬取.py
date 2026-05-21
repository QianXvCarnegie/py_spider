# 爬5页数据

import requests
from lxml import etree
import os

# https://category.dangdang.com/cp01.01.02.00.00.00.html
# https://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
# https://category.dangdang.com/pg3-cp01.01.02.00.00.00.html

def get_intels(page):
    if page == 1:
        url = "https://category.dangdang.com/cp01.01.02.00.00.00.html"
    else:
        url = f"https://category.dangdang.com/pg{page}-cp01.01.02.00.00.00.html"
    my_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "cookie": "ddscreen=2; __permanent_id=20260427181412181324784515232387367; __visit_id=20260427181412202232624861339216314; __out_refer=1777284852%7C!%7Ccn.bing.com%7C!%7C; __rpm=%7Cmix_317715...1777284863730; search_passback=277100891a762cd25037ef69000000007c6fcb004837ef69; __trace_id=20260427181545908327465388241456248; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; pos_9_end=1777284946069; pos_6_end=1777284947101; pos_6_start=1777284963291; ad_ids=108395950%2C88414785%7C%231%2C1",
        "host": "category.dangdang.com",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
    }

    resp = requests.get(url, headers=my_headers)
    tree = etree.HTML(resp.text)

    lines = tree.xpath("//div[@id='search_nature_rg']//li")

    f = open(f"./books/{page}.csv", mode="w", encoding='utf-8')

    for line in lines:
        intro = ''.join(line.xpath("./p[@class='name' and @name='title']/a/@title"))
        now_price = ''.join(line.xpath("./p[@class='price']/span[@class='search_now_price']/text()"))
        pre_price = ''.join(line.xpath("./p[@class='price']/span[@class='search_pre_price']/text()"))
        desc = ''.join(line.xpath("./p[@class='detail']/text()"))

        content = f"{intro}\nnow_price: {now_price},  pre_price: {pre_price}\n{desc}"
        f.write(content)
        f.write("\n"*2)

    print(f"第{page}已完成")

    f.close()

if not os.path.exists("./books"):
    os.makedirs("./books")

for i in range(1,6):
    get_intels(i)
