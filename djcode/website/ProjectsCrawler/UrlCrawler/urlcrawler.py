#encoding=utf-8
import re
import time
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import re,sys,Queue,datetime,time
import threading,mutex
from projectDAO import projectDAO
import urlparse 
from myfactory import MyFactory 
from projectclassify import ProjectClassify
from datetime import date
 
#unique url set
urlset = set()
#parser url job queue
urlqueue = Queue.Queue()


class UrlParser():
    def __init__(self,name):
	self.name = name
	mf = MyFactory(name)
	self.ProjectParser = mf.createProjectParser() 

    def flushtime(self,project,job,now_time):
   	pass
 
    def run(self):
        while urlqueue.empty()==False:
		job = urlqueue.get()
        	today = datetime.date.today()
                text = urlopen(job).read()
		print self.name
                if self.name == "most":
			soup = BeautifulSoup(text.decode('gb2312','ignore'))
	        elif self.name == "nsfc":
			soup = BeautifulSoup(text,fromEncoding="gb18030")
	
		now_time = date.isoformat(date.today())

                if job:
		    project = self.ProjectParser.projectparser(soup,job,now_time)
		    if project:
		    	print project['pubdate']
			
			#分类
			nc = ProjectClassify()
			project['sort'] = nc.classify(project['title'])
			
			if project['sort'] == 'others':
				pass
			else:
		        	project_time = project['pubdate']
		        	#将每个小时刷新一次新闻
				stmt = 'insert into project_info(ProjectTitle,ProjectContent,ProjectDate,ProjectSource,ProjectLogo,ProjectSort) values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' % (project['title'],project['content'],project['pubdate'],project['source'],project['logo'],project['sort'])                                                          
        			projectDAO(stmt)
				print "insert success %s" % (job)

    def getallproject(self):
    		job = urlqueue.get()
    		text = urlopen(job).read()
    		soup = BeautifulSoup(text.decode('gb2312','ignore'))
		if self.name == "most":
			for header in soup('a'):
				#<a>label which has href attribute
				if header.has_key('href'):
				#strip whitespace before or after the string
					url = header['href'].encode('utf8').strip()
					#if the string begins with 'http://' or 'https://'and isn't in the urlset
					pattern = re.compile('^\./(\d{6})/')
					if pattern.match(url) and url not in urlset:
						url = "http://www.most.gov.cn/tztg/" + url[2:] 
						urlqueue.put(url)
						urlset.add(url)
						print url
		elif self.name == "nsfc":
			for header in soup('a'):
				#<a>label which has href attribute
				if header.has_key('href'):
				#strip whitespace before or after the string
					url = header['href'].encode('utf8').strip()
					#if the string begins with 'http://' or 'https://'and isn't in the urlset
					pattern = re.compile('/Portal0/InfoModule_396/(\d)+')
					if pattern.match(url) and url not in urlset:
						url = "http://www.nsfc.gov.cn"+url
						urlqueue.put(url)
						urlset.add(url)		 
						print url
    def test(self,urls):
		for url in urls:
    			urlset.add(url)
    			urlqueue.put(url)
    			#urlparser = UrlParser()	
			self.getallproject()
    			self.run()

if __name__ == '__main__':
	url ="http://www.nsfc.gov.cn/Portal0/InfoModule_396/More.htm"
	urls = []
	urls.append(url)
	urlparser = UrlParser("nsfc")
	urlparser.test(urls)
