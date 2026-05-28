import time as tm

print("hi")
tm.sleep(1.5)
print("how are u doing?")
r = input("")
tm.sleep(1.5)
if r == 'bad' or "im bad" or 'more lass'.lower():
    print("because?")
    tm.sleep(1.5)
    r = input("")
else:
    print("that's great")