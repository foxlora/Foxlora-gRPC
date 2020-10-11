# -*- coding: utf-8 -*-
'''

'''
__author__ = 'Foxlora'
__time__ = '2020/10/11 20:04'

import time
from concurrent import futures

import grpc

import test_pb2
import test_pb2_grpc


# 实现 proto 文件中定义的 GreeterServicer
class AddNumServicer(test_pb2_grpc.AddNumServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def addnum(self, request, context):
        #解析请求
        a = request.a
        b = request.b
        res = self.add_forlora(a,b)

        return test_pb2.AddReply(result = res)

    def add_forlora(self,a,b):
        c = a + b
        return '相加的结果是：' + str(c)

def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_AddNumServicer_to_server(AddNumServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print('服务器已在50052端口监听')
    try:
        while True:
            time.sleep(60*60*24) # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()