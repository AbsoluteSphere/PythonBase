use student_info

show collections

db.stu.drop()

// 新建一个集合
// 当前stu_test不存在
// 就算这个集合不存在我也可以直接插入数据
// 当数据插入成功之后mongodb会自动创建集合
db.stu_test.insert({'name': 'xiaoming', 'age': 10})

// 数据查询
db.stu_test.find()

// 插入第二条数据 并且编辑数据时key不加引号
db.stu_test.insert({name: 'xiaohong', age: 10})
db.stu_test.find()


// 保存修改后的数据
db.stu_test.insert({_id: 10010, name: 'xiaoming', age: 30})
db.stu_test.find()

// 如果要修改已经存在的数据不能用insert
// db.stu_test.insert({_id: 10010, name: 'xiaoming', age: 40})
db.stu_test.save({_id: 10010, name: 'xiaoming', age: 40})  // 可以进行数据覆盖
db.stu_test.find()

// 数据更新
db.stu_test.update({name: 'xiaoming'}, {name: 'xiaozhao'})  // 会造成其他字段的丢失
db.stu_test.insert({name: '安娜', age: 18, gender: '女'})
db.stu_test.update({name: '安娜'}, {$set: {name: '双双'}})


// 数据删除
db.stu_test.remove({name: '木木'})  // 只要名称是木木 那么就全部删除
db.stu_test.remove({name: 'xiaozhao'}, {justOne: true})
db.stu_test.remove({name: 'xiaozhao'})