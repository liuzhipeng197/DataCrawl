#encoding=utf-8
import xml.etree.ElementTree as ET
from UrlCrawler.urlcrawler import UrlParser

#新建xml文件
def buildNewsXmlFile():
	#设置一个新节点，并设置其标签为root
	root = ET.Element("root")

	#在root下新建两个子节点,设置其名称分别为sina和chinabyte
	sina = ET.SubElement(root, "sina")
	chinabyte = ET.SubElement(root, "chinabyte")

	#在sina下新建一个子节点url
	sina_url = ET.SubElement(sina, "url")
	sina_url.text = "http://roll.tech.sina.com.cn/internet_all/index_1.shtml"

	#在chinabyte下新建一个子节点url
	chinabyte_url = ET.SubElement(chinabyte, "url")
	chinabyte_url.text = "http://www.chinabyte.com/more/124566.shtml"

	#将节点数信息保存在ElementTree中，并且保存为XML格式文件
	tree = ET.ElementTree(root)
	tree.write("urlfile.xml")

#解析xml中的所有的节点
def parseAllTags(xml_name):
	tree = ET.parse(xml_name)
	root = tree.getroot()
	
	urls = []
	#输入root的所有子节点
	for child in root:
		print child.tag
		'''
		mf = MyFactory(child.tag)
		element = mf.createElement()
		for sub_tag in child:
			urls.append(sub_tag.text)
		element.test(urls)
		'''
		element = UrlParser(child.tag)
		for sub_tag in child:
			urls.append(sub_tag.text)
		element.test(urls)


#解析Xml文件中指定tag的节点
def parseXmlFile(xml_name, tag):
	#将XMl文件加载并返回一个ELementTree对象
	tree = ET.parse(xml_name)
	
	#得到第一个匹配sina标签的Element对象
	sina = tree.find(tag)
	urls =[]

	#得到tag的SubElement
	for sub_tag in sina:
		if sub_tag.tag != "number":
			urls.append(sub_tag.text)
	
	#返回指定的tag的url地址
	return urls
	'''	
	for m in urls:
		print m
	'''

#在XML文件后面添加节点
def editXmlFile(xml_name, tag, url):
	tree = ET.parse(xml_name)
	
	#得到根节点的element对象
	root = tree.getroot()
	
	#在root节点下添加标签名称为tag的子标签，子标签有两个子标签，分别为number和url
	if root.find(tag):
		new_node = root.find(tag)
		new_url = ET.SubElement(new_node, "url")
        	new_url.text = url
	else:
		new_node = ET.SubElement(root, tag)
		new_url = ET.SubElement(new_node, "url")
		new_url.text = url
	
	tree = ET.ElementTree(root)
	tree.write(xml_name)
	
	
if __name__ == "__main__":
	#buildNewsXmlFile()
	#parseXmlFile("urls.xml", "sina")
	parseAllTags("/liuzp/NSTC_DataCrawl/DataCrawl/djcode/website/ProjectsCrawler/urlfile.xml")
