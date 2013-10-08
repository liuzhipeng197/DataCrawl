#encoding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from dboperation.user import isuserexist
from users.models import User
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
def listnews(request):
	return render_to_response("listnews.html")

def logout_view(request):
	logout(request)
	return render_to_response("registration/login.html")
