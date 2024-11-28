try:
    print("In the try")
except:
    print("In the exception")
finally:
    print("Ending")

# throw an exception
if 1 > 0:
    raise Exception("It is")