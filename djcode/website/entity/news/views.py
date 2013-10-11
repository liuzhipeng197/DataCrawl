# Create your views here.
from entity.news.models import Info

def getAllNews():
	news_list = []
	news_list = Info.objects.all().order_by('-NewsDate')
	return news_list

def getNewsById(id):
	news = Info.objects.get(id = id)
	return news
	
if __name__ == '__main__':
	newslist = []
	getAllNews()
