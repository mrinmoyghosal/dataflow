from mgq import MgqBroker

if __name__ == "__main__":
    broker = MgqBroker("Mybroker", 5555, False, True)
    broker.start_brokering()
