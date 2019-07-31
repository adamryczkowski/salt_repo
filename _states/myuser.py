#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Custom Salt State Module Example from https://implement.pt/2019/01/an-advanced-guide-to-salt
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

__virtualname__ = 'myuser'


def __virtual__():
    return __virtualname__


def disable_login(name):

    ret = dict()

    if __opts__['test']:
        ret['name'] = 'login'
        ret['changes'] = dict()
        ret['result'] = None
        ret['comment'] = 'Would disable login for user {0}'.format(name)
        return ret

    ret = __salt__['myuser.disable_login'](name)

    ret['name'] = 'login'

    return ret


def enable_login(name):

    ret = dict()

    if __opts__['test']:
        ret['name'] = 'login'
        ret['changes'] = dict()
        ret['result'] = None
        ret['comment'] = 'Would enable login for user {0}'.format(name)
        return ret

    ret = __salt__['myuser.enable_login'](name)

    ret['name'] = 'login'

    return ret


def expire_passwd(name):

    ret = dict()

    if __opts__['test']:
        ret['name'] = 'login'
        ret['changes'] = dict()
        ret['result'] = None
        ret['comment'] = 'Would force password change for user {0}'.format(name)
        return ret

    ret = __salt__['myuser.expire_passwd'](name)

    ret['name'] = 'login'

    return ret