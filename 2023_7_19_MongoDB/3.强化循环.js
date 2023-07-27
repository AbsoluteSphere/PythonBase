// 查询年龄在20岁的学生
use test

db.stu_info.find({age: 20})

// 查询18岁的学生并且只返回符合条件的第一个数据
db.stu_info.findOne({age: 18})
db.stu_info.find({age: 20}).pretty()  // 在终端使用

// 查询大于等于18岁的数据
db.stu_info.find({age: {$gte: 18}})

// 范围运算符
db.stu_info.find({age: {$in: [18, 45]}})

// 逻辑运算符 and or not
db.stu_info.find({age: 18, hometown: '桃花岛'})

db.stu_info.find({$or: [{age: 18}, {hometown: "桃花岛"}]})

db.stu_info.find({$or: [{age: {$gte: 45}}, {hometown: {$in:["桃花岛", "华山"]}}]})


db.products.find({sku:/^abc/})
db.products.find({sku: {$regex: "789$"}})

db.products.find().limit(2)
db.products.find().skip(2)
db.products.find().skip(2).limit(2)

db.stu_info.find({$where: function(){return this.age<=18}})


db.stu_info.find({age: {$gt: 18}}, {name: 1, age: 1, _id: 0})

db.stu_info.find({}, {name: 1, _id: 0})

// 排序
db.stu_info.find().sort({age: -1})
db.stu_info.find().sort({age: -1, gender: -1})

db.stu_info.find({age: {$gt: 18}}).sort({age: 1})


db.stu_info.find().count()


db.stu_info.distinct("hometown")


// 分组查询
db.stu_info.aggregate(
  {
    $group: {_id: "$gender", counter: {$sum: 1}}
  }
)

db.stu_info.aggregate(
  {
    $group: {_id: "$gender", count: {$sum: 1}, avg_age: {$avg: "$age"}}
  }
)


db.stu_info.aggregate(
  {
    $group: {_id: null, counter: {$sum: 1}, avg_age: {$avg: "$age"}}
  }
)

db.stu_info.aggregate(
  {
    $project: {_id: 0, name: 1, age: 1}
  }
)

db.stu_info.aggregate(
  {
    $group: {_id: "$gender", count: {$sum: 1}, avg_age: {$avg: "$age"}}
  },
  {
    $project: {"性别": "$_id", "人数统计": "$count", "平均年龄": "$avg_age", _id: 0}
  }
)


db.stu_info.aggregate(
  {
    $match: {age: {$gt: 20}}
  }
)


db.stu_info.aggregate(
  {
    $match: {age: {$gt: 20}},
  },
  {
    $group: {_id: "$gender", counter: {$sum: 1}}
  },
  {
    $project: {"性别": "$_id", "统计人数": "$counter", _id: 0}
  }
)


db.stu_info.aggregate(
  {
    $match:
    {
      $or:
        [
          {
            age: {$gt: 20}
          },
          {
            hometown: {$in: ["蒙古", "大理"]}
          }
        ]
    },
  },

  {
    $group: {_id: "$gender", counter: {$sum: 1}}
  },

  {
    $project: {"性别": "$_id", "统计人数": "$counter", _id: 0}
  }
)


db.stu_info.aggregate(
  {
    $sort: {age: 1}
  }
)


db.stu_info.aggregate(
  {
    $group: {_id: "$gender", counter: {$sum: 1}}
  },
  {
    $sort: {counter: -1}
  }
)


db.stu_info.aggregate(
  {$limit: 2}
)

db.stu_info.aggregate(
  {$skip: 2}
)

db.stu_info.aggregate({$skip: 1}, {$limit: 1})
