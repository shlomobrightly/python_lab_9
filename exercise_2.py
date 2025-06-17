"""

Name: check_matrix(matrix)

Input: a matrix

Output: True of False

Algorithm:  1- in a for loop in the matrix, if the length of eny of the rows are not equal to the length of the collums, returns False
            2- assumes the fist character of the first list is the smallest of the main diagnal. and sets m_a as 0
            3- in a for loop, runs as long as m_a is smaller than the length of the matrix
            4- in a for loop in the matrix, if i in the place of m_a is smaller than min_main, exchanges with min_main and adds 1 to min_main

            5- assumes the last character of the first list is the largest of the seccond diagnal. and sets m_a as the length of the matrix, minus 1.
            6- in a for loop, runs as long as m_a is larger than 0.
            7- in a for loop in the matrix, if i in the place of m_a is larger than max_second, exchanges with max_second and subtracts 1 to max_second
            8- in min_main is smaller than max_second, returns False, else, returns True




Name: main()

Input: a matrix

Output: matrix and True of False

Algorithm:  1- prints 'first matrix:'
            2- in a for loop in the given matrix, prints the rows
            3- prints 'is extreme matrix: '
            4- applies the check_matrix function on the matrix
            
            
"""





def check_matrix(matrix):
    for i in matrix:
        if len(i) != len (matrix):
            return False
        
    m_a = 0
    min_main = matrix[0][0]
    while m_a < len(matrix):
        for i in matrix:
            if i[m_a] < min_main:
                min_main = i[m_a]
            m_a += 1
    
    m_a = len(matrix) - 1
    max_second = matrix[0][len(matrix)-1]
    while m_a > 0:
        for i in matrix:
            if i[m_a] > max_second:
                max_second = i[m_a]
            m_a -= 1    
    if min_main >= max_second:
        return True
    else:
        return False
    
def main():
    
    print('first matrix:')
    m_1=[[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5]]
    for i in m_1:
        print(i)
    print('is extreme matrix: ', check_matrix(m_1)) 
    
    print('second matrix:')
    m_2=[[5,2,3,4,2],[6,7,8,3,0],[1,2,4,4,5],[1,2,3,4,5]]
    for i in m_2:
        print(i)
    print('is extreme matrix:', check_matrix(m_2)) 

    
    print('third matrix:')
    m_3=[[5,2,3,4,2],[6,7,8,3,0],[1,2,4,4,5],[6,0,8,9,0],[1,2,3,4,5]]
    for i in m_3:
        print(i)
    print('is extreme matrix:', check_matrix(m_3)) 
    
    
    print('fourth matrix:')
    m_4=[[1]]
    for i in m_4:
        print(i)
    print('is extreme matrix:', check_matrix(m_4)) 
    


main()

