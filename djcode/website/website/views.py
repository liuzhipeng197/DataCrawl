#encoding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
#pagination
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from entity.users.models import User
from entity.news.models import Info
'''
from entity.news.views import getAllNews
from entity.news.views import getNewsById
from entity.news.views import getNewsByTitle
from entity.news.views import getNewsById                                                                                                                     
from entity.news.views import getNewsBySort
'''
from entity.project.views import *
from entity.news.views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login,logout
import datetime

#显示模板页的view函数
@login_required(login_url='/accounts/login')
def base(request):
	return render_to_response("base.html")

#显示主界面的view函数
@login_required(login_url='/accounts/login')
def main(request):
	'''	
	if 'inputUser' in request.GET:
		name = request.GET['inputUser']
	else:
		name = 'You submitted an empty form.'

	if 'inputPassword' in request.GET:
		pwd = request.GET['inputPassword']
	else:
		pwd = 'error'

	user = User(username = name, password = pwd)
	
	if(isuserexist(user) == 'True'):
		return render_to_response('main.html',{'User':name,'Password':pwd})
	else:
		return render_to_response('login.html',{'Message':'用户或者密码不正确'})
	'''
	return render_to_response('main.html')

#显示新闻列表的view函数
@login_required(login_url='/accounts/login')
def listnews(request, offset):
	'''
	if request.GET['inputCondition']:
		condition = request.GET['inputCondition']
		newslist = getNewsByTitle(condition)	
	'''
	if offset =='all':
		newslist = getAllNews()
	else:
		newslist = getNewsBySort(offset)
		my_title = offset

	if offset == 'all':                                                                                                                                   
                my_title = "所有新闻"                                                                                                                         
        elif offset =='storage':                                                                                                                          
                my_title = "存储新闻"                                                                                                                     
        elif offset =='test':                                                                                                                         
                my_title = "测试新闻"                                                                                                                     
        elif offset =='cloud':                                                                                                                      
                my_title = "云计算新闻"                                                                                                                     
        elif offset =='bigdata':                                                                                                                              
                my_title = "大数据新闻"                                                                                                               
        elif offset =='datacenter':                                                                                                                         
                my_title = "数据中心新闻"                                                                                                                     
        else:                                                                                                                                                 
                my_title = "其它新闻"

	#Pagination"Show 25 examples per page"
	paginator = Paginator(newslist,10)
	#Make sure page request is an int.If not,deliver first page.
	try:
		page = int(request.GET.get('page','1'))
	except ValueError:
		page = 1

	#if page request is out of range, deliver last page of results
	try:
		newslist = paginator.page(page)
	except(EmptyPage, InvalidPage):
		newslist = paginator.page(paginator.num_pages)
		
	return render_to_response("listnews.html",{'newslist':newslist,'my_title':my_title})

#显示新闻内容的view函数
@login_required(login_url='/accounts/login')
def news(request, offset):
	news = getNewsById(offset)
	return render_to_response("news.html",{'news':news})

#退出系统的view函数
def logout_view(request):
	logout(request)
	return render_to_response("registration/login.html")

#显示项目列表的view函数
@login_required(login_url ='/accouts/login')
def listproject(request,offset):
	'''
        if request.GET['inputCondition']:
                condition = request.GET['inputCondition']
                newslist = getNewsByTitle(condition)    
        '''
        if offset =='all':
                projectlist = getAllProject()
        else:   
                projectlist = getProjectBySort(offset)
                my_title = offset

	if offset == 'all':
		my_title = "所有项目"
	elif offset =='test':
                my_title = "测试项目"
	elif offset =='softwaredevelop':
                my_title = "软件研发项目"
	elif offset =='bigdata':
                my_title = "大数据和云计算项目"
	elif offset =='projectapply':
                my_title = "科研项目申请"
	elif offset == 'storage':
		my_title = '存储项目'
	else:
		my_title = "其它项目"

        #Pagination"Show 25 examples per page"
        paginator = Paginator(projectlist,10)
        #Make sure page request is an int.If not,deliver first page.
        try:
                page = int(request.GET.get('page','1'))
        except ValueError:
                page = 1

        #if page request is out of range, deliver last page of results
        try:
                projectlist = paginator.page(page)
        except(EmptyPage, InvalidPage):
                projectlist = paginator.page(paginator.num_pages)

        return render_to_response("listproject.html",{'projectlist':projectlist,'my_title':my_title})

