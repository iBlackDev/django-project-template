# coding:utf-8

ERROR_0_OK = 0
ERROR_UNKOWN = -100
ERROR_PERMISSION_DENIED = -210
ERROR_TOKEN_ERROR = -300
ERROR_TOKEN_EXPIRE = -310

# 错误号   英文代码    中文描述    备注
CONSTANT = {
    # 公用模块
    "100000": ["Request type error", u"请求类型错误"],
    "100001": ["Required field can not be empty", u"必填字段不能为空"],
    "100002": ["Parameter type error", u"参数类型错误"],
    "100003": ["param value error", u"参数取值错误"],
    "100004": ["Request throw exception", u"请求出现错误."],
    "100005":
    ["You don't have enought permissions to this action!", u"您无权访问该页面."],
    "100006": ["Param value out of range!", u"参数取值超出范围."],
    "100007": ["The length of string value out of range!", u"字符串长度值超出范围."],
    "100008": ["This is the necessary option,please choose.", u"必选项，请选择！"],
    "100009": ["Params format error.", u"参数格式错误"],
}


def get_error_msg(k='100100000', en='ch'):
    k = str(k)
    if not k:
        return ""
    if en == 'ch':
        return CONSTANT.get(k)[1]
    elif en == 'en':
        return CONSTANT.get(k)[0]
    return CONSTANT.get(k)[1]
