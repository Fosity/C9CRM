# -*- coding: utf-8 -*-
import random

import forgery_py


def task_create():
    title = forgery_py.lorem_ipsum.sentence()
    introduction_content = forgery_py.email.body()
    create_time = forgery_py.date.datetime(True, max_delta=10)
    wish_finish_time = forgery_py.date.datetime(True, max_delta=10)
    finish_time = forgery_py.date.datetime(True, max_delta=10)
    finish_content = forgery_py.email.body()
    from_user_id = random.randrange(1, 16)
    status = random.randrange(1, 6)
    print(finish_time, wish_finish_time, create_time)
    if finish_time > create_time and wish_finish_time > create_time:
        data = {
            'title': title,
            'introduction_content': introduction_content,
            'status': status,
            'creat_time': create_time,
            'finish_time': finish_time,
            'from_user_id': from_user_id,
            'wish_finish_time': wish_finish_time,
            'finish_content': finish_content,
        }
        return data


def user_create():
    username = forgery_py.name.full_name()
    password = forgery_py.name.full_name()
    email = forgery_py.internet.email_address()
    roles = random.randrange(1, 4)
    data = {
        'username': username,
        'password': password,
        'email': email,
    }
    return data


def user_to_task(i):
    task_id = i
    user_id = random.randrange(1, 16)
    return user_id
