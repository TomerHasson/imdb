from cnvrg import Experiment
import time
import os

e=Experiment()
e.log_param("test_acc", 0.6)
f = open("filename_06", "a")
f.write("hello")
f.close()
e.sync(message="my commit: 06")