#显示项目的view函数
@login_required(login_url='/accounts/login')
def project(request, offset):
        project = getProjectById(offset)
	
	#转化正文的内容
	contents = project.ProjectContent.split("&nbsp;")
        m = 0
	tem_content=""
  	for i in contents:
		if i:
			tem_content=tem_content+i
			m=0
		elif m==0:
			tem_content=tem_content+'\n\n'
			m=1
			
	content = tem_content.replace(' ','')
	return render_to_response("project.html",{'project':project,'content':content})

#显示信息统计的view函数
@login_required(login_url='/accounts/login')
def search(request):
	'''
	if request.method == 'GET':
		basic_content = request.GET.get('optionsRadios')
		keyword = request.GET.get('keyword')
		source = request.GET.get('source')
		begintime = str(request.GET.get('datetimepicker'))
		endtime = str(request.GET.get('datetimepicker1'))

		begin = begintime[0:4] + '年' + begintime[5:7] + '月' + begintime[8:10] + '日'
		end = endtime[0:4] + '年' + endtime[5:7] + '月' + endtime[8:10] + '日'	
		#判断是新闻检索还是项目的检索
		list = []	
		if basic_content == 'option1':
			list = getNewsByQueryConditons(keyword, source, begin, end)
			type = 'news'
		else:
			type = '项目'

		#Pagination"Show 25 examples per page"
        	paginator = Paginator(list,10)
        	#Make sure page request is an int.If not,deliver first page.
        	try:
                	page = int(request.GET.get('page','1'))
        	except ValueError:
                	page = 1

        	#if page request is out of range, deliver last page of results
        	try:
                	list = paginator.page(page)
        	except(EmptyPage, InvalidPage):
                	list = paginator.page(paginator.num_pages)
		
		return render_to_response("search.html",{'list':list,'type':type,'begintime':begin,'endtime':end})
	else:
	'''
	return render_to_response("search.html")

#显示列子的view函数
def example(request):
	return render_to_response("example.html")

#显示信息统计与分析页面的view函数
@login_required(login_url='/accounts/login')
def statistics(request):
	return render_to_response("statistics.html")

#显示查询结果的view函数
@login_required(login_url='/accounts/login')
def search_result(request):
	basic_content = request.GET.get('optionsRadios')
	keyword = request.GET.get('keyword')
	source = request.GET.get('source')
	begintime = str(request.GET.get('datetimepicker'))
	endtime = str(request.GET.get('datetimepicker1'))

	begin = begintime[0:4] + '年' + begintime[5:7] + '月' + begintime[8:10] + '日'
	end = endtime[0:4] + '年' + endtime[5:7] + '月' + endtime[8:10] + '日'

	begin_p = begintime[0:4] + '-' + begintime[5:7] + '-' + begintime[8:10]
	end_p = endtime[0:4] + '-' + endtime[5:7] + '-' + endtime[8:10]

	#判断是新闻检索还是项目的检索                                                                                                                 
	list = []
	if basic_content == 'option1':
		list = getNewsByQueryConditons(keyword, source, begin, end)
		type = 'news'
	else:
		type = 'project'
		list = getProjectByQueryConditions(keyword,source,begin_p,end_p)

      	#Pagination"Show 25 examples per page"                                                                                                        
       	paginator = Paginator(list,10)
        #Make sure page request is an int.If not,deliver first page.                                                                                  
       	try:
        	page = int(request.GET.get('page','1'))
      	except ValueError:
             	page = 1

     	#if page request is out of range, deliver last page of results                                                                                
       	try:
        	list = paginator.page(page)
       	except(EmptyPage, InvalidPage):
       		list = paginator.page(paginator.num_pages)

       	return render_to_response("search_result.html",{'list':list,'type':type,'begintime':begin,'endtime':end,'request':request})
