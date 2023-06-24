# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArabicfiWordItem(scrapy.Item):
    word_in_arabic_diacritics = scrapy.Field()
    word_in_arabic = scrapy.Field()
    pronunciation = scrapy.Field()
    meaning = scrapy.Field()
    declension = scrapy.Field()
    pronunciation_audio = scrapy.Field()
    part_of_speech = scrapy.Field()
    pattern = scrapy.Field()
    word_link = scrapy.Field()
