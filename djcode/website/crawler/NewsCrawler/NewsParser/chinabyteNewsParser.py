#:encoding=utf-8
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import urllib
import time
import re
from datetime import date

def chinabyteNewsParser(soup,url,now_time):
    '''
    url作为保存在hbase中的row_key
    '''
    newscontents = ''
    newstitle = ''
    pubdate = ''
    urlimage = ''
    contenttitle = soup.find('h1',id='artibodyTitle')
    vediotitle = soup.find('div',id='videoTitle')
    
    res = r'<span class="date">.*?<\/span>'
    match = re.findall(res,str(soup))
    
    #找到文章的出处
    res_resource = r'<span class="where">.*?<\/span>'
    match_resource = re.findall(res_resource,str(soup))
    resource = match_resource[0]
    if resource == "论坛" or resource == "比特网":
        source = "比特网"
    	logo = "chinabyte"	  
    elif resource == "中关村在线":
	source = "中关村在线"
	logo = "zol"
    elif resource == "TT虚拟化" or resource == "TechTarget中国":
	source = "TT中国"
	logo = "techtarget"
    elif resource == "51cto":
   	source = "51cto"
	logo = "51cto"
    else:
	source = "比特网"
	logo = "chinabyte"
    
    if len(match)>0:
    	time_array = match[0].split('>')[1][0:16]
    else:
	return None
 
    if contenttitle:
        newstitle = str(contenttitle.getText().encode('utf-8')).replace('&nbsp;','')
    elif vediotitle:
        newstitle = str(vediotitle.getText().encode('utf-8'))
 
    pubdate = time_array[0:16]    
	
    news_date = pubdate[0:10]

    hour = time_array[11:13]
    minute = time_array[14:16]

    now_date = date.isoformat(date.today())
    news_time = int(hour) *60 + int(minute)                                                                                                                                                       
    if now_time - news_time <= 60 and now_date == news_date:  
    	contentbody = soup.find('div',id="artibody")
    	vediobody = soup.find('td',id='videoContent')


	if contentbody:
        	p = contentbody.find('p')
        	if not p.find('script'):
            		newscontents += '  '+str(p.getText().encode('utf-8'))+'\n'+'\n'
        	while p.findNextSibling('p'):
            		p = p.findNextSibling('p')
            		if not p.find('script'):
                		newscontents += '  '+str(p.getText().encode('utf-8'))+'\n'+'\n'
    	elif vediobody:
        	p = vediobody.find('p')
        	if not p.find('script'):
            		newscontents += str(p.getText().encode('utf-8'))
        	while p.findNextSibling('p'):
            		p = p.findNextSibling('p')
            		if not p.find('script'):
                		newscontents += str(p.getText().encode('utf-8'))
    	news = dict()
	pubdate = pubdate[0:4]+'年'+pubdate[5:7]+'月'+pubdate[8:10]+'日'+ time_array[11:16]
    	news['title'] = newstitle
    	news['pubdate'] = pubdate
    	news['content'] = newscontents
	news['source'] = source
        news['logo'] = logo
    
    	return news
    
if __name__ == "__main__":

    url='http://storage.chinabyte.com/165/12751665.shtml'
    now_time = time.localtime().tm_hour*60 + time.localtime().tm_min   
 
    text = urlopen(url).read()
    soup = BeautifulSoup(text.decode('gb2312','ignore'))
    #news = chinabyteNewsParser(soup,url,now_time)
    print soup.originalEncoding
    print soup.prettify()
    #print '[NEWS]\ttitle: %s\n\t\tpublish date: %s\n\t\tcontents: %s\n' % (news['title'],news['pubdate'],news['content'])
