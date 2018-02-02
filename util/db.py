import pymysql

con = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='root1234',
                db='kytv',
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )

# con1 = pymysql.connect(
#     host='172.21.19.203',
#     port=3306,
#     user='ky',
#     passwd='ky',
#     db='kytv',
#     charset='utf8',
#     cursorclass=pymysql.cursors.DictCursor)
