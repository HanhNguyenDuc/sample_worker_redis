# Sample Worker with Redis

## 1. How to use:
  - install redis in requirements.txt
  - run worker_1.py to start publish product
  - run worker_master.py to take, store and publish product
  - run worker_2.py to take product and use it
## 2. Pipeline explaination
  - worker 2 take data from worker 1 and use it, but in fact, worker 2 is very slow and worker 1 is very fast, so we will split worker 1 to a process, and run some worker 2 to make speed better and avoid bottleneck.
  - worker_master is an worker to take and store message, if worker 1 complete preparing product for worker 2, it will send product to worker master for storing, if worker 2 is process product completely, it will bring another product to worker 2.
