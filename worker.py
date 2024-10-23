import uuid
from mgq import MgqWorker

if __name__ == "__main__":
    randomStr = uuid.uuid4().hex.upper()[0:6]
    worker = MgqWorker("tcp://broker:5555", "work", False)
    worker.set_recv_callback(lambda x: x+' from '+randomStr)
    worker.start_recv(blocking=True)
