from django.shortcuts import render
from utils.api_response import JsonResponse
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
# @authentication_classes((JSONWebTokenAuthentication, ))
# @permission_classes((IsAuthenticated, ))
def user_info(request):
    """
    获取用户信息
    """
    result = {}
    result['nickname'] = 'karl'
    result['avatar'] = 'avatar'
    result['mobile'] = '138000000'
    return JsonResponse(data=result)
