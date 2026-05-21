"""
搞定滚动刷新， 取——用户名，题目，内容
"""

import requests

url = "https://xueqiu.com/statuses/hot/listV3.json"

# 为什么url取上面的部分，而不是如下全部？
"""
https://xueqiu.com/statuses/hot/listV3.json?page=1&last_id=386967184&md5__
1038=263ce5aa2b-et7SqSXhNdokhno2h80VEhkBhxtQkQEIhrSE8ZXktdTHEh6UhoHpXThJAS
kddYo6hotozhT8hh7heUh_dIhoEdhbeUhPDiSomhZUhWhmsool%3DhnhLSggbhoV0BhMEYbfg_
hb9hBSgFsdhy9hVVUh12U6PEI%2Fydo%2FTd43ydc%3DdIYYudHSfhtwWoWUhf7%2FhgUSh
"""

page = 1
last_id = '386967184'
pages = int(input("请输入爬取页数："))

for i in range(pages):
    my_headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "cookie": "cookiesu=581777525258577; device_id=7b760ecfffa6a42aef071aca0d899fa4; smidV2=20260430130101efccf28f7842d49feb2072d72b2631d700f23b5bcdfa820b0; acw_tc=276077e917776886742855374ef5e1259d3bf118caab7bb0d2414dc3e25005; xq_a_token=0b6d260a5333284ddd41e07bd185f7392f567236; xqat=0b6d260a5333284ddd41e07bd185f7392f567236; xq_r_token=865b12c689ce7a8fd47556c8eaaf2d2e6361c23b; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTc3OTc1ODU4OCwiY3RtIjoxNzc3Njg4NjUwOTMzLCJjaWQiOiJkOWQwbjRBWnVwIn0.Ck4SdR1aw31PkTJ-kZHDkiyw99VRaSfDYW4S_klA_-KuuZODi4wrFCpihsoNbShVG2l4M967O_qtJ2pipJyQS6O6sKjEe_l4XX89HOoNMjTHhPB_QuTvmPPu7ww2Eg1cDF68ueiZs_UT-QyrA1ZWaLWT-9fBVkqNoAhgY2B2SPbDiEX1ObyWvA6NIozyf_fXrnFJHm25W5vA6cU2qUUHgkJ4T6hJltNzBityaq9oD4FshyfIc-yaNkywQfe3HIj0b4WzTJjOoskSl_yi85c1437hLFZ1sh8IpWPm-9X6eNPBGIYR0xCfDl6Td3Bv3c6Lvxf-DvhHWp7LYvOZEhHvSQ; u=581777525258577; Hm_lvt_1db88642e346389874251b5a1eded6e3=1777525261,1777688684; HMACCOUNT=90BE23EA50B15D8E; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1777688737; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=fGG2tqwrGUh9BUC2ir/YDjXMaRszNOLE20YGsGHpH/5ILI2287RWjD+CfwALphsPIA0L4kgESQvVYO/FavBmog%3D%3D; ssxmod_itna=1-YqUx9GKQwbD=G0D2DRxiIPQFzDQqY9Di=DzxC5iOsDuOxjKidqDUAQdxGwPEehXxtCeWjGxo3BBxGNopDA5DnGx7YDtr4IqCDGhvx4kPcW4u4Wm0kDHpeKjaE_C3HYbgkOp2=G6kIk2ODsx/Ktvaqq2=DbShweq0qoDCPDExGk3lAwmDiiax0rD0eDPxDYDG4DoaoDnh4DjxDdmf8LU83Dbxi3m4iaDGeDerfvDY5eDD5WTI23vUPDB6pnk6oxk_uUDNo2Am2f3Djebi3D964DsoRgkrS2AL/FR4QB_vLbz40kBq0OU_Rja3quBWnSag_e74tNfdfhecr42Eit7de2xl0x30xsotNGePA5TCdtBDi4=1EdDD3zjPnj0wn0l2NVxixb_mYx5Ae=Rez9pKQDqeKGiD3BrP0qsCGGGq5CIzBi3ixqQRrBbPr4NKY=34cecxr4d8RwGP2UPxD; ssxmod_itna2=1-YqUx9GKQwbD=G0D2DRxiIPQFzDQqY9Di=DzxC5iOsDuOxjKidqDUAQdxGwPEehXxtCeWjGxo3BYxD3bBDDqoPt147prWs4GNoWh2axpjqAFaxt2mE3OGm6E2E7M7OW1GQkc2bm7DZDCW2iFD8HG_mpxcobG6rxaKlcOtipYsgiFzaH_3nKQdbWGthEed3_4xKyzW80_LODxOrDG0B0m3CE4dSaqf=cik2cHtPy7_DAO_4uiZ_3Iqm7OHSPGrwEwCgivTRpY5FaOZ1S73QG7o3h6B3UpkrG89IS9EXaatIkj7PBpbCS8STs1fby3vRjRVGhBAnhAT0fpk3TC8cVIWctaaR9ASFHe29mbtCKHAaulRmKHCmxH9nhKGwAaaBw2CqinnuGpHYid1vW0mqC54=nABbc/gPdyCB4PtegSREeWh/g69RcD8PfTuz3Gfoj4_8SHUjExKqe2mObTWpxct7NQLnG9xPdiVKFbPkfwV7oCmT_Ghx9F7X5sEYwC9gtB_UA9bT71TIB5jerdLLG7OHKGBmRopp8KEES4MmhkPeQbL1Ydk2uIND07K7tmK1GoPupxSc832znVta_G=8I5989EIeKV=riTTkTVfT7jARsYp0a8C0Oef8ZQHYGTtwH8En5EVm2iLLQnEqB200rs=X/l3t99gMMfXPMdoEYxoG4/ohpghNtii8NPj5e0ZrGbDNCs4D",
    "host": "xueqiu.com",
    "pragma": "no-cache",
    "referer": "https://xueqiu.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"147\", \"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"147\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
}

    my_param = {
        "page": page,
        "last_id": last_id,
        "md5__1038": "263ce5aa2b-et7SqSXhNdokhno2h80VEhkBhxtQkQEIhrSE8ZXktdTHEh6UhoHpXThJASkddYo6hotozhT8hh7heUh_dIhoEdhbeUhPDiSomhZUhWhmsool=hnhLSggbhoV0BhMEYbfg_hb9hBSgFsdhy9hVVUh12U6PEI/ydo/Td43ydc=dIYYudHSfhtwWoWUhf7/hgUSh"
    }
    # Query String Parameters 的最后一个参数  ”md5__1038“:…………  为什么不上传？

    resp = requests.get(url, headers = my_headers, params= my_param)
    rst = resp.json()
    lists = rst['list']
    for lst in lists:
        title = lst["title"]
        user_name = lst["user"]['screen_name']

        # 刷新last_id
        if not i == 1:
            last_id = lst["id"]

        # content =
        print(title[:5] if title else "(无标题)", user_name)

    page += 1