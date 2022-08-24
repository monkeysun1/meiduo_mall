from django.shortcuts import render
from django_redis import get_redis_connection
from libs.captcha.captcha import captcha
from django.views import View
from django.http import HttpResponse
# Create your views here.
class ImageCodeView(View):
    """图形验证码"""

    def get(self, request, uuid):
        """
        :param request: 请求对象
        :param uuid: 唯一标识图形验证码所属于的用户
        :return: image/jpeg
        """
        # 生成图片验证码
        text, image = captcha.generate_captcha()

        # 保存图片验证码
        redis_conn = get_redis_connection('code')
        redis_conn.setex('img_%s' % uuid, 300, text)

        # 响应图片验证码
        return HttpResponse(image, content_type='image/jpeg')