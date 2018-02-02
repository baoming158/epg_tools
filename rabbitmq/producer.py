#!/usr/bin/env python
# -*- coding: utf_8 -*-

import pika

from util import config


def sendMqMessage(message):
    # 创建连接connection到localhost
    user_pwd = pika.PlainCredentials(config.getMqValue('username'), config.getMqValue('password'))

    connection = pika.BlockingConnection(pika.ConnectionParameters(host= config.getMqValue('host'), credentials=user_pwd))
    channel = connection.channel()

    channel.exchange_declare(exchange=config.getMqValue('exchange_name'),
                             exchange_type=config.getMqValue('exchange_type'))

    channel.basic_publish(exchange=config.getMqValue('exchange_name'),
                          routing_key=config.getMqValue('route_key'),
                          body=message)

    connection.close()


if __name__ == '__main__':
    sendMqMessage("message test 222")
