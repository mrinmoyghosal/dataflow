# Dataflow

## Installation
```
docker-compose up --build --force-recreate
```
## Whats inside

1. A broker instance that will be continiously running
2. 3 instance of worker running all the time
3. 5 client worker job continiously sending 50k messages then dying and restarting again to send another 50k. This will happen continiously just to demonstrate it's capability of fast message processing, no message loss etc..