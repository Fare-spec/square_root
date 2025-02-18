# Doing this repo just for fun, there is no real purpose behind this


def square_root(number: int, iteration: int):
    for i in range(int((number/2) +1)):
        if i**2 == number:
            return i
        elif i**2>number and (i-1)**2<number:
            if i**2 -number < (i-1)**2-number:
                digit = i
                print(digit)
                for _ in range(iteration):
                    a = number - digit**2
                    b = digit*2
                    digit = digit + a/b

            else:
                print(i-1)
                digit = i-1
                for _ in range(iteration):
                    a = number - digit**2
                    b = digit*2
                    digit = digit + a/b

            return digit



if __name__ == "__main__":
    number = int(input("please enter a number to square_root: "))
    precision = int(input("Please enter the number of iteration: "))
    square = square_root(number,precision)
    print(f"sqrt({number}) = {square}")
