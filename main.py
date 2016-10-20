from scrapy import cmdline
#cmdline.execute("scrapy crawl movies".split())
#cmdline.execute("scrapy crawl movies_recursion".split())
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="1234")
cur = conn.cursor()
cur.execute('create database if not exists scrapydb')
conn.select_db('scrapydb')
cur.execute('create table tb_scrapy(`name` char(20) not null,`link` char(20) not null,`desc` varchar(16) default null)')
conn.commit()
cur.close()
conn.close()

cmdline.execute("scrapy crawl movies_recursion_mysql".split())
