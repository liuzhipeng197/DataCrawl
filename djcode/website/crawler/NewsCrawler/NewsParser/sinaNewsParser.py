#encoding=utf-8
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import urllib
import time

def sinaNewsParser(soup,url,now_time):
    '''
    url作为保存在hbase中的row_key
    '''
    newscontents = ''
    newstitle = ''
    pubdate = ''
    urlimage = ''
    contenttitle = soup.find('h1',id='artibodyTitle')
    vediotitle = soup.find('div',id='videoTitle')
    date = soup.find('span',id='pub_date')
    
    if contenttitle:
        newstitle = str(contenttitle.getText().encode('utf-8')).replace('&nbsp;','')
    elif vediotitle:
        newstitle = str(vediotitle.getText().encode('utf-8'))
    if date:
        pubdate = str(date.getText().encode('utf-8').replace('&nbsp;',''))
    
    news_time = pubdate
    time_array = news_time.split('日')                                                                                                                                                            
    hour = time_array[1].split(':')[0]                                                                                                                                                            
    minute = time_array[1].split(":")[1]                                                                                                                                                          
    news_time = int(hour) *60 + int(minute)                                                                                                                                                       
    if now_time - news_time <= 60:  
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
    	news['title'] = newstitle
    	news['pubdate'] = pubdate
    	news['content'] = newscontents
	news['source'] = '新浪科技'
   	news["logo"] = 'sina' 
    	return news
    
if __name__ == "__main__":

    url='http://tech.sina.com.cn/i/2013-06-08/15448427173.shtml'
    now_time = time.localtime().tm_hour*60 + time.localtime().tm_min   
 
    text = urlopen(url).read()
    soup = BeautifulSoup(text,fromEncoding="gb18030")
    news = sinaNewsParser(soup,url,now_time)
    print '[NEWS]\ttitle: %s\n\t\tpublish date: %s\n\t\tcontents: %s\n' % (news['title'],news['pubdate'],news['content'])
