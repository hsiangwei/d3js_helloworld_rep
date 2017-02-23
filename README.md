# D3.js 期末 Project : PTT Stock版文章與推文與股價走勢之視覺化

# 作品簡介
Ptt 股票版討論熱度, 與股價走勢之視覺化.
洞見契機, 趨吉避凶, 避免成為股海慘戶.

*****
# 作法分享
## 1. 網路爬蟲爬取 Ptt 文章與推文, 並定義多空關鍵字
### 1.1 Scrapy 抓取 Ptt 文章並分析
作者: SHAFORM  
參考網址: http://city.shaform.com/blog/2016/02/28/scrapy.html  

### 1.2 定義多空關鍵字與分數結構
參考 Ptt Stock 版版規  
#### [類別一 標的 主文]  -> 文章 title 帶有 '標的' 且不以 'Re:'開頭  
文章內容找到'分類'那一行, 若關鍵字多比空多, 則本篇分數 = +1x推噓文總量, 若是空, 分數為-1x推虛文總量  
> 由於推文難以拆解分析到底推文者看空看多, 牽涉語意分析, 故簡化算法.  

#### [類別二 標的 回文] -> 文章 title 帶有 '標的' 且以 'Re:'開頭  
文章內容帶有多的關鍵字較多, 則本篇分數 = +1x推噓文總量, 若是空, 分數為-1x推虛文總量  
#### 在爬取同時順便分析是否帶有多 Long, 空 Short 關鍵字, 並計算多空討論熱度分數  
增加 PostItem 內容, L_score, S_score, isTarget, targetName  
重新爬取資料.

example : https://www.ptt.cc/bbs/Stock/M.1487741035.A.881.html

## 2. 網路爬蟲爬取台股半年資料
本來想參考 https://github.com/Asoul/tsec 自製爬蟲
> 因為時間不夠, 直接手動下載 ptt 討論熱度較高的個股, 再手動把爬蟲爬下來的 ptt 討論熱度加到 dataset


## 3. 利用d3js視覺化
### 3.1 股價K線圖與討論熱度圓圈
> 有了每日開盤收盤, 最高最低價的資訊, 就可以用 rect & line 來繪製 K 線圖

### 3.2 引力圈圈
> 參考投影片重力場版型, 把要視覺化的個股依照討論熱度來繪製不同大小的圓圈.

*****
# 遭遇困難


## 未解決
1. 自行定義的討論熱度太主觀, 需要語意分析來判別這個推文隱含的立場 (在酸民, 反串充斥的 ptt 尤其困難)
2. 過程不夠自動化, 收盤資訊與資料整理依然是手動進行.

Demo : https://hsiangwei.github.io/d3js_helloworld_rep/index.html

