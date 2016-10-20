from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors


class TutorialPipeline(object):

    def __init__(self):

        dbargs = dict(
            host = '127.0.0.1' ,
            db = 'scrapydb',
            user = 'root', #replace with you user name
            passwd = '1234', # replace with you password
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
            )
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)

    def process_item(self, item,spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item

    def insert_into_table(self,conn,item):
        print type(item['name'])
        va = (item['name'],'1',item['desc'])
        sql = "insert into tb_scrapy values ('%s','%s','%s')" % va
        conn.execute(sql)
