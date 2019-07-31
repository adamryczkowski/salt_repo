#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Custom Salt Execution Module Example from https://implement.pt/2019/01/an-advanced-guide-to-salt
"""

import spwd
import pwd
import os

__author__ = u"Manuel Torrinha"
__copyright__ = u"""Copyright (c) 2019 Manuel Torrinha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

__credits__ = u"Manuel Torrinha"
__maintainer__ = u"Manuel Torrinha"
__email__ = "torrinha _at_ implement _dot_ pt"


def get_orphan_home_dirs():
    """
    returns a directory list of directories, which the users that they belong to no longer exist

    CLI Example::

        salt '*' myuser.get_orphan_home_dirs
    """
    ret = dict()
    root = '/home'
    dirs = os.listdir(root)
    for dir_ in [d for d in dirs if os.path.isdir(os.path.join(root, d))]:
        found = False
        for p in [u for u in pwd.getpwall() if (u.pw_uid >= 1000)]: # here we skip system users
            if p.pw_dir == os.path.join(root, dir_):
                found = True
                break
        if not found:  # we got a culprit
            ret[root+dir_] = 'User {} Not Found!'.format(dir_)
    return ret


def disable_login(name):
    """
    disables a user from being able to login to the minion

    CLI Example::

        salt '*' myuser.disable_login username
    """
    ret = dict()

    minion_id = __salt__['grains.get']('id')

    try:
        pwd.getpwnam(name)
        __salt__['shadow.set_expire'](name, 0)

        ret['result'] = True
        ret['comment'] = None
        ret['changes'] = {'disable_login': {'old': '',
                                            'new': name + '@' + minion_id}}
    except KeyError:
        ret['result'] = True
        ret['changes'] = dict()
        ret['comment'] = 'User not Present ' + name + ' @ ' + minion_id

    return ret


def enable_login(name):
    """
    enables a user to login to the minion

    CLI Example::

        salt '*' myuser.enable_login username
    """
    ret = dict()
    minion_id = __salt__['grains.get']('id')

    try:
        pwd.getpwnam(name)
        __salt__['shadow.set_expire'](name, -1)

        ret['result'] = True
        ret['comment'] = None
        ret['changes'] = {'enable_login': {'old': '',
                                           'new': name + '@' + minion_id}}
    except KeyError:
        ret['result'] = True
        ret['changes'] = dict()
        ret['comment'] = 'User not Present ' + name + ' @ ' + minion_id

    return ret


def expire_passwd(name):
    """
    Expire the password validity for a user, forcing the user to change the password at next successful login

    CLI Example::

        salt '*' myuser.expire_passwd username
    """
    ret = dict()
    minion_id = __salt__['grains.get']('id')

    try:
        old = spwd.getspnam(name)
        __salt__['shadow.set_date'](name, 0)

        ret['result'] = True
        ret['changes'] = {'expire_passwd': {'old': old.sp_lstchg,
                                            'new': spwd.getspnam(name).sp_lstchg}}
        ret['comment'] = None
    except KeyError:
        ret['result'] = True
        ret['changes'] = dict()
        ret['comment'] = 'User not Present ' + name + ' @ ' + minion_id

    return ret