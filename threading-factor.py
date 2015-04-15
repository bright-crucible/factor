#!/usr/bin/env python
'Attempt to use threading module to improve performance of int factoring'
from __future__ import print_function
from __future__ import division
import math
import threading


class myThread (threading.Thread):
    def __init__(self, threadID, name, workstart, workend, N):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.workstart = workstart
        self.workend = workend
        self.N = N
        self.data = []
    def run(self):
        for i in xrange(self.workstart, self.workend):
            dm = divmod(self.N,i)
            if dm[1] == 0:
                self.data.append((i, dm[0]))
        print(self.name, "is done")

if __name__ == '__main__':
    N=2**50
    E=int(math.ceil(math.sqrt(N)))
    l=[]
    for i in xrange(2,E+1,E//8):
        l.append(i)
    l.append(E+1)
    thread1 = myThread(1, "Thread-1", l[0], l[1], N)
    thread2 = myThread(2, "Thread-2", l[1], l[2], N)
    thread3 = myThread(3, "Thread-3", l[2], l[3], N)
    thread4 = myThread(4, "Thread-4", l[3], l[4], N)
    thread5 = myThread(5, "Thread-5", l[4], l[5], N)
    thread6 = myThread(6, "Thread-6", l[5], l[6], N)
    thread7 = myThread(7, "Thread-7", l[6], l[7], N)
    thread8 = myThread(8, "Thread-8", l[7], l[8], N)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()

    threads = []
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)
    threads.append(thread4)
    threads.append(thread5)
    threads.append(thread6)
    threads.append(thread7)
    threads.append(thread8)

    for t in threads:
        t.join()

    final = thread1.data + thread2.data + thread3.data + thread4.data + thread5.data + thread6.data + thread7.data + thread8.data
    #print(sorted(final))
    print(final)
