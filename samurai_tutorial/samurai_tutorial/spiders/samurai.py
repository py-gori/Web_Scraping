# -*- coding: utf-8 -*-
import scrapy


class SamuraiSpider(scrapy.Spider):
    name = 'samurai'
    allowed_domains = ['www.sejuku.net']
    start_urls = [
        'https://www.sejuku.net/blog/',
    ]

    def parse(self, response):
        root_url = self.start_urls[0].replace('/blog/', '')

        div_main_box = response.css('div#main-box-2')[0]
        for div_cur in div_main_box.css('div.curriculum_banner'):
            url = div_cur.css('a::attr(href)').extract_first()
            url = root_url + url
            yield scrapy.Request(url, callback=self.parse_word)

    def parse_word(self, response):
        search_word = 'python'
        main_contents = response.css('main').extract_first()

        if search_word in main_contents.lower():
            print('{}という文字列を発見しました。nURL: {}'.format(search_word, response.url))
