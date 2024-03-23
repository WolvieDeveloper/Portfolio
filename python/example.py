import time

x = 0

while(True):
    time.sleep(1)
    x = x+1
    print ("Ctr:",x)
    if (x>7):
        break

print("\nFinish")