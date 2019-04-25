from rest_framework.response import Response
from rest_framework import status, permissions
from django.core.exceptions import PermissionDenied
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed
from utils import errors
import time
import datetime


class Error(Exception):
    def __init__(self, code, msg=u'服务异常', status_code=status.HTTP_200_OK):
        self.code = code
        self.msg = msg
        self.status_code = status_code

    def __unicode__(self):
        return u'[Error] %s: %s(%d)' % (self.code, self.msg, self.status_code)

    def getResponse(self):
        return ErrorResponse(self.code, self.msg, self.status_code)


def ErrorResponse(code=errors.ERROR_UNKOWN,
                  msg=u'服务异常',
                  status=status.HTTP_400_BAD_REQUEST,
                  headers=None):
    err = {
        'code': code,
        'msg': msg,
        'systemtime': int(round(time.time() * 1000)),
        'status_code': status
    }
    return Response(err, status, headers=headers)


def custom_exception_handler(exc, context):
    if isinstance(exc, Error):
        return ErrorResponse(exc.code, exc.msg, status=exc.status_code)

    if isinstance(exc, (NotAuthenticated, AuthenticationFailed)):
        return ErrorResponse(
            errors.ERROR_TOKEN_ERROR,
            u'opps, token错误，请重新登录',
            status=status.HTTP_403_FORBIDDEN)

    if isinstance(exc, (PermissionDenied)):
        msg = _('Permission denied.')
        return ErrorResponse(
            errors.ERROR_PERMISSION_DENIED,
            u'opps, 您没有对应的权限',
            status=status.HTTP_403_FORBIDDEN)
        log.error(exc)
    # Note: Unhandled exceptions will raise a 500 error.
    # return ErrorResponse(errors.SYSTEM_ERROR, 'Internal Server Error', status.HTTP_500_INTERNAL_SERVER_ERROR)
