#!/usr/bin/python
# encoding: utf-8
#
u'''
作者： zrong(http://zengrong.net)
创建日期： 2016-05-30
'''

import json
import io
import sys
from workflow import Workflow, ICON_WEB

log = None

def readurls():
    urlstring = None
    with io.open('urls.json', encoding='utf-8') as f:
        urlstring = f.read()
    urllist = json.loads(urlstring)
    return urllist

urls = readurls()

def main(wf):
    urllist = urls
    qs = wf.args[0] if len(wf.args) else None
    log.debug(wf.args)
    if qs:
        urllist = filter(lambda item:item['title'].lower().find(qs.lower()) >- 1, urls)
    for url in urllist:
        wf.add_item(url['title'], url['url'], arg=url['url'], valid=True, icon=ICON_WEB)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
