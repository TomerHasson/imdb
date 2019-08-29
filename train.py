import time
from cnvrg import Experiment
i = 0
while True:
    filename = "test-{file_idx}.log".format(file_idx=i)
    f = open(filename, "a")
    f.write("output/hello")
    f.close()
    Experiment.sync(message="my commit: %d" % i)
    time.sleep(60)
    i += 1
