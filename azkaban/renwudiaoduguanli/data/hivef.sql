-- 切换到default数据库
use default;
-- 如果student表存在则删除
drop table if exists student;
-- 创建student管理表
create table if not exists student(id int, name string)
row format delimited fields terminated by '\t';
-- 加载本地数据到student管理表
load data local inpath '/root/data/student.txt' into table student;
-- 往student管理表中插入一行数据
insert into student values(1100,"qingjiao");
-- 查询student表所有数据，并将查询结果导出到本地文件系统的/root/data/student目录下
insert overwrite local directory '/root/data/student'
row format delimited fields terminated by '\t'
select * from student;
