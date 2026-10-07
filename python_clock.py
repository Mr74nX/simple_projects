import datetime
import sys
def time():
    while True:
        clock=datetime.datetime.now().strftime("%I:%M:%S %p")# if use 12h formate must replace %H to %I and %p to am pm 
        sys.stdout.write(f"\r{clock} ")
print(time())
