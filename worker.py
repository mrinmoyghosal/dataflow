from mgq import MgqWorker

if __name__ == "__main__":
    worker = MgqWorker("tcp://broker:5555", "work", True)
    worker.set_recv_callback(lambda x: x)
    worker.start_recv(blocking=True)
