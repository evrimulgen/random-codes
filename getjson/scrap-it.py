import scrapy

class ArticleSpider(scrapy.Spider):
	name = "article"
	start_urls = ['htt[p://blog.theodo.fr/2018/02/scrape-websites-5-minutes-scrapy']

	def parse(self, response):
		conten = response.xpath(".//div[@class='entry-content']/descendant::text()").extract()
		tield {"article" : ''.join(content)}