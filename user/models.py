from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from utils.constant import *


class User(AbstractUser):
    """
    用户
    """
    name = models.CharField(
        _(u"姓名"), db_index=True, max_length=128, null=True, blank=True)
    nickname = models.CharField(
        _(u"昵称"), max_length=128, null=True, blank=True)
    avatar = models.URLField(_(u"头像URL"), null=True, blank=True)
    gender = models.CharField(
        _(u"性别"), max_length=16, null=True, blank=True, choices=GENDER_CHOICE)
    identity_card = models.CharField(
        _(u"身份证号码"), max_length=32, null=True, blank=True)
    mobile = models.CharField(_(u"手机号"), max_length=16, null=True, blank=True)
    ctime = models.DateTimeField(_(u"创建时间"), auto_now_add=True)
    utime = models.DateTimeField(_(u"修改时间"), auto_now=True)

    def __str__(self):
        return self.nickname or self.username

    class Meta(AbstractUser.Meta):
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        db_table = "auth_user"

    def generate_token(self):
        """
        生成用户token

        客户端使用token进行用户权限校验
        """
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)
        return token
