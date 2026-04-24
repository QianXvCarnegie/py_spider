# 目标, 拿到该网站的标题, 影评内容

# 先访问页面源代码. 从页面源代码中提取到 标题和data-rid
# 根据不同的rid. 发送不同的full请求. 就能拿到文章的所有内容

import requests
from lxml import etree
import re

url = "https://movie.douban.com/review/best/"

my_headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "cookie": "bid=WqyfHhbDftc; ll=\"118225\"; _pk_id.100001.4cf6=bed849490052f0f3.1770719332.; _vwo_uuid_v2=D502B13318CDF47C66A54089C0CA3A126|252145e8ca1091718c188ce755c9e72e; __yadk_uid=QSmSuCG70l3Xx4poPw2upIzqcoCmGlcy; viewed=\"1085860\"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1776992736%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.1009391277.1770623478.1776948254.1776992736.12; __utmb=30149280.0.10.1776992736; __utmc=30149280; __utmz=30149280.1776992736.12.10.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.984711973.1770719332.1776948254.1776992736.10; __utmb=223695111.0.10.1776992736; __utmc=223695111; __utmz=223695111.1776992736.10.8.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://movie.douban.com/top250",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
}

resp_1 = requests.get(url, headers = my_headers)
page_1 = etree.HTML(resp_1.text)
rts = page_1.xpath("//div[@data-cid]")

f = open("豆瓣评价.txt", mode="w", encoding="utf-8")

for rt in rts:
    title = rt.xpath(".//h2/a/text()")[0]

    # 提取展开后的url
    cid = rt.xpath(".//@data-cid")[0]

    # 拼接url，发请求，得到评价内容所在文本
    full_url = f"https://movie.douban.com/j/review/{cid}/full"
    resp_2 = requests.get(full_url, headers = my_headers)

    # 解析内容，提取文本
    body = resp_2.json()["body"]
    page_2 = etree.HTML(body)
    content = page_2.xpath("//div[@class='review-content clearfix']//text()")
    content = re.sub(r"\s","", "".join(content))
    f.write(content)
    f.write("\n"*3)

f.close()

