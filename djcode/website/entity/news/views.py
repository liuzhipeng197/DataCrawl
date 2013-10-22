#encoding=utf-8
# Create your views here.
from entity.news.models import Info

def getAllNews():
	news_list = []
	news_list = Info.objects.all().order_by('-NewsDate')
	return news_list

def getNewsById(id):
	news = Info.objects.get(id = id)
	return news

#执行一个忽略大小写的内容包含检测，返回包含keywords关键字的所有新闻列表
def getNewsByTitle(keywords):
	news_list = Info.objects.filter(NewsTitle__icontains = keywords).order_by('-NewsDate')
	return news_list
	
if __name__ == '__main__':
	newslist = []
	getAllNews()
