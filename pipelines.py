# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class AptiquesPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn = sqlite3.connect("myquestions.db")
        self.curr = self.conn.cursor()
        
    def create_table(self):
            self.curr.execute("""DROP TABLE IF EXISTS questions""")
            self.curr.execute(""" create table questions (
               Question text,
               Option1 text,
               Option2 text,
               Option3 text,
               Option4 text,
               option5 text )
               """)
                              
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self,item):
        self.curr.execute("""insert into questions values (?,?,?,?,?,?)""",
                          (item['_question'],
                           item['option1'],
                           item['option2'],
                           item['option3'],
                           item['option4'],
                           item['option5']
                              ))
        self.conn.commit()
            
                           

