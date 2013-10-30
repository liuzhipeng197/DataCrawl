#encoding=utf-8
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import urllib
import time
import re
from datetime import date

class MostProjectParser():
	def __init__(self):
		pass

	def projectparser(self,soup,url,now_time):
	    '''
	    url作为保存在hbase中的row_key
	    '''
	    projectcontents = ''
	    projecttitle = ''
	    pubdate = ''
	
	    #得到文章的标题
	    contenttitle = soup.find('div',id='Title')
	    projecttitle = str(contenttitle.getText().encode('utf-8')).replace('&nbsp;','')
	    print projecttitle
		 
	    #得到文章的日期
	    res = '<div class="gray12 lh22">.*日'
	    match = re.findall(res, str(soup))
	    if len(match)>0:
		project_time = match[0]	   
	    else:
		print 'error'

	    time_array = project_time.split('：')[1].split('日')[0]
	    year = time_array.split('年')[0]
	    month = time_array.split('年')[1].split('月')[0]
	    day = time_array.split('年')[1].split('月')[1]
	    project_date = year + '-'+ month + '-' + day
	   
	    #得到文章的正文
	    if project_date == now_time:
		contentbody = soup.find('div',id="Zoom")
	    	if contentbody:
			p = contentbody.find('p')
			if not p.find('div'):
				projectcontents += '  '+str(p.getText().encode('utf-8'))+'\n'
			while p.findNextSibling('p'):
				p = p.findNextSibling('p')
				if not p.find('div'):
					projectcontents += '  '+str(p.getText().encode('utf-8'))+'\n'
		project = dict()
		project['title'] = projecttitle
		project['pubdate'] = project_date
		project['content'] = projectcontents
		project['source'] = '科学技术部'
		project["logo"] = 'most' 
		return project

if __name__ == "__main__":

    url='http://www.most.gov.cn/tztg/201310/t20131021_109850.htm'
    now_time = date.isoformat(date.today()) 
    text = urlopen(url).read()
    soup = BeautifulSoup(text,fromEncoding="gb18030")
    mpp = MostProjectParser()
    project = mpp.projectparser(soup,url,now_time)
    print '[NEWS]\ttitle: %s\n\t\tpublish date: %s\n\t\tcontents: %s\n' % (project['title'],project['pubdate'],project['content'])
