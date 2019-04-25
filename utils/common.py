# -*- coding:utf-8 -*-
import sys
import logging
import datetime

logger = logging.getLogger(__name__)


# 异常信息打印
def except_info(ex, params=None, need_log=True):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_details = {
        'filename': exc_traceback.tb_frame.f_code.co_filename,
        'lineno': exc_traceback.tb_lineno,
        'name': exc_traceback.tb_frame.f_code.co_name,
        'type': exc_type.__name__,
        'message': exc_value,
    }
    if need_log:
        logger.critical(" |---Throw Exception:{0}\n params:{1} errmsg:{2}".format(traceback_details, params, str(ex)))
    return "{0}('{1}')".format(exc_type.__name__, exc_value)


# 获取GMT+8时间戳
def get_gmt8_timestr(t):
    try:
        # delta = datetime.timedelta(hours=8)
        # gmt8 = t + delta
        tstr = t.strftime("%Y-%m-%d %H:%M:%S")
        return tstr
    except BaseException as ex:
        except_info(ex)
        return ''
