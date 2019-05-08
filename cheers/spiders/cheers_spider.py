import scrapy
from scrapy import Spider
import csv
from cheers.items import CheersItem, Field

class CheersSpider(Spider):
	name = "cheers"
	allowed_domains = ["cheers.com.np"]
	
	def start_requests(self):
		liquor_type = ['whisky','vodka','gin','rum','brandy','liqueur','tequila','wine','beer','beverages','glass','mixers','tobacco','offers']
		urls = []
		for i in range(0, len(liquor_type)):
			product = liquor_type[i]
			for i in range(1, 50):
				page_number = str(i)
				address = 'https://cheers.com.np/category?c='+str(product)+'&pf=&pt=&p='+page_number+'&node=child'
				urls.append(address)
		print(urls)
		for url in urls:
			print("Scrapping here")
			print(url)
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		print("processing:"+response.url)
		title = response.css('.title.primary-color::text').getall()
		price = response.css('.price::text').getall()
		
		with open('new_result.csv', 'a', encoding='utf-8') as csvfile:
			for i in range(len(title)):
				csvfile.write(title[i])
				csvfile.write('*')
				csvfile.write(price[i])
				csvfile.write('\n')
		print("writing to file")
