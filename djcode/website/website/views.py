#encoding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
#pagination
from django.core.paginator import Paginator,InvalidPage,EmptyPage
from entity.users.models import User
from entity.news.models import Info
from entity.news.views import getAllNews
from entity.news.views import getNewsById
from entity.news.views import getNewsByTitle
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login,logout
import datetime

@login_required(login_url='/accounts/login')
def base(request):
	return render_to_response("base.html")

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


@login_required(login_url='/accounts/login')
def listnews(request, offset):
	if offset =='all':
		newslist = getAllNews()
		my_title = "新闻列表"
	else:
		newslist = getNewsByTitle(offset)
		my_title = offset
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

@login_required(login_url='/accounts/login')
def news(request, offset):
	news = getNewsById(offset)
	return render_to_response("news.html",{'news':news})

def logout_view(request):
	logout(request)
	return render_to_response("registration/login.html")

