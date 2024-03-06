import scrapy


class firstSpider(scrapy.Spider):
    name = 'books'

    def start_requests(self):
        URL = 'https://books.toscrape.com/'
        yield scrapy.Request(url=URL, callback=self.response_parser)

    def response_parser(self, response):
        for selector in response.css('article.product_pod'):
            yield {
                'title': selector.css('h3 > a::attr(title)').extract_first(),
                'price': selector.css('.price_color::text').extract_first(),
            }

        next_page_link = response.css('li.next a::attr(href)').extract_first()

        if next_page_link:
            yield response.follow(next_page_link, callback=self.response_parser)

        for book in response.xpath('//article'):
            yield {
                'booktitle': book.xpath('.//a/text()').get(),
                'bookrating': book.xpath('.//p').attrib['class'],
                'bookprice': book.xpath('.//div[2]/p/text()').get(),
                'bookavailability': book.xpath('.//div[2]/p[2]/i/following-sibling::text()').get().strip()
            }

