# 來進行591租屋網爬蟲吧!
    學習影片: https://www.youtube.com/watch?v=zzMRbrOHlrk&list=PLohb4k71XnPaQRTvKW4Uii1oq-JPGpwWF&index=23
    在學習此篇爬蟲時，請勿造成591租屋網困擾，此篇教學僅為學習爬蟲使用

## 在XHR找到資料的連結後，你也請求失敗嗎?
    找到https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=6，結果請求卻得到空值嗎?
    當把實際網頁的headers的內容全部給加上，再進行一次requests就可以請求到了!
    主要可以發現是Cookie及X-CSRF-TOKEN的值是務必要填入的，否則會requests不出來
    1. Cookie
    2. X-CSRF-TOKEN
    
## response 的json中文內容都變成亂碼嗎? 來參考這篇吧!
    參考文獻: https://www.itread01.com/content/1547834072.html


## 進階學習！把全部頁數的資料都給爬出來吧
    請查看591Rentall.py吧!我們在每次切換頁面時，把不一樣的地方給列出來
    # https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=3&firstRow=30&totalRows=8950
    # https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=3&firstRow=60&totalRows=8950
    # https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=3&firstRow=90&totalRows=8950
    # https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=3&firstRow=120&totalRows=8950

    從上述可以發現，firstRow每30切換一次，因此我們用for迴圈進行一個重複動作，重新請求，然後複寫檔案就可以了
    要記住因為寫入檔案時，我們是推新的東西進到檔案裏面，因此w+改為用a

    我們因為是練習，只抓取10個頁面的資料，我們當然能用beautifulsoup先去抓取總頁數，然後再把for迴圈的條件給改成總頁數後，全部抓取
    但為了避免造成他人困擾，因此我這邊就不示範了，謝謝