#!/usr/bin/python
# encoding: utf-8

u'''
作者： zrong(http://zengrong.net)
创建日期： 2016-05-30
'''

import sys
from workflow import (Workflow, ICON_USER, ICON_SETTINGS, ICON_NETWORK)

log = None

def checkargs(qs):
    conf = []
    if qs:
        conf = qs.split(u' ', 1)
    if len(conf) > 1:
        if conf[1].strip():
            return True, {'name':conf[0].strip(), 'pass':conf[1].strip()}
        return False, 1
    return False, len(conf)

def main(wf):
    user = wf.stored_data('user')
    succ, conf = checkargs(wf.args[0] if len(wf.args) else None)
    if user:
        if succ:
            # 仅用于临时存储，回车后才真正存储
            wf.settings['user'] = conf
            wf.add_item(u'回车覆盖已保存的用户并连接网络', valid=True, icon=ICON_SETTINGS)
        elif conf == 1:
            wf.add_item(u'请输入密码', u'bnconn user pass', valid=True, icon=ICON_USER)
        else:
            wf.add_item(u'使用已保存的信息连接网络', valid=True, icon=ICON_NETWORK)
    else:
        if succ:
            # 仅用于临时存储，回车后才真正存储
            wf.settings['user'] = conf
            wf.add_item(u'回车保存用户信息并连接网络', valid=True, icon=ICON_SETTINGS)
        elif conf == 1:
            wf.add_item(u'请输入密码', u'bnconn user pass', valid=True, icon=ICON_USER)
        else:
            wf.add_item(u'请输入用户名和密码（仅需一次）', u'bnconn user pass', valid=True, icon=ICON_USER)

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
