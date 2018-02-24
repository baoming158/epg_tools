#!/usr/bin/env python3

# 此工具类用来，根据栏目ID更新epg抽象节目ID，然后发送mq通知
import pymysql

from util.log import Logger

from util import db


class TvColumn():
    pass


logger = Logger(logName='logs/sucessful.txt', logLevel="INFO", logger="filter_column").getlog()
column = TvColumn()

def filter_epg(line):
    sql = "select id,status,tv_id,ca_id from kytv_resource_column_tvstation where id = %d" % (int(line))
    try:
        # 执行SQL语句
        cursor = db.con.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            if row['status'] == 0:
                continue
            if row['tv_id']:
                if row['tv_id'] != 412 and row['tv_id'] != 33 and row['tv_id'] != 1036:
                    logger.info(str(row['id']) + '---' + str(row['tv_id']) + '---' + str(row['ca_id']))
    except:
        # 发生错误时回滚
        logger.error('select error column_id=%s', str(line))
        db.con.rollback()
        # 关闭数据库连接
    # db.con.close()


def read_file_epg(file):
    file = open(file)
    while 1:
        line = file.readline()
        if not line:
            break
        filter_epg(line)

    file.close()


if __name__ == '__main__':
    logger.info('start run job')
    read_file_epg()