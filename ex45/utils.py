import time
import sys

def cool_print(text):
    for i in text: 
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0)   
    print   
