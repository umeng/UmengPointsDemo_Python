# -*- coding: utf-8 -*-
import consts
from HExceptions import *

def check_request(r):
    if r.status_code == consts.NORMAL_HTTP_CODE:
        return r

    if r.status_code == consts.FORBIDDEN_CODE:
        code = r.headers.get('forbidden-code', 403000)
        raise make403Exception(code)

    if  r.status_code == consts.GATEWAY_TIMEOUT:
        raise gatewayTimeoutException

    if r.status_code == consts.BAD_GATEWAY:
        raise badGatewayException

    if r.status_code == consts.NOT_FOUND:
        raise notFoundException

    if r.status_code == consts.SERVER_ERROR:
        raise serverErrorException