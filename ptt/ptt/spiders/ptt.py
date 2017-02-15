import scrapy
import logging
from scrapy.http import FormRequest
from datetime import datetime
from ptt.items import PostItem
from ptt.items import PostItem2

class PTTSpider(scrapy.Spider):
    name = 'ptt'
    allowed_domains = ['ptt.cc']
    start_urls = ('https://www.ptt.cc/bbs/Stock/index.html', )
    _retries = 0
    MAX_RETRY = 1
    _pages = 0
    MAX_PAGES = 1

    def parse(self, response):
        if len(response.xpath('//div[@class="over18-notice"]')) > 0:
            if self._retries < PTTSpider.MAX_RETRY:
                self._retries += 1
                logging.warning('retry {} times...'.format(self._retries))
                yield FormRequest.from_response(response,
                                                formdata={'yes': 'yes'},
                                                callback=self.parse)
            else:
                logging.warning('you cannot pass')


        else:
            self._pages += 1
            for href in response.css('.r-ent > div.title > a::attr(href)'):
                url = response.urljoin(href.extract())
                yield scrapy.Request(url, callback=self.parse_post)

            if self._pages < PTTSpider.MAX_PAGES:
                next_page = response.xpath(
                    '//div[@id="action-bar-container"]//a[contains(text(), "上頁")]/@href')
                if next_page:
                    url = response.urljoin(next_page[0].extract())
                    logging.warning('follow {}'.format(url))
                    yield scrapy.Request(url, self.parse)
                else:
                    logging.warning('no next page')
            else:
                logging.warning('max pages reached')
    
                    
#--------------------------------------

    def parse_post(self, response):
        item = PostItem2()
        item['title'] = response.xpath(
            '//meta[@property="og:title"]/@content')[0].extract()
        #不抓作者
        #item['author'] = response.xpath(
        #    '//div[@class="article-metaline"]/span[text()="作者"]/following-#sibling::span[1]/text()')[
        #        0].extract().split(' ')[0]
        datetime_str = response.xpath(
            '//div[@class="article-metaline"]/span[text()="時間"]/following-sibling::span[1]/text()')[
                0].extract()
        item['date'] = datetime.strptime(datetime_str, '%a %b %d %H:%M:%S %Y')

        item['content'] = response.xpath('//div[@id="main-content"]/text()')[
            0].extract()

        comments = []
        #改寫為推噓箭頭皆為1分
        total_score = 0
        for comment in response.xpath('//div[@class="push"]'):
            push_tag = comment.css('span.push-tag::text')[0].extract()
            push_user = comment.css('span.push-userid::text')[0].extract()
            push_content = comment.css('span.push-content::text')[0].extract()

            if '推' in push_tag:
                score = 1
            elif '噓' in push_tag:
                score = 1
            else:
                score = 1

            total_score += score

            #comments.append({'user': push_user,
            #                 'content': push_content,
            #                 'score': score})
            
        #不爬comment內容只爬分數
        #item['comments'] = comments
        item['score'] = total_score
        #不爬url
        #item['url'] = response.url

        #辨別是否為標的文
        if item['title'].find('標的')>-1: 
            item['isTarget'] = 1
            if item['title'].find('Re:')==-1:
                LS = 0
                #找到內文 分類那行,  分辨多空
                if LS==1:
                    item['L_score'] = total_score * 1
                    item['S_score'] = 0
                elif LS==-1:
                    item['L_score'] = 0
                    item['S_score'] = total_score * -1  
                    
            elif item['title'].find('Re:')>-1:
                LS = 0
                #找到搜索內文, 分辨多空
                if LS==1:
                    item['L_score'] = total_score * 1
                    item['S_score'] = 0
                elif LS==-1:
                    item['L_score'] = 0
                    item['S_score'] = total_score * -1         
            else:
                item['L_score'] = 0
                item['S_score'] = 0
        else:
            item['isTarget'] = 0
            item['L_score'] = 0
            item['S_score'] = 0
        
        yield item