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

		#显示具体的新闻
		(r'^news/(\d+)/$', views.news),

		#信息检索
		(r'^search/$', views.search),		

		#信息检索结果
		(r'^search_result/$', views.search_result),		

		#数据统计与分析
		(r'^statistics/$', views.statistics),
		
		#显示例子
		(r'^example/$',views.example),		

		#新闻界面
		(r'^listnews/(.+)/$', views.listnews),
		
		#项目界面
		(r'^listproject/(.+)/$',views.listproject),

		#显示具体的项目
		(r'^project/(.+)/$',views.project),
		
		#基本信息
		(r'^base/', views.base),
	
		#使用bootstrap-datepicker.css             
                (r'^bootstrap-datetimepicker/css/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': '/liuzp/NSTC_DataCrawl/DataCrawl/djcode/website/css/bootstrap-datetimepicker/css/'}),

		#使用bootstrap-datepicker.js 
                (r'^bootstrap-datetimepicker/js/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': '/liuzp/NSTC_DataCrawl/DataCrawl/djcode/website/css/bootstrap-datetimepicker/js/'}), 		
	
		#使用bootstrap.css
    		(r'^bootstrap/css/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': '/liuzp/NSTC_DataCrawl/DataCrawl/djcode/website/css/bootstrap/css/'}),
	
		#使用bootstrap.js
		(r'^bootstrap/js/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': '/liuzp/NSTC_DataCrawl/DataCrawl/djcode/website/css/bootstrap/js/'}),

		#使用图片
		(r'^images/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/liuzp/NSTC_DataCrawl/DataCrawl/djcode/website/images/' }),

		#使用fonts中的小图标
             	(r'^fonts/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': '/liuzp/NSTC_DataCrawl/DataCrawl/djcode/website/css/bootstrap/fonts/'}),
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
