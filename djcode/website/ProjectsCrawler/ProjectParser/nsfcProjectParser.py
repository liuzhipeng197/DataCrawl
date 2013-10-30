#encoding=utf-8
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import urllib
import time
import re
from datetime import date

class NsfcProjectParser():
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
	    contenttitle = soup.find('div',id='nr_top')
	    projecttitle = str(contenttitle.getText().encode('utf-8')).replace('&nbsp;','')
	    print projecttitle
		 
	    #得到文章的日期
	    res = '<p align="center">.*?摘自'
	    match = re.findall(res, str(soup))
	    if len(match)>0:
		project_time = match[0]	   
	    else:
		return None

	    time_array = project_time.split('摘')[0].split('时间:')[1][0:10]
	    project_date = time_array
	   
	    #得到文章的正文
	    if project_date == now_time:
		contentbody = soup.find('div',id="nr2")
	    	if contentbody:
			p = contentbody.find('p')
			if not p.find('meta'):
				projectcontents += '  '+str(p.getText().encode('utf-8'))+'\n'+'\n'
			while p.findNextSibling('p'):
				p = p.findNextSibling('p')
				if not p.find('meta'):
					projectcontents += '  '+str(p.getText().encode('utf-8'))+'\n'+'\n'
		project = dict()
		project['title'] = projecttitle
		project['pubdate'] = project_date
		project['content'] = projectcontents
		project['source'] = '国家自然科学基金委员会'
		project["logo"] = 'nsfc' 
		return project

if __name__ == "__main__":

    url='http://www.nsfc.gov.cn/Portal0/InfoModule_396/52455.htm'
    now_time = date.isoformat(date.today()) 
    text = urlopen(url).read()
    soup = BeautifulSoup(text,fromEncoding="gb18030")
    mpp = NsfcProjectParser()
    project = mpp.projectparser(soup,url,now_time)
    print '[NEWS]\ttitle: %s\n\t\tpublish date: %s\n\t\tcontents: %s\n' % (project['title'],project['pubdate'],project['content'])
