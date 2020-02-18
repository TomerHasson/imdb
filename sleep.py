import time
print("creating file)
f = open("output/first_exp.txt", "a")
f.write("Now the file has more content!")
f.close()
time.sleep(10)
