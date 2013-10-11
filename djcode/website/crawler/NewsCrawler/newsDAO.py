#encoding=utf-8
import MySQLdb
import sys
import _mysql

def newsDAO(stmt):
    try:
        reload(sys)
        sys.setdefaultencoding('utf-8')
	conn = MySQLdb.connect(host="192.168.1.170",user="hive",passwd="123456",db="datacrawldb",charset="utf8")
        conn.query(stmt)
        conn.close()
    except _mysql.Error,e:
        print "Error %d: %s" %(e.args[0],e.args[1])
    
if __name__ == "__main__":
    title = '你好'
    content = 'hello world'
    date = '2011-12-07'  #date
    stmt = 'insert into NEWS (NEWS_TITLE,NEWS_CONTENT,NEWS_PUBLISHDATE) values(\'%s\',\'%s\',\'%s\')' % (title,content,date)
    newsDAO(stmt)
