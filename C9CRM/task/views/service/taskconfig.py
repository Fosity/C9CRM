# -*- coding: utf-8 -*-  
task_config = {
    '00': {
        'menu': '2018全年任务',  ###生成页面显示名称
        'name_id': '00',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '全年完成任务情况',
            'b': '全年未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': True,
        },
        'x_axis': {
            'type': 'to_user_username',  # 定义x轴上显示内容
            'status': True,  ####定义x轴上是否有值
        },
        'select_args': {
            'group_by': ['to_user__username', ],
            'time': '2018-01-01/2019-01-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
    '01': {
        'menu': '2018一月份任务',  ###生成页面显示名称
        'name_id': '01',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '一月份完成任务情况',
            'b': '一月份未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': None,
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-01-01/2018-02-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
    '02': {
        'menu': '2018二月份任务',  ###生成页面显示名称
        'name_id': '02',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '二月完成任务情况',
            'b': '二月未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': None,
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-02-01/2018-03-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
    '03': {
        'menu': '2018三月份任务',  ###生成页面显示名称
        'name_id': '03',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '三月完成任务情况',
            'b': '三月未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': None,
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-03-01/2018-04-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
    '04': {
        'menu': '2018四月份任务',  ###生成页面显示名称
        'name_id': '04',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '四月完成任务情况',
            'b': '四月未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': None,
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-04-01/2018-05-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
    '05': {
        'menu': '2018五月份任务',  ###生成页面显示名称
        'name_id': '05',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '五月完成任务情况',
            'b': '五月未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': None,
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-05-01/2018-06-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
    '06': {
        'menu': '2018六月份任务',  ###生成页面显示名称
        'name_id': '06',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '六月完成任务情况',
            'b': '六月未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': None,
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-06-01/2018-07-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
    '07': {
        'menu': '2018七月份任务',  ###生成页面显示名称
        'name_id': '07',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '七月完成任务情况',
            'b': '七月未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': None,
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-07-01/2018-08-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
    '08': {
        'menu': '2018八月份任务',  ###生成页面显示名称
        'name_id': '08',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '八月完成任务情况',
            'b': '八月未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': None,
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-08-01/2018-09-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
    '09': {
        'menu': '2018九月份任务',  ###生成页面显示名称
        'name_id': '09',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '九月完成任务情况',
            'b': '九月未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': None,
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-08-01/2018-09-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
    '10': {
        'menu': '2018十月份任务',  ###生成页面显示名称
        'name_id': '10',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '十月完成任务情况',
            'b': '十月未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': None,
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-09-01/2018-10-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
    '11': {
        'menu': '2018十一月份任务',  ###生成页面显示名称
        'name_id': '11',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '十一月完成任务情况',
            'b': '十一月未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': None,
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-10-01/2018-11-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
    '12': {
        'menu': '2018十二月份任务',  ###生成页面显示名称
        'name_id': '12',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '十二月完成任务情况',
            'b': '十二月未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': None,
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-11-01/2018-12-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    }
}
task_config_person = {
    '00': {
        'menu': '全年任务',  ###生成页面显示名称
        'name_id': '00',  ###定义前后端交互的id
        'status': {
            'a': [1],
            'b': [2, 3, 4, 5],
        },
        'title': {
            'a': '全年完成任务情况',
            'b': '全年未完成任务情况',
        },
        'y_axis': {
            'type': 'num',
            'together': True,
        },
        'x_axis': {
            'type': 'to_user__username',  # 定义x轴上显示内容
            'status': True,  ####定义x轴上是否有值
        },
        'select_args': {
            'group_by': ['to_user__username'],
            'time': '2018-01-01/2019-01-01',
            'time_name': 'finish_time',
            'id_name': 'nid',
        },
        'type': 'pie'  # 定义 图标类型
    },
}
