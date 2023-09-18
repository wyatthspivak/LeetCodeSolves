"""
inputNum, represents the given number.
"""


def funcFizzBuzz(inputNum):
    # Write your code here
    for i in range(1, inputNum + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")

        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")

        else:
            print(str(i))

    return


def main():
    # input for inputNum
    inputNum = int(input())

    result = funcFizzBuzz(inputNum)
    print(result)


if __name__ == "__main__":
    main()