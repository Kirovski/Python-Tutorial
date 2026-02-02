import random
def my_age(age):
    if age > 2:
        return "Higher than 2"
    else:
        return "Lower than 2"
print(my_age(random.randint(0,10)))
