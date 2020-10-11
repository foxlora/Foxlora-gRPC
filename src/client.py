# -*- coding: utf-8 -*-
'''

'''
__author__ = 'Foxlora'
__time__ = '2020/10/11 23:23'

import grpc

import test_pb2
import test_pb2_grpc


def run():
    # 连接 rpc 服务器
    a = int(input('请输入整数a：'))
    b = int(input('请输入整数b：'))
    channel = grpc.insecure_channel('localhost:50052')
    # 调用 rpc 服务
    stub = test_pb2_grpc.AddNumStub(channel=channel)

    response = stub.addnum(test_pb2.AddRequest(a=a,b=b))#必须指明a=,b= 辣鸡

    print( response.result)


if __name__ == '__main__':
    run()