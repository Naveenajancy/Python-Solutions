from multiprocessing import Process
import time,signal
#import test


def f():
    for i in range(20):
        print ("Tick -> %s\n"%i)
        time.sleep(2)
def proc():
    threads = []
    p =Process(target=f,name="P")
    threads.append(p)
    l = Process(target=f,name="L")
    threads.append(l)
    q = Process(target=f,name="Q")
    threads.append(q)

    for th in threads:
        print("%s : PID : %s\n" % (th, th.pid))
        #print "Name is %s\n"%(i.getName())
        th.start()

    for th in threads:
        print ("pid ", th,th.pid)
        th.join(timeout=5)
        print("timeout reached")
        if th.is_alive():
            print("still alive")
            th.terminate()
            exit=th.pid
            print("terminate process")
            print("exiting process %s" % exit)


#for th in threads:
        #if th.is_alive():
            #print th.taskdone()
            #print "still alive"
            #th.terminate()
            #print "process terminated"

if __name__ ==	'__main__':
    proc()