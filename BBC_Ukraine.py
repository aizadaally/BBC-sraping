import scrapy 

class bbcSpider(scrapy.Spider):
    name = 'bbcnews'
    start_urls = ['https://www.bbc.com/russian/topics/cez0n29ggrdt']

    def parse(self, response):
        for link in response.css('bbc-1prgecg e3hd7yi0 a::attr(href)').get():
            yield response.follow(link,callback=self.parse_bbc)

        for i in range(1, 100):
            next_page = f'https://www.bbc.com/russian/topics/cez0n29ggrdt/page-{i}/'
            yield response.follow(next_page, callback=self.parse)
    
    def parse_bbc(self, response):
        yield{
            'title':response.css('h1.bbc-7ota8y e1yj3cbb0::text').get(),
            'date':response.css('time class.bbc-14xtggo exyigsi0::text').get(),
            'text':response.css('p.bbc-bm53ic e1cc2ql70::text').get()
        }




