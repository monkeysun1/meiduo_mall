from django.urls import converters

class UsernameConverter:
    """自定义路由转换器去匹配用户名"""
    # 定义匹配用户名的正则表达式
    regex = '[a-zA-Z0-9_-]{5,20}'

    def to_python(self, value):
        return str(value)


class UUIDConverter:
    """自定义路由转换器去匹配手机号"""
    # 定义UUID的正则表达式
    regex = '[\w-]+'

    def to_python(self, value):
        # to_python：将匹配结果传递到视图内部时使用
        return str(value)

# 在工程的总路由出添加
from utils.converters import UUIDConverter
from django.urls import register_converter

register_converter(UUIDConverter,'uuid')