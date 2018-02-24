import pymysql

# con = pymysql.connect(
#                 host='127.0.0.1',
#                 port=3306,
#                 user='root',
#                 passwd='root1234',
#                 db='kytv',
#                 charset='utf8',
#                 cursorclass=pymysql.cursors.DictCursor
#             )

con = pymysql.connect(
                host='172.21.62.114',
                port=3308,
                user='kytv',
                passwd='NGOLESkMfp',
                db='kytv',
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
