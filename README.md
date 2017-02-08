# D3.js 期末 Project : PTT Stock版文章與推文與股價與成交量視覺化

## 1. 網路爬蟲爬取 Ptt 文章與推文, 並定義多空關鍵字
### 1.1 Scrapy + Python3  抓取 Ptt 文章並分析
> 作者: SHAFORM  
> 參考網址: http://city.shaform.com/blog/2016/02/28/scrapy.html  
> 目前進度:  
> 取得10頁資料, 要設定讓爬蟲抓350頁.


### 1.2 定義多空關鍵字與分數結構
> 目前進度:   
> 參考 Ptt Stock 版版規  
> #### [類別一 標的 主文]  -> 文章 title 帶有 '標的' 且不以 'Re:'開頭  
> 文章內容找到'分類'那一行, 若關鍵字多比空多, 則本篇分數 = +1x推噓文總量, 若是空, 分數為-1x推虛文總量  
> 由於推文難以拆解分析到底推文者看空看多, 牽涉語意分析, 故簡化算法.  
> #### [類別二 標的 回文] -> 文章 title 帶有 '標的' 且以 'Re:'開頭  
> 文章內容帶有多的關鍵字較多, 則本篇分數 = +1x推噓文總量, 若是空, 分數為-1x推虛文總量  


### 1.3 將爬取的 json 檔案按照 1.2 的規則整理成 csv 或是另一個 json
> 目前進度:  
> python 的 json 操作, 是否要轉成 dataframe 以便操作? 
> 如何辨別這篇文章標的? title 跟 分類  
> Loop through json 檔把整理一張分數列表  
> 股號, 中文名, 日期, +分數, -分數


## 2. 網路爬蟲爬取台股半年資料
### 2.1 使用網路爬蟲
> 參考  
> 目前進度: 
> 執行出現a bytes-like object is required, not 'str' error  
> 尚未找到挑選股票再爬的方法  
> 資料格式不符  

## 3. 選定視覺化模板
### 3.1 股價K線圖
> 參考 http://bl.ocks.org/andredumas/045f550b72ad46301130  
> 目前進度:  
> 網頁script, css可以運作, data格式固定 

### 3.2 關鍵字出現分數圖

## 4. 網頁與視覺化製作