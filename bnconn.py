#!/usr/bin/python
# encoding: utf-8

########################################
u'''
作者： zrong(http://zengrong.net)
创建日期： 2016-05-30
'''
########################################

import sys
from workflow import (Workflow, notify, ICON_USER, ICON_SETTINGS, ICON_NETWORK)

log = None

def connect(name, passwd):
    notify.notify(name, passwd)

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
