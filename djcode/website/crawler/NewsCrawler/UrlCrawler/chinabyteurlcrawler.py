#encoding=utf-8
import re
import time
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import re,sys,Queue,datetime,time
import threading,mutex
from NewsParser.chinabyteNewsParser import chinabyteNewsParser
from newsDAO import newsDAO
import urlparse 
 
#unique url set
urlset = set()
#parser url job queue
urlqueue = Queue.Queue()


class ChinabyteUrlParser():
    def flushtime(self,news,job,now_time):
   	pass
 
    def run(self):
        while urlqueue.empty()==False:
		job=urlqueue.get()
        	today = datetime.date.today()
                text = urlopen(job).read()
                soup = BeautifulSoup(text.decode('gb2312','ignore'))
	        now_time = time.localtime().tm_hour*60 + time.localtime().tm_min

                if job:
		    news = chinabyteNewsParser(soup,job,now_time)
		    if news:
		    	print news['pubdate']
		        news_time = news['pubdate']
		        #将每个小时刷新一次新闻
			stmt = 'insert into news_info(NewsTitle,NewsContent,NewsDate,NewsSource,NewsLogo) values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' % (news['title'],news['content'],news['pubdate'],news['source'],news['logo'])                                                          
        		newsDAO(stmt)
		    else:
			break

    def getallnews(self):
    		job = urlqueue.get()
    		text = urlopen(job).read()
    		soup = BeautifulSoup(text.decode('gb2312','ignore'))

    		for header in soup('a'):
        		#<a>label which has href attribute
        		if header.has_key('href'):
                	#strip whitespace before or after the string
                		url = header['href'].encode('utf8').strip()
                		#if the string begins with 'http://' or 'https://'and isn't in the urlset
                		pattern = re.compile('^(http://(\w)+\.chinabyte.com/(\d)+/)')
                		if pattern.match(url) and url not in urlset: 
                    			urlqueue.put(url)
					urlset.add(url)
					print url

    def test(self,urls):
		for url in urls:
    			urlset.add(url)
    			urlqueue.put(url)
    			#urlparser = UrlParser()	
			self.getallnews()
    			self.run()

if __name__ == '__main__':
	chinabyte = ChinabyteUrlParser()
	chinabyte.test() 
