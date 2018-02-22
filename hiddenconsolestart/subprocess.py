# -*- coding: utf-8 -*-

import subprocess as sub


class HCSProcess(object):
    def __init__(self, app):
        self.__app = app
        self.__p = None

    def run(self):
        self.__p = sub.Popen(self.__app, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
        output, errors = self.__p.communicate()

