from cnvrg import Experiment
import time
import os

e=Experiment()
e.log_param("test_acc", 0.8)
f = open("filename_08", "a")
f.write("hello")
f.close()
e.sync(message="my commit: 08")