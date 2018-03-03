# _*_coding:utf-8_*_
# Author:xupan
# -*- coding:utf-8 -*-
import re
import os
from django import template
from django.utils.safestring import mark_safe
from django.conf import settings

register = template.Library()


def process_menu_tree_data(request):
    """
    根据Session中获取的菜单以及权限信息，结构化数据，生成特殊数据结构，如：
    [
        {id:1,caption:'菜单标题',parent_id:None,status:False,opened:False,child:[...]},
    ]
    PS: 最后一层的权限会有url，即：菜单跳转的地址

    :param request:
    :return:
    """
    menu_permission_dict = request.session.get(settings.RBAC_MENU_PERMISSION_SESSION_KEY)
    if not menu_permission_dict:
        raise Exception('Session中未保存当前用户菜单以及权限信息，请登录后初始化权限信息！')

    """ session中获取菜单和权限信息 """
    all_menu_list = menu_permission_dict[settings.RBAC_MENU_KEY]
    menu_permission_list = menu_permission_dict[settings.RBAC_MENU_PERMISSION_KEY]

    all_menu_dict = {}
    for row in all_menu_list:
        row['opened'] = False
        row['status'] = False
        row['child'] = []
        all_menu_dict[row['id']] = row
    permission_list = []
    """ 将权限信息挂靠在菜单上，并设置是否默认打开，以及默认显示 """
    for per in menu_permission_list:
        item = {'id': per['permissions__id'], 'caption': per['permissions__caption'], 'url': per['permissions__url'],
                'parent_id': per['permissions__menu_id'],
                'opened': False,
                'status': True}
        menu_id = item['parent_id']
        all_menu_dict[menu_id]['child'].append(item)

        # 将当前URL和权限正则进行匹配，用于指示是否默认打开菜单
        pattern = settings.RBAC_MATCH_PARTTERN.format(item['url'])
        if re.match(pattern, request.path_info):
            item['opened'] = True
            permission_list.append(item['caption'])
        if item['opened']:
            pid = menu_id
            while not all_menu_dict[pid]['opened']:
                all_menu_dict[pid]['opened'] = True
                permission_list.append(all_menu_dict[pid]['caption'])
                pid = all_menu_dict[pid]['parent_id']
                if not pid:
                    break

        if item['status']:
            pid = menu_id
            while not all_menu_dict[pid]['status']:
                all_menu_dict[pid]['status'] = True
                pid = all_menu_dict[pid]['parent_id']
                if not pid:
                    break
    result = []
    for row in all_menu_list:
        pid = row['parent_id']
        if pid:
            all_menu_dict[pid]['child'].append(row)
        else:
            result.append(row)
    return result, permission_list


@register.simple_tag
def title_pre(request):
    p, result = process_menu_tree_data(request)
    result.reverse()
    tpl = '>'.join(result)
    print(tpl)
    return tpl


def build_menu_tree_html(menu_list):
    # tpl1 = """
    #     <div class='rbac-menu-item'>
    #         <div class='rbac-menu-header'>{0}</div>
    #         <div class='rbac-menu-body {2}'>{1}</div>
    #     </div>
    # """
    # tpl2 = """
    #     <a href='{0}' class='{1}'>{2}</a>
    # """
    tpl1 = """
			<li class="list-divider"></li>
	        <li {2}>
	            <a aria-expanded="{3}">
                	<i class="psi-geo-2-star"></i>
            			<span class="menu-title">{0}</span>
                    <i class="arrow"></i>
                </a>
	            <ul class='collapse {4}' aria-expanded="{3}">{1}</ul>
	        </li>
	    """
    tpl2 = """
			<li {1}>
	        <a href='{0}' >{2}</a>
	        </li>
	    """
    menu_str = ""
    for menu in menu_list:
        if not menu['status']:
            continue

        if menu.get('url'):
            menu_str += tpl2.format(menu['url'], "class='active-link'" if menu['opened'] else "", menu['caption'], )
        else:
            if menu.get('child'):
                child = build_menu_tree_html(menu.get('child'))
            else:
                child = ""
            menu_str += tpl1.format(menu['caption'], child, "class='active'" if menu['opened'] else '',
                                    "true" if menu['opened'] else "false", "in" if menu['opened'] else "")
    return menu_str


@register.simple_tag
def rbac_menu(request):
    """
    根据Session中当前用户的菜单信息以及当前URL生成菜单
    :param request: 请求对象
    :return:
    """
    menu_tree_list, p = process_menu_tree_data(request)
    return mark_safe(build_menu_tree_html(menu_tree_list))


@register.simple_tag
def rbac_css():
    file_path = os.path.join('carry', 'theme', settings.RBAC_THEME, 'rbac.css')
    if os.path.exists(file_path):
        return mark_safe(open(file_path, 'r', encoding='utf-8').read())
    else:
        raise Exception('rbac主题CSS文件不存在')


@register.simple_tag
def rbac_js():
    file_path = os.path.join('carry', 'theme', settings.RBAC_THEME, 'rbac.js')
    if os.path.exists(file_path):
        return mark_safe(open(file_path, 'r', encoding='utf-8').read())
    else:
        raise Exception('rbac主题JavaScript文件不存在')
