#encoding=utf-8
import re
import time
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import re,sys,Queue,datetime,time
import threading,mutex
from newsDAO import newsDAO
import urlparse 
from myfactory import MyFactory 
from newsclassify import NewsClassify
 
#unique url set
urlset = set()
#parser url job queue
urlqueue = Queue.Queue()


class UrlParser():
    def __init__(self,name):
	self.name = name
	mf = MyFactory(name)
	self.NewsParser = mf.createNewsParser() 

    def flushtime(self,news,job,now_time):
   	pass
 
    def run(self):
        while urlqueue.empty()==False:
		job = urlqueue.get()
        	today = datetime.date.today()
                text = urlopen(job).read()
		print self.name
                
		if self.name == "chinabyte":
			soup = BeautifulSoup(text.decode('gb2312','ignore'))
	        elif self.name == "sina":
			soup = BeautifulSoup(text,fromEncoding="gb18030")
		
		now_time = time.localtime().tm_hour*60 + time.localtime().tm_min

                if job:
		    news = self.NewsParser.newsparser(soup,job,now_time)
		    if news:
		    	print news['pubdate']
			
			#分类
			nc = NewsClassify()
			news['sort'] = nc.classify(news['title'])
			
			if news['sort'] == 'others':
				pass
			else:
		        	news_time = news['pubdate']
				print news['addtime']
		        	#将每个小时刷新一次新闻
				stmt = 'insert into news_info(NewsTitle,NewsContent,NewsDate,NewsSource,NewsLogo,NewsSort,NewsAddTime) values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',,\'%s\')' % (news['title'],news['content'],news['pubdate'],news['source'],news['logo'],news['sort'],news['addtime']) 
        			newsDAO(stmt)
				print "insert success %s" % (job)

    def getallnews(self):
    		job = urlqueue.get()
    		text = urlopen(job).read()
    		soup = BeautifulSoup(text.decode('gb2312','ignore'))
		if self.name == "chinabyte":
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
		elif self.name == "sina":
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
