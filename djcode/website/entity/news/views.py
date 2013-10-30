#encoding=utf-8
# Create your views here.
from models import *

def getAllNews():
	news_list = []
	news_list = Info.objects.all().order_by('-NewsDate')
	return news_list

#根据新闻的种类得到所有的新闻
def getNewsBySort(name):
	news = list(Info.objects.filter(NewsSort=name).order_by('-NewsDate'))
	return news

def getKeyWordByName(name):
	KeyWords_list = KeyWord.objects.filter(NkeyClassified = name)
	
	keywords = []
	for k in KeyWords_list:
		keywords.append(k.NkeyWord)
	return keywords

def getNewsById(id):
	news = Info.objects.get(id = id)
	return news

#执行一个忽略大小写的内容包含检测，返回包含keywords关键字的所有新闻列表
def getNewsByTitle(keywords):
	news_list = Info.objects.filter(NewsTitle__icontains = keywords).order_by('-NewsDate')
	return news_list

#根据新闻的来源、新闻的发表时间和新闻的内容进行过滤
def getNewsByQueryConditons(keyword, source, begintime, endtime):
	news_list = Info.objects.filter(NewsTitle__icontains = keyword).filter(NewsSource__icontains = source).filter(NewsDate__range = (begintime, endtime))
	return news_list

	
if __name__ == '__main__':
	newslist = []
	getAllNews()
