"""
inputNum1, represents the number X.
inputNum2, represents the number Y.
"""


def funcCount(inputNum1, inputNum2):
    # Write your code here
    count = 0
    for i in range(inputNum1 + 1):
        string_i = str(i)
        list_i = list(string_i)
        sum = 0
        for string_dig in list_i:
            dig = int(string_dig)
            sum += dig

        if sum == inputNum2:
            count += 1

    return count


def main():
    # input for inputNum1
    inputNum1 = int(input())

    # input for inputNum2
    inputNum2 = int(input())

    result = funcCount(inputNum1, inputNum2)
    print(result)


if __name__ == "__main__":
    main()