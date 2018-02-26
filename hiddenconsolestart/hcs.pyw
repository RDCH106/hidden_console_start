# -*- coding: utf-8 -*-

from hiddenconsolestart.metadata import Metadata
from hiddenconsolestart.process import HCSProcess
import argparse
import threading
from time import sleep


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

        stop = False
        while not stop:
            num_thr = 0
            for t in self.__threads:
                if not t.isAlive():
                    num_thr += 1
            if num_thr == len(self.__threads):
                stop = True
            else:
                num_thr
            sleep(1)


if __name__ == "__main__":
    hcs = HCS()
    hcs.run()
