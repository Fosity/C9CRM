# -*- coding: utf-8 -*-  
from bs4 import BeautifulSoup


def xss_defend(content):
    """
    输入内容是否符合要求检查
    :param content:
    :return:
    """
    # 白名单列表
    valid_tap = {
        'p': ['class', 'id'],
        'img': ['src'],
        'div': ['class']
    }
    soup = BeautifulSoup(content, 'html.parser')

    tags = soup.find_all()
    for tag in tags:
        if tag.name not in valid_tap:
            tag.decompose()  # 删除不在白名单的标签

        if tag.attrs:
            for k in list(tag.attrs.keys()):
                if k not in valid_tap[tag.name]:
                    del tag.attrs[k]  # 删除 不在白名单标签属性的值
    content_str = soup.decode()
    return content_str
