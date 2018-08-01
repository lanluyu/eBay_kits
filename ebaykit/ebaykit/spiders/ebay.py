# -*- coding: utf-8 -*-
from scrapy import Request,Spider
from ebaykit.items import EbaykitItem

class EbaySpider(Spider):
    name = 'ebay'
    allowed_domains = ['ebay.com']

    def start_requests(self):
        # 设置请求链接规则
        for i in range(1,72):
            basic_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=emergency+kit&_ipg=200&_pgn="
            start_url = basic_url+str(i)
            yield Request(url=start_url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        yema = response.xpath('.//a[@aria-current="page"]/text()').extract_first()
        print('正在爬取第'+yema+'页')
        kits = response.xpath('.//ul[@class="srp-results srp-list clearfix"]/li')
        for kit in kits:
            item = EbaykitItem()
            item['name'] = kit.xpath('.//h3[@role="text"]/text()').extract_first()
            item['price'] = kit.xpath('.//span[@class="s-item__price"]//text()').extract_first()
            item['origin'] = kit.xpath('.//span[@class="s-item__location s-item__itemLocation"]/text()').extract_first()  # 产地
            item['sold'] = kit.xpath('.//span[@class="NEGATIVE BOLD"]/text()').extract_first()
            item['status'] = kit.xpath('.//span[@class="SECONDARY_INFO"]/text()').extract_first()   # 新旧
            item['yema'] = response.xpath('.//a[@aria-current="page"]/text()').extract_first()

            #print(item)
            yield item