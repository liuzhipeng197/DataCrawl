#encoding=utf-8
from django.conf.urls import patterns, include, url
from website import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login,logout

admin.autodiscover()

urlpatterns = patterns('',
		#登陆
		(r'^accounts/login/$',login),

		#退出
		(r'^accounts/logout/$',logout),

		#主界面
		(r'^main/$',views.main),

		#使用管理界面
		(r'^admin/', include(admin.site.urls)),

		#新闻界面
		(r'^listnews/$', views.listnews),
		
		#基本信息
		(r'^base/', views.base),
		
		#使用bootstrap.css
    		(r'^css/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': '/liuzp/DataCrawl/djcode/website/css/bootstrap/css/'}),
	
		#使用bootstrap.js
		(r'^js/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': '/liuzp/DataCrawl/djcode/website/css/bootstrap/js/'}),

		#使用图片
		( r'^images/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/liuzp/DataCrawl/djcode/website/images/' }),

		#使用fonts中的小图标
             	(r'^fonts/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': '/liuzp/DataCrawl/djcode/website/css/bootstrap/fonts/'}),
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
