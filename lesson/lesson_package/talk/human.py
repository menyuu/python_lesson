# 相対パスは使わずに極力絶対パスにする
from lesson.lesson_package.tools import utils


# from ..tools import utils

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')