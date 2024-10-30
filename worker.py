import uuid
import os
from mgq import MgqWorker

if __name__ == "__main__":
    randomStr = uuid.uuid4().hex.upper()[0:6]
    broker=os.getenv("BROKER_SERVICE_PORT")
    worker = MgqWorker(broker, "work", False)
    worker.set_recv_callback(lambda x: x+' from '+randomStr)
    worker.start_recv(blocking=True)
