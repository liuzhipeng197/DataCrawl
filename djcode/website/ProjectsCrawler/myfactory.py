#encoding=utf-8
from ProjectParser.mostProjectParser import MostProjectParser as MPP
from ProjectParser.nsfcProjectParser import NsfcProjectParser as NPP

class MyFactory():
	#初始化对象
	def __init__(self,classname):
		self.classname = classname

	'''
	#产生实体类的实例化对象
	def createElement(self):
		#根据classname得到相应的类的实例化对象
		if self.classname == 'sina':
			return SUP()
		elif self.classname == 'chinabyte':
			return CUP()
		else:
			print "error"
	'''

	#根据名称得到相应的解析文件
	def createProjectParser(self):
		if self.classname == "most":
			return MPP()
		elif self.classname == "nsfc":
			return NPP()
		else:
			print "error"

	
if __name__ == '__main__':
	mf = MyFactory('chinabyte')
	element = mf.createElement()
	element.test()		 
