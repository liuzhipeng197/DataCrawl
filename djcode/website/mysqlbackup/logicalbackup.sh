#!/bin/bash
backup_compression_dir=/backup/logicalbackup
db=datacrawldb

#复制数据库文件
mysqldump -uhive -p123456 $db > $db.sql

#将文件压缩
DATE=$(date +%Y%m%d)
tar -zcvf $db$DATE.tar.gz $db.sql

#将文件备份至hadoop00服务器上
scp $db$DATE.tar.gz root@hadoop00:$backup_compression_dir

#删除源文件
rm -rf $db.sql
rm -rf $db$DATE.tar.gz

#删除上次的压缩数据
ccDATE=$(date "-d 7 day ago" +%Y%m%d)
ssh hadoop00 rm -rf $backup_compression_dir/$db$ccDATE.tar.gz
