#Create your views here.
#encoding=utf-8
# Create your views here.
from models import *

def getAllProject():
	project_list = []
	project_list = Info.objects.all().order_by('-ProjectDate')
	return project_list

#根据新闻的种类得到所有的新闻
def getProjectBySort(name):
	project = list(Info.objects.filter(ProjectSort=name).order_by('-ProjectDate'))
	return project

def getKeyWordByName(name):
	KeyWords_list = KeyWord.objects.filter(PkeyClassified = name)
	
	keywords = []
	for k in KeyWords_list:
		keywords.append(k.PkeyWord)
	return keywords

def getProjectById(id):
	project = Info.objects.get(id = id)
	return project

#执行一个忽略大小写的内容包含检测，返回包含keywords关键字的所有新闻列表
def getProjectByTitle(keywords):
	project_list = Info.objects.filter(ProjectTitle__icontains = keywords).order_by('-ProjectDate')
	return project_list

#根据项目的来源、新闻的发表时间和新闻的内容进行过滤                                                                                                           
def getProjectByQueryConditions(keyword,source,begintime,endtime):
	project_list = Info.objects.filter(ProjectTitle__icontains = keyword).filter(ProjectSource__icontains = source).filter(ProjectDate__range = (begintime,endtime))	
	return project_list 	

if __name__ == '__main__':
	projectlist = []
	getAllProject()
