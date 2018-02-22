# -*- coding: utf-8 -*-

from hiddenconsolestart.metadata import Metadata
from hiddenconsolestart.process import HCSProcess
import argparse
import threading


def worker(app):
    HCSProcess(app).run()


class HCS(object):
    def __init__(self):
        self.meta = Metadata()
        self.__threads = list()

        # Parse arguments provided
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--version', action='version', version=self.meta.get_version())
        parser.add_argument('-e', '--execute', dest='execute',
                            help='Executables to launch (can be a space seperated list)',
                            metavar='APP', type=str, nargs='+')
        self.args = parser.parse_args()

    def run(self):
        if not self.args.execute:
            exit(0)
        for app in self.args.execute:
            t = threading.Thread(target=worker, args=(app,))
            self.__threads.append(t)
            t.start()


if __name__ == "__main__":
    hcs = HCS()
    hcs.run()
