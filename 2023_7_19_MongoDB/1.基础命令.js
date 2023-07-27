// 如何进入到mongo数据库交互环境
mongo

// 查询mongo中已经存在的数据库
show dbs

// 进入到指定数据库中
// use 集合名称
use admin

// 查询当前位于哪个数据库中
db


// 进入到自定义数据库中  mongodb不需要先创建集合再进入到集合中
// use 不存在的集合名称
// 当前进入的这个数据库是虚拟的 在这个虚拟数据库中插入数据之后mongodb才会帮你真正的创建数据库
use student_info


// 在数据库中创建集合
// db.createCollection('集合名称')
db.createCollection('stu')
/*
通过navicat发现所谓的student_info相当于mysql中的数据库
stu相当于mysql中的表
*/

// 创建带有容量的集合
db.createCollection("sub", {capped: true, size: 10})

// 查看创建的集合
use student_info
show collections  // 集合查看

// 删除指定集合
// db.集合名称.drop()
db.sub.drop()
