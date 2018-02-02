#!/usr/bin/env python3

# 此工具类用来，根据栏目ID更新epg抽象节目ID，然后发送mq通知
from util.log import Logger

from util import db


class TvColumn():
    pass


logger = Logger(logName='logs/sucessful.txt', logLevel="INFO", logger="update_abs_id").getlog()

column = TvColumn()
list = []

def update_epg(line):
    epg = line.split(' ')
    sql = "UPDATE kytv_resource_column_tvstation SET ca_id = "+str(epg[1])+" WHERE id = %d" % (int(epg[0]))
    try:
        # 执行SQL语句
        db.con.cursor().execute(sql)

        column.id = epg[0]
        # 提交到数据库执行
        db.con.commit()
        logger.info('update successful column_id=%s', str(epg[0]))
    except:
        # 发生错误时回滚
        logger.error('update error column_id=%s', str(epg[0]))
        db.con.rollback()
        # 关闭数据库连接
    # db.con.close()


def do_modify(file):
    file = open(file)
    while 1:
        line = file.readline()
        if not line:
            break
        update_epg(line)

        list.append(column)
    file.close()
    return list


if __name__ == '__main__':
    logging.info('start run job')
    do_modify()