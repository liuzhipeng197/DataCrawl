#encoding=utf-8
from NewsParser.chinabyteNewsParser import chinabyteNewsParser as CNP
from NewsParser.sinaNewsParser import sinaNewsParser as SNP

class MyFactory():
	#初始化对象
	def __init__(self,classname):
		self.classname = classname

	#产生实体类的实例化对象
	def createElement(self):
		#根据classname得到相应的类的实例化对象
		if self.classname == 'sina':
			return SUP()
		elif self.classname == 'chinabyte':
			return CUP()
		else:
			print "error"

	def createNewsParser(self):
		if self.classname == "sina":
			return SNP()
		elif self.classname == "chinabyte":
			return CNP()
		else:
			print "error"

	
if __name__ == '__main__':
	mf = MyFactory('chinabyte')
	element = mf.createElement()
	element.test()		 
