import requests
import json

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,ja;q=0.5,cs;q=0.4',
    'Connection': 'keep-alive',
    'Cookie': 'T591_TOKEN=fv1tt7pgo4sntbgf2c7b6qhp27; _ga=GA1.3.534028057.1602575540; tw591__privacy_agree=0; webp=1; PHPSESSID=qmc3bj1h8uq4i913df54uijdv1; c10f3143a018a0513ebe1e8d27b5391c=1; new_rent_list_kind_test=0; _gid=GA1.3.1950998262.1602990911; _ga=GA1.4.534028057.1602575540; _gid=GA1.4.1950998262.1602990911; _fbp=fb.2.1602990911030.1484722112; is_new_index=1; is_new_index_redirect=1; index_keyword_search_analysis=%7B%22role%22%3A%220%22%2C%22type%22%3A%221%22%2C%22keyword%22%3A%22%22%2C%22selectKeyword%22%3A%22%22%2C%22menu%22%3A%22%22%2C%22hasHistory%22%3A0%2C%22hasPrompt%22%3A0%2C%22history%22%3A0%7D; user_index_role=1; __auc=3f2aabc31753aa5069533cf6292; __utma=82835026.534028057.1602575540.1603009936.1603009936.1; __utmz=82835026.1603009936.1.1.utmcsr=pttdigits.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=82835026; localTime=2; DETAIL[1][9785213]=1; last_search_type=2; DETAIL[1][9918209]=1; urlJumpIp=3; urlJumpIpByTxt=%E6%96%B0%E5%8C%97%E5%B8%82; DETAIL[1][9888388]=1; user_browse_recent=a%3A5%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bs%3A7%3A%229888388%22%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bs%3A7%3A%229918209%22%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bs%3A7%3A%229785213%22%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bs%3A7%3A%229941534%22%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bs%3A7%3A%229967629%22%3B%7D%7D; __asc=ceb7d7601753ba4252d8c48ee72; XSRF-TOKEN=eyJpdiI6IjFSbStqY1hKU1Fva1BoNklqb1NxTkE9PSIsInZhbHVlIjoielpCZFpYbHIyWm5tMTI5V3JvQ1orUUtYQ2ZFQ1lWS29kOWpNN2N5OUtyUyt4c2hSd2Q5NlwvTE5nUGtQMHBTVUN5YnkwdlJSUzNRejRLTmZuUnlaS3V3PT0iLCJtYWMiOiJhMWUyZGQ0NjdiMDYyZDg0Y2NlOTUyNmQ4ODQ0ZTIwYzQ3OWY4MGE0ODMyMzEyZGIwNjI5NmY2ZjBjYmRhMDk4In0%3D; 591_new_session=eyJpdiI6Im1YSGpvOVpmcERweDY3Q0h3QUY5ekE9PSIsInZhbHVlIjoiSnVXZWhDVVBqKzVjSGhcL1BubzBIc1F0cGJ0NzRpQ0Z5REFlaURTNm83Q1dmZ2ZROStCTUZjTGJtempmTjgrRVdJR3NTOE83aDJrbE1QSmdkMGdQbTdnPT0iLCJtYWMiOiI0NWIzZGRkZmI0M2QwNTUxMTg3YWQ5MmI0NGRiOWNlNjQ4ZjUyNWZjZTI4YTNlYjg2NDBjOWM5OWM1Y2IxN2U2In0%3D; _gat_UA-97423186-1=1',
    'Host': 'rent.591.com.tw',
    'Referer': 'https://rent.591.com.tw/?kind=0&region=3',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'X-CSRF-TOKEN': '4CHmjtOiuW4BdsYMZAbbmbTiclMOoJInWsaL0bmP',
    'X-Requested-With': 'XMLHttpRequest'
    }

# 基本591官網requests
res = requests.get('https://www.591.com.tw/', headers = headers)

# 租屋頁首頁抓取
res = requests.get('https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=3', headers = headers)

# 租屋頁第二頁抓取
res = requests.get('https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=3&firstRow=30&totalRows=8950', headers = headers)
# print(res.text)

# https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=3&firstRow=30&totalRows=8950
# https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=3&firstRow=60&totalRows=8950
# https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=3&firstRow=90&totalRows=8950
# https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=3&firstRow=120&totalRows=8950

for i in range(0,300, 30):
    res = requests.get('https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=3&firstRow=%s&totalRows=8950' %i, headers = headers)
    data = json.loads(res.text, encoding= 'utf-8')
    # print(data) # 換成json後會變成中文

    # 改成字串排列整齊，並調整好中文編碼問題, indent 表示空格數量
    content = json.dumps(data,ensure_ascii=False,sort_keys=True, indent=4)

    # 儲存到data.json檔案裡面
    with open('alldata.json', 'a',encoding='utf-8') as file: # 千萬要記住檔案這邊也要用utf-8來處理，否則也會是亂碼
        file.write(content)
        pass
    # print('https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=3&firstRow=%s&totalRows=8950' %i)
    pass




# # 資料轉換成json
# data = json.loads(res.text, encoding= 'utf-8')
# print(data) # 換成json後會變成中文

# # 改成字串排列整齊，並調整好中文編碼問題, indent 表示空格數量
# content = json.dumps(data,ensure_ascii=False,sort_keys=True, indent=4)

# # 儲存到data.json檔案裡面
# with open('data.json', 'w+',encoding='utf-8') as file: # 千萬要記住檔案這邊也要用utf-8來處理，否則也會是亂碼
#     file.write(content)
#     pass