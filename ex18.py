def print_two(*args):
    arg1,arg2 = args
    print(f"arg1: {arg1}, arg2:{arg2}")

def print_two_again(arg1, arg2):
        print(f"arg1: {arg1}, arg2:{arg2}")

#takes one argument
def print_one(arg1):
      print(f"arg1: {arg1}")

#no arguments
def print_none():
      print("I got nothing!!")

print_two("emi","malik")
print_two_again("emi","malik")
print_one("first!")
print_none()