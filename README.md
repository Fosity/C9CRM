# C9CRM
CRM using django

功能实现：
1.参考django admin，实现自定制 CURD 组件。
2.基于中间件的权限管理功能。
3.实现任务管理功能
4.基于haystack，实现全局搜索功能。
5.配置缓存功能


C9CRM
|-----
    |----C9CRM              配置文件
    |-----carry             自定制CURD组件,权限管理
        |----middleware           权限管理中间件                
        |----service              CURD，rbac
        |----static               静态文件
        |----templates            html文件
        |----templatetags         模板标签
        |----utils                分页工具
        |----views                业务逻辑
        |----models.py            数据库
        |----carry.py             类似admin 的注册功能
        |----apps.py              组件运行
    |-----gsearch           全局搜索功能
        |----search_indexes.py    全局搜索配置
        |----views.py             页面ajax交互逻辑
    |-----task              任务管理功能
        |----views                任务管理业务
            |----taskadmin.py         任务CURD
            |----tasktypeadmin.py     任务类型CURD
            |----service              任务报表
                |----task_func            任务报表数据获取与清理
                |----taskconfig           任务报表配置
        |----models.py                数据库
        |----carry.py                 注册功能
    |-----templates         html页面
    |-----test              测试
    |-----utils             其他工具
    |-----websocket         页面聊天框（基于django-channels,channel-reids)
    |-----whoosh_index      haystack缓存内容
    |-----db.sqlites        数据库
    |-----manage.py         执行文件
    
    
    ######## 关于 carryadmin 组件 ###########
    
    
