#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @CreateDate             : 4/11/2017 11:51 AM
# @Author                 : gaopq (peiqianggao@gmail.com)
# @Version                : 001
# @File                   : main.py
# @ModifyDate             :
# @Descriptions           :
# @ChangeLog              :


import os
import sys
import copy
from wox import Wox

result_template = {
    'Title': '{}',
    'SubTitle': 'Copy to clipboard',
    'IcoPath': 'Images/md5.png',
    'JsonRPCAction': {
        'method': 'copyToClipboard',
        'parameters': ['{}'],
    }
}


class Main(Wox):
    def query(self, key=None):
        if not key:
            return ["Pls specify a string for md5sum :)"]

        if sys.version_info[0] == 3:
            import hashlib

            m = hashlib.md5()
            m.update(key.encode())
        else:
            import md5

            m = md5.new()
            m.update(key)

        md_res = m.hexdigest()
        results = list()
        for md in [md_res, md_res.upper()]:
            res = copy.deepcopy(result_template)
            res['Title'] = res['Title'].format(md)
            res['JsonRPCAction']['parameters'][0] = res['JsonRPCAction']['parameters'][0].format(md)
            results.append(res)
            res = None

        return results

    def copyToClipboard(self, value):
        command = 'echo ' + value.strip() + '| clip'
        os.system(command)

if __name__ == '__main__':
    Main()
