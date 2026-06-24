import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Queue

def get_img_src(url, q):

    session = requests.session()
    # 获取图片链接
    session.headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "cookie": "Hm_lvt_2fc12699c699441729d4b335ce117f40=1780185866; HMACCOUNT=26DA1A8A6170BDF8; _agep=1780185867; _agfp=609698db01e05bbee4ad50ea76a379e8; _agtk=b41ea9e752ec5ce9381781404de04087; XSRF-TOKEN=eyJpdiI6Ikw1ejJ5VVZzZnF6bllvS2N5VXZxVHc9PSIsInZhbHVlIjoicTRid2hjNUN3ajR4dGNcL3FpUnJNZ21rUDdHSDdOZzJlUWNSeHJmaFRpWHhSb3JVRnVnUmZuRmZrd1FyWWFaa1QiLCJtYWMiOiI5NDA3ZTRmNGU5YzNhYWZmMWZhNzMxMjZkNDk4Y2E0MWFiMGNiNGMxNGU2MTZlZWQ2YTEyYzhmYjdlNWEyMzkwIn0%3D; doutula_session=eyJpdiI6Im1WRjlpTHJvNEMydHFvXC8ya3VKMmdBPT0iLCJ2YWx1ZSI6IllJYXFxOHdXZnR6dzBQcjZWSTY5K3ZxTU5JdFZUZERDMXQyWGF0TmplTlRyczlUSW1nK2hcL21IdnhINkllbUtWIiwibWFjIjoiN2ZhODE5Y2I5MGEwOGMxNGEyZDE1YzE2YzFmOTQ0NTIwMGIzOTgxNGM5YjQ4ZDdmMzI4OTMwMzU1MmQ0YWY4NCJ9; Hm_lpvt_2fc12699c699441729d4b335ce117f40=1780185912",
        "host": "www.doutupk.com",
        "pragma": "no-cache",
        "referer": "https://www.doutupk.com/article/list/?page=1",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Microsoft Edge\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
    }

    resp = session.get(url)
    tree = etree.HTML(resp.text)

    srcs = tree.xpath('//div[@class="col-sm-9 center-wrap"]/a')

    for src in srcs:
        origin_urls = src.xpath(".//img/@data-original")
        q.put(origin_urls)
        print(origin_urls)


def get_img_process(q):
    with ThreadPoolExecutor(2) as t:
        for i in range(2,4):
            t.submit(get_img_src, f"https://www.doutupk.com/article/list/?page={i}", q)
    q.put("结束啦")
    print("生产者完成，===============================")

def download_img(origin_urls):

    session_img = requests.session()
    session_img.headers = {
        "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "host": "img.doutupk.com",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"149\", \"Chromium\";v=\"149\", \"Not)A;Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "image",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"
    }

    for url in origin_urls:
        file_name = url.split('/')[-1]
        img_resp = session_img.get(url)

        with open(file_name, mode = 'wb') as f:
            f.write(img_resp.content)
            print("已完成下载一张图片")


def download_process(q):
    with ThreadPoolExecutor(3) as t:
        while 1:
            original_src = q.get()
            if original_src == "结束啦":
                break
            t.submit(download_img, original_src)
    print("所有文件下载完毕，==========================")


def main():
    # 创建队列
    q = Queue()

    # 搞生产获取链接
    p1 = Process(target=get_img_process, args=(q,))
    # 搞消费下载图片
    p2 = Process(target=download_process, args=(q,))

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()

# 接下来要上多线程，提升效率了！加油，哈哈哈，好棒