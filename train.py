import time
import os
from cnvrg import Experiment
os.mkdir('output')
i = 0
while True:
    filename = "output/test-{file_idx}.log".format(file_idx=i)
    f = open(filename, "a")
    f.write("hello")
    f.close()
    Experiment.sync(message="my commit: %d" % i)
    time.sleep(60)
    i += 1
