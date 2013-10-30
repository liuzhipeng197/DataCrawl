#encoding=utf-8
from newsDAO import newsQuery
class NewsClassify():
	def __init__(self):
		pass

	def classify(self,newstitle):
		cloud = newsQuery("select NkeyWord from news_keyword where NkeyClassified ='cloud'")
		storage = newsQuery("select NkeyWord from news_keyword where NkeyClassified ='storage'")
		bigdata = newsQuery("select NkeyWord from news_keyword where NkeyClassified ='bigdata'")
		datacenter = newsQuery("select NkeyWord from news_keyword where NkeyClassified ='datacenter'")
		test = newsQuery("select NkeyWord from news_keyword where NkeyClassified ='test'")
		
		newsclassified = "others"
		for m in range(0,5): 
			for i in cloud:
				if newstitle.find(i[0]) > -1:
					newsclassified = "cloud"
					break

			for i in storage:
				if newstitle.find(i[0]) > -1:
					newsclassified = "storage"
					break
			for i in bigdata:
				if newstitle.find(i[0]) > -1:
					newsclassified = "bigdata"
					break

			for i in datacenter:
				if newstitle.find(i[0]) > -1:
					newsclassified = "datacenter"
					break
			for i in test:
				if newstitle.find(i[0]) > -1:
					newsclassified = "test"	
					break

		print newsclassified
		return newsclassified

if __name__ == "__main__":
	nc = NewsClassify()
	nc.classify("IaaS")	

