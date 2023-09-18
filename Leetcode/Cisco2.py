"""
inputStr, represents the given string for the puzzle
"""


def funcSubstring(inputStr):
    # Write your code here
    substring_indices_list = []

    for i in range(len(inputStr)):
        # for each character find the longest substring which reads the same forwards and backwards
        # by extending out from the center until it is no longer the same
        # must do this for both even and odd cases

        # even case
        left = i - 1
        right = i
        while left >= 0 and right <= len(inputStr) - 1 and inputStr[left] == inputStr[right]:
            left -= 1
            right += 1

        left += 1
        right -= 1

        if right - left + 1 > 1:
            substring_indices_list.append((left, right))

        # odd case
        left = i - 1
        right = i + 1

        while left >= 0 and right <= len(inputStr) - 1 and inputStr[left] == inputStr[right]:
            left -= 1
            right += 1

        left += 1
        right -= 1
        if right - left + 1 > 1:
            substring_indices_list.append((left, right))

    max_length = -1
    curr_substring = "None"
    for index_pair in substring_indices_list:
        left, right = index_pair[0], index_pair[1]
        substring = inputStr[left: right + 1]
        length = right - left + 1
        if length > max_length and length > 1:
            max_length = right - left + 1
            curr_substring = substring
        elif length == max_length and substring < curr_substring:
            curr_substring = substring

    return curr_substring


def main():
    # input for inputStr
    inputStr = str(input())

    result = funcSubstring(inputStr)
    print(result)


if __name__ == "__main__":
    main()