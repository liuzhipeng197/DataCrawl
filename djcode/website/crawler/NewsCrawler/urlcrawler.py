#encoding=utf-8
import time
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import re,sys,Queue,datetime,time
import threading,mutex
from NewsParser.sinaNewsParser import sinaNewsParser
from newsDAO import newsDAO
 
#unique url set
urlset = set()
#parser url job queue
urlqueue = Queue.Queue()


class UrlParser():
    def getallnews():
	pass
 
    def flushtime(self,news,job,now_time):
   	pass
 
    def run(self):
        while urlqueue.empty()==False:
		job=urlqueue.get()
        	today = datetime.date.today()
                newsurlpattern = re.compile(str(today))
                text = urlopen(job).read()
                soup = BeautifulSoup(text,fromEncoding="gb18030")
	        now_time = time.localtime().tm_hour*60 + time.localtime().tm_min

                if newsurlpattern.search(job):
                    print job
		    news = sinaNewsParser(soup,job,now_time)
		    if news:
		    	print news['pubdate']
		        news_time = news['pubdate']
		        #将每个小时刷新一次新闻
			stmt = 'insert into news_info(NewsTitle,NewsContent,NewsDate,NewsSource) values(\'%s\',\'%s\',\'%s\',\'%s\')' % (news['title'],news['content'],news['pubdate'],news['source'])                                                          
        		newsDAO(stmt)
		    else:
			break

def getallnews():
    job = urlqueue.get()
    text = urlopen(job).read()
    soup = BeautifulSoup(text,fromEncoding="gb18030")

    for header in soup('a'):
        #<a>label which has href attribute
        if header.has_key('href'):
                #strip whitespace before or after the string
                url = header['href'].encode('utf8').strip()
                #if the string begins with 'http://' or 'https://'and isn't in the urlset
                pattern = re.compile('^(https?://tech.sina.com.cn/i/)')
                if pattern.match(url) and url not in urlset: 
                    urlqueue.put(url)
                    urlset.add(url)

def test():
    urlset.add('http://roll.tech.sina.com.cn/internet_all/index_1.shtml')
    urlqueue.put('http://roll.tech.sina.com.cn/internet_all/index_1.shtml')
    getallnews()
    paraser = UrlParser()
    paraser.run()

if __name__ == "__main__":
    test()
