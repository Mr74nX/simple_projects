import sys,time
timer=int(input("Set Timer: "))
for i in range(timer, 0, -1):
    sys.stdout.write(f"\rTime Remaining: {i}  ")
    sys.stdout.flush()
    time.sleep(1)
print("Time's up!")
