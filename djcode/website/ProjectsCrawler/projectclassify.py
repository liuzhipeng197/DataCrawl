#encoding=utf-8
from projectDAO import projectQuery
class ProjectClassify():
	def __init__(self):
		pass

	def classify(self,projecttitle):
		cloud = projectQuery("select PkeyWord from project_keyword where PkeyClassified ='cloud'")
		storage = projectQuery("select PkeyWord from project_keyword where PkeyClassified ='storage'")
		bigdata = projectQuery("select PkeyWord from project_keyword where PkeyClassified ='bigdata'")
		projectapply = projectQuery("select PkeyWord from project_keyword where PkeyClassified ='projectapply'")
		test = projectQuery("select PkeyWord from project_keyword where PkeyClassified ='test'")
		
		projectclassified = "others"
		for m in range(0,5): 
			for i in cloud:
				if projecttitle.find(i[0]) > -1:
					projectclassified = "cloud"
					break

			for i in storage:
				if projecttitle.find(i[0]) > -1:
					projectclassified = "storage"
					break
			for i in bigdata:
				if projecttitle.find(i[0]) > -1:
					projectclassified = "bigdata"
					break

			for i in projectapply:
				if projecttitle.find(i[0]) > -1:
					projectclassified = "projectapply"
					break
			for i in test:
				if projecttitle.find(i[0]) > -1:
					projectclassified = "test"	
					break

		print projectclassified
		return projectclassified

if __name__ == "__main__":
	nc = NewsClassify()
	nc.classify("IaaS")	

