year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
else:
    print("You are special, a 1994ite")

## The problem is that there is no check for when age = 1994

