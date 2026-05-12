import time as tm

print("hi")
tm.sleep(1.5)
print("how are u doing?")
r = input("")
tm.sleep(1.5)
if r != 'well' or "im well" or 'nice' or 'im fine'.lower():
    print("because?")
    tm.sleep(1.5)
else:
    print("that's good")