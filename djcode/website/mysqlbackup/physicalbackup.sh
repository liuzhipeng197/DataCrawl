#!/bin/bash
#基本的参数配置
#备份文件存放路径
backup_target_dir=/backup/db
backup_compression_dir=/backup/compressiondb
db=datacrawldb


#复制数据库文件
mysqlhotcopy -u hive -p 123456 $db $backup_target_dir

#将文件在本地进行压缩
DATE=$(date +%Y%m%d)
cd $backup_compression_dir
tar -zcvf $backup_compression_dir/$db$DATE.tar.gz $backup_target_dir/$db

#删除本地的源文件
rm -rf $backup_target_dir/$db/

#将数据备份至hadoop00的机器上
scp -r $backup_compression_dir/$db$DATE.tar.gz root@hadoop00:$backup_compression_dir

#删除本地的压缩文件
rm -rf $backup_compression_dir/$db$DATE.tar.gz 

#删除10天前的压缩数据
ccDATE=$(date "-d 10 day ago" +%Y%m%d)
ssh hadoop00 rm -rf $backup_compression_dir/$db$ccDATE.tar.gz
