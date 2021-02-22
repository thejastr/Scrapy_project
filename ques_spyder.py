# -*- coding: utf-8 -*-

import scrapy
from ..items import AptiquesItem

class QuoteSpider(scrapy.Spider):
    name = 'apti'
    page_number = 2
    start_urls = [
            'https://www.fresherslive.com/online-test/probability-questions-and-answers/1'
            ]
    
    def parse(self, response):
        
        items = AptiquesItem()
        
        o=response.css('label::text').extract()
        l=response.css('.qus_txt::text').extract()


        
        for i,j in zip(range(len(l)),range(0,len(o),5)):
            questions = l[i]
            op1=o[j]
            op2=o[j+1]
            op3=o[j+2]
            op4=o[j+3]
            op5=o[j+4]
            
            
            items['_question'] = questions
            items['option1'] = op1
            items['option2'] = op2
            items['option3'] = op3
            items['option4'] = op4
            items['option5'] = op5
        
            yield items
            #yield{'question':questions,'option1':op1,'option2':op2,'option3':op3,'option4':op4,'option5':op5}
            
        next_page = 'https://www.fresherslive.com/online-test/probability-questions-and-answers/'+str(QuoteSpider.page_number)+'/'
        print(next_page)
        
            
        if QuoteSpider.page_number < 11:
            yield response.follow(next_page, callback = self.parse)
            QuoteSpider.page_number += 1
            
            
            