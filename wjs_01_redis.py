from redis import StrictRedis


if __name__ == '__main__':
    # 创建一个StrictRedis对象，链接redis数据库
    try:
        sr = StrictRedis()
        # 添加一个KEY,为name，值为Jason
        # res = sr.set("name", "Jason")
        # print(res)

        # 修改name的值为wangjinsen
        # res = sr.set("name", "wangjinsen")
        # print(res)

        # 获取name的值
        # res = sr.get("name")
        # print(res)

        # 删除name以及对应的值
        # res = sr.delete("name")
        # print(res)

        # 删除多个键值
        # res = sr.delete("name", "name1")
        # print(res)

        # 获取数据库中所有的键
        res = sr.keys()
        print(res)

    except Exception as e:
        print(e)
