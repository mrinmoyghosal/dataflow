import uuid
from mgq import MgqWorker
import tracemalloc

if __name__ == "__main__":
    tracemalloc.start()
    randomStr = uuid.uuid4().hex.upper()[0:6]
    s = tracemalloc.take_snapshot()
    c = 0
    worker = MgqWorker("tcp://localhost:5555", "work", False)

    def recv(msg):
        global c
        global s
        c = c+1
        returnmsg = msg + "DFDf"
        if (c % 1000) == 0 :
            ns = tracemalloc.take_snapshot()
            stats = ns.compare_to(s, 'lineno')
            for stat in stats[:10]:
                print(stat)
            s = ns
        return returnmsg

    worker.set_recv_callback(recv)
    worker.start_recv(blocking=True)
