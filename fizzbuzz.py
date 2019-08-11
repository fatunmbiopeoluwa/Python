#Creating a fizzbuzz program
#to display any mutiple of 3 as fizz and
#any mutiple of 5 as buzz,
#then any multiple of both as fizzbuzz
#then return the number is it doesnt meet any of the requirements


def fizzbuzz(num):
    if num%3==0 and num%5==0:
        print("fizzbuzz")
    elif num%3==0:
        print('fizz')
    elif num%5==0:
        print("buzz")
    else:
        return num

#print(fizzbuzz())
