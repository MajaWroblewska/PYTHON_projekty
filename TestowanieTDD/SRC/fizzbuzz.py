def fizzbuzz(x):
    if x<1 or x>100:
        return 0
    if x%15==0:
        return "FizzBuzz"
    elif x%3==0:
        return "Fizz"
    elif x%5==0:
        return 'Buzz'
    else:
        return x

