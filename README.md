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
    