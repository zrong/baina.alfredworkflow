#!/usr/bin/python
# encoding: utf-8

########################################
u'''
作者： zrong(http://zengrong.net)
创建日期： 2016-05-30
'''
########################################

import sys
import json
from workflow import (Workflow, notify, web)

log = None
loginurl = 'http://192.168.66.1/ac_portal/login.php'


def connect(name, passwd):
    params = dict(opr='pwdLogin', userName=name, pwd=passwd)
    r = web.post(loginurl, params)
    r.raise_for_status()
    log.debug(r.status_code)
    # encoding 的值为 None
    # 不得不BS一下硬件公司的软件程序员的编码水平
    # 没有 encoding ，JSON用单引号
    log.debug(r.encoding)
    # 是哪个傻X在JSON里面使用单引号！
    jsonstr = unicode(r.content, 'utf8').replace("'", '"')
    result = json.loads(jsonstr)
    notify.notify(result['msg'], u'user: %s'%result['userName'])

def main(wf):
    conf = wf.settings.get('user')
    if conf:
        # 删除暂存的配置信息，该信息仅用于参数传递
        del wf.settings['user']
        # 更新配置信息
        wf.store_data('user', conf)
    user = wf.stored_data('user')
    log.debug('conf in settings:%s'%conf)
    log.debug('user in stored:%s'%user)
    if user:
        connect(user['name'], user['pass'])
    else:
        notify.notify(u'无法获取配置信息！', u'请使用 bnconn user pass 保存。')

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
