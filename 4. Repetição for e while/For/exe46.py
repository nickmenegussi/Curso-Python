from time import sleep

for x in range(10, -1, -1):
    print(x) 
    sleep(1)
    if x == 0: 
        print("\033[34m BUM POWWWWW!")