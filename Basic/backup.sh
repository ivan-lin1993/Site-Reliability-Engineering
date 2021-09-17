#!/bin/sh

filename=mysql-$(date +%Y%m%d%H)-employees.sql
mysqldump -h 127.0.0.1 -uroot -p -P3307 employees > $filename
tar czvf $filename.tar.gz $filename
rm $filename
find . -type f -mtime +7 -name 'mysql-*-employees.sql.tar.gz' -execdir rm -- '{}' \;
