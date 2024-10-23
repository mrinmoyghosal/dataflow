from mgq import MgqBroker

if __name__ == "__main__":
    broker = MgqBroker(5555, False)
    broker.start_brokering()
