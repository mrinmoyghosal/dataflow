from mgq import MgqBroker

if __name__ == "__main__":
    broker = MgqBroker(5555, True)
    broker.start_brokering()
