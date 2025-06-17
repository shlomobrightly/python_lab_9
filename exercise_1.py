"""

Name: max_letter

Input: a string

Output: returns the letter witch appears the most in the string. "-1" if there are no given letters.

Algorithm:  1- creates a counter list. duplicating "0" 26 times in a list.
            2- in a for loop, itirates over the given string. if numbers are between "A" or "Z" or between "a" and "z": adds 1 to the couunter list in index of acii i minus ascii "a" or "A".
            3- if the couner list as only zeroes, returns -1
            4- assumes the largest number is the first  in the counter list.
            5- in a for loop in the counter list, if a number is larger than max_l, exchanges them.
            6- returns the ascii character of the index of max_l plus the ascii of "a"



Name: main()

Input: a string

Output: returns the letter witch appears the most in the string. "-1" if there are no given lettersself. and a message if inputed "quit" or "Quit"

Algorithm:  1- creates a empty string
            2- creates a for loop, running as long as not given "quit" or "Quit"
            3- inputs a string. if given "quit" or "Quit", outputs a message and exits the program
            4- applies the max_letter function on the given string. if returns -1, prints an empty string
            5- elsewise, prints a message with applying the max_letter function on the string and prints the output of max_letter



"""

def max_letter(string):
    cnt = [0]*26

    for i in string:
        if "a" <= i <= "z":
            cnt[ord(i) - ord("a")] += 1        
        elif "A" <= i <= "Z":
            cnt[ord(i) - ord("A")] += 1        
    if cnt == [0]*26:
        return -1

            
    max_l = cnt[0]
    for i in cnt:
        if i > max_l:
            max_l = i
    return chr(cnt.index(max_l) + ord("a"))
  
    
def main():
    
    a = ""
    while a != "Quit" or a != "quit":
        a = input("Enter a string, please: ")
        if a == "Quit" or a == "quit":
            print("Thank you for exploring strings and complexity")
            return
        elif max_letter(a) == -1:
            print(max_letter(a))
        else:
            print("The most frequent letter is ", end = "")
            print(max_letter(a))
            

main()    
