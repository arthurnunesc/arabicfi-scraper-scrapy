import scrapy
from scrapy.loader import ItemLoader
from arabicfi_scraper.items import ArabicfiWordItem
from bidi.algorithm import get_display
import pyarabic.araby as araby


class Spider(scrapy.Spider):
    name = "arabicfi"
    start_urls = ["https://arabic.fi/words"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, dont_filter=True, callback=self.crawl_word_links)

    def crawl_word_links(self, response):
        for word_link in response.css(
            "div.alphabet-links-english a::attr(href)"
        ).getall():
            yield scrapy.Request(word_link, dont_filter=True, callback=self.parse_word)

    def parse_word(self, response):
        loader = ItemLoader(item=ArabicfiWordItem, response=response)
        loader.add_css("word_in_arabic_diacritics", "span::text")
        loader.add_value(
            "word_in_arabic", araby.strip_diacritics(response.css("span::text").get())
        )
        yield loader.load_item()
