eBay_kits说明文档
==
介绍
 - 
eBay_kits是一个基于Scrapy的商品信息爬虫，爬取了eBay上关于急救包的价格、产地等信息。<br>

代码说明
--
### 运行环境
* Windows 10 专业版<br>
* Python 3.5/Scrapy 1.5.0/MongoDB 3.4.7<br>

### 依赖包
* Requests<br>
* Pymongo<br>
* Faker(随机切换User-Agent)<br>

爬取结果
-
在eBay上爬取了12000余条有关急救包的信息。结果由爬虫先存储在MongoDB中，再导出为Excle文件。部分数据如下截图:<br>
![信息截图](https://github.com/lanluyu/eBay_kits/blob/master/%E9%83%A8%E5%88%86%E6%80%A5%E6%95%91%E5%8C%85%E4%BF%A1%E6%81%AF%E6%88%AA%E5%9B%BE.PNG)
