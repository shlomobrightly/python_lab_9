"""

Name: minShiftedList

Input: ordered and shifted list of numbers

Output: the smallest number

Algorithm:  1- starts "left" as 0, and "right" as the lenght of the list, minus 1
            2- in a while loop, the program runs as long as "left" is smaller than "right"
            3- reffers "mid" as the middle element between "right" and "left"
            4- if the list in the index of "mid" is greater than list in the index of "right", renews "left" as "mid" + 1 
            5- otherwise, exchanges "right" with "mid"
            6- when the loop ends, returns list in index "left"
            



Name: main()

Input: ordered and shifted list of numbers

Output: text and the smallest number

Algorithm:  1- prints text
            2- in a while loop, runs the program as long as not given -1
            3- inputs numbers and appends them to a list
            4- when inputted -1, exits the loop, slices off the last character (-1)
            5- prints text, and prints the minimum number of the list by importing the minShiftedList function
"""


def minShiftedList(lst):
    left = 0
    right = len(lst) -1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] > lst[right]:
            left = mid +1
        else:
            right = mid
    return lst[left]




def main():

    lst = []
    print("Please enter ordered and shifted sequence of numbers (end with -1): ")
    while -1 not in lst:
        lst.append(int(input()))

    print("The smallest number is: ", end = "")
    s = lst[:len(lst) -1:]
    print(minShiftedList(s))

main()
