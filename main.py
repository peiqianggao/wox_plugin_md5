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
import clipboard
from wox import Wox, WoxAPI

result_template = {
    'Title': '{}',
    'SubTitle': 'Click to copy',
    'IcoPath': 'Images/md5.png',
    'JsonRPCAction': {
        'method': 'copy_to_clipboard',
        'parameters': ['{}'],
    }
}


class Wox_md5(Wox):
    def query(self, key):
        if not key:
            return [{"Title": "Please specify a string for md5sum :)",
                     "IcoPath": "Images/md5.png"
                     }]

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

    def copy_to_clipboard(self, value):
        """
        Copies the given value to the clipboard.
        WARNING:Uses yet-to-be-known Win32 API and ctypes black magic to work.
        """
        try:
            clipboard.put(value)
        except:
            command = 'echo ' + value.strip() + '| clip'
            os.system(command)



if __name__ == '__main__':
    Wox_md5()
