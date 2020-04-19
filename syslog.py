#!/usr/bin/env python3       
import os
import time
import blinkt
blinkt.set_clear_on_exit()
keep_phrases = ["facebook",
                "instagram",
                "twitter",
                "youtube"]
def follow(name):
    current = open(name, "r")
    curino = os.fstat(current.fileno()).st_ino
    while True:
        while True:
            line = current.readline()
            if not line:
                break
            yield line

        try:
            if os.stat(name).st_ino != curino:
                new = open(name, "r")
                current.close()
                current = new
                curino = os.fstat(current.fileno()).st_ino
                continue
        except IOError:
            pass
        time.sleep(1)


if __name__ == '__main__':
    fname = "/var/log/arris.log"
    for l in follow(fname):
        for phrase in keep_phrases:
            if phrase in l:
                blinkt.set_all(128, 0, 0)
                blinkt.show()
                print ("HIT:  {}".format(l))
                time.sleep(0.1)
                blinkt.set_all(0, 0, 0)
                blinkt.show()
