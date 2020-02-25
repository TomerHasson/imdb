import time
print("creating file")
f = open("output/exp3.txt", "a")
f.write("Now the file has more content!")
f.close()
time.sleep(100000)
