# -*- coding: utf-8 -*-


class WSQException(Exception):
    error_code = None
    error_msg = None

    def __init__(self, *args, **kwargs):
        self.args = args
        super(Exception, self).__init__(*args, **kwargs)

    def __str__(self):
        return 'Code: %s, Msg: %s %s' % (self.error_code, self.error_msg, " ".join([str(item) for item in self.args]))


class parametersTypWrongException(WSQException):
    error_code = 100001
    error_msg = "parameter type is wrong"

class forbiddenException(WSQException):
    error_code = 403000
    error_msg = "403 forbidden"

class serverErrorException(WSQException):
    #SERVER_ERROR = 500
    error_code = 500000
    error_msg = "server interal error"

class badGatewayException(WSQException):
    #BAD_GATEWAY = 502
    error_code = 502000
    error_msg = "502 bad gateway"

class gatewayTimeoutException(WSQException):
    #GATEWAY_TIMEOUT = 504
    error_code = 504000
    error_msg = "504 gateway timeout"

class notFoundException(WSQException):
    #GATEWAY_TIMEOUT = 504
    error_code = 404000
    error_msg = "404 not found"

def make403Exception(error_code):
    e = forbiddenException
    e.error_code = int(error_code)
    e.error_msg = forbidden_codes[e.error_code]
    return e

forbidden_codes = {}
forbidden_codes[403001] = "illegal request method"
forbidden_codes[403002] = "ak not exist"
forbidden_codes[403003] = "ip frequency exceed"
forbidden_codes[403004] = "ak not in whitelist"
forbidden_codes[403005] = "ak frequency exceed"
forbidden_codes[403006] = "ak url method not authorized"
forbidden_codes[403007] = "ak url method frequency exceed"
forbidden_codes[403008] = "same request timeout"
forbidden_codes[403009] = "wrong signature parameters"
forbidden_codes[403010] = "wrong post content_type"
forbidden_codes[403011] = "empty signature parameter"
forbidden_codes[403012] = "ip in blacklist"


