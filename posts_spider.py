import scrapy

class PostsSpider(scrapy.Spider):
    name = "Posts"

    start_urls = [
        'https://www.bbc.com/russian/topics/cez0n29ggrdt'
    ]

    def parse(self, response):
        for post in response.css('div.post-item'):
            yield {
                'title':post.css('.post-header h2 a::text')[0].get, 
                'date':post.css('.post-header a;;text')[1].get(), 
                'author':post.css('.post-header a::text')[2].get()
            }
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
             
