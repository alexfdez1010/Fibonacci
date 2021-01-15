#============================================================================
# Name        : Fibonacci.py
# Author      : Alejandro Fernández Camello
# Version     : 1.0
# Copyright   : GPL-3.0
# Description : Different implementations to calculate the n-term of the fibonacci sequence
#============================================================================

#Note: If you want to calculate a range of fibonacci numbers the best option will be using 
#the fibonacci dynamic programming top-down solution and will have practically a constant time
#because it will reutilizate the previous results
#in the case you want to calculate only one number the best option
#will be using the solution using a matrix with a logaritmic complexity

from math import sqrt,floor
import numpy as np

MOD = 10000000000 #For only show the last 10 digits in case the numbers are very long
MAX = 100000000 #Large number fibonacci that we are going to calculate in the dynamic programming solution
PHI = 1/2 + sqrt(5)/2 #Phi constant for the direct formula

#Different forms to calculate the n term of the fibonacci sequence

#Pure recursive form
#Complexity: O(PHI^n)

def fibonacci_recursive(n : int) -> int:
    if n <= 1:
        return n
    else:
        return (fibonacci_recursive(n-1) + fibonacci_recursive(n-2)) % MOD


#Dynamic programming top-down
#Complexity: O(n)

mem = [-1 for i in range(MAX)] #Array for memoization of the results that have been calculated

def fibonacci_dp_top(n : int) -> int:
    if n <= 1:
        return n
    if mem[n] == -1:
        mem[n] = (fibonacci_dp_top(n-1) + fibonacci_dp_top(n-2)) % MOD
    return mem[n]

#Classical iterative form
#Complexity O(n)

def fibonacci_classical(n : int) -> int:
    
    fib1 = 0
    fib2 = 1
    
    for _ in range(n):
        
        temp = fib2 % MOD
        fib2 += fib1
        fib1 = temp
        
    return fib1

#Using formula(can be wrong with large numbers)
#Complexity O(n)

def fibonacci_formula(n : int) -> int:
    
    return (int(floor((PHI**n - (1-PHI)**n)/sqrt(5))) % MOD)

#Using matrices with binary exponentation(Best form to get the n term of fibonacci numbers)
#Complexity O(log n)

initial_matrix = np.array([[0,1],
                          [1,1]])

identity = np.eye(2, dtype = np.int32)


def binary_exponential_matrix(matrix, n : int):
    
    if n == 0:
        
        return identity
    
    if n == 1:
       
        return matrix
    
    else:
        
        if n & 1 == 0:
            
            temp = binary_exponential_matrix(matrix,n//2)
            return (temp @ temp) % MOD
        
        else:
            
            return (matrix @ binary_exponential_matrix(matrix,n-1)) % MOD
            

def fibonacci_matrix(n : int) -> int:
    
    return binary_exponential_matrix(initial_matrix,n)[1][0]

if __name__ == "__main__": 

    for i in range(21):
        print(i," : ",fibonacci_recursive(i),end = " ")
        print(fibonacci_dp_top(i), end = " ")
        print(fibonacci_classical(i), end = " ")
        print(fibonacci_formula(i), end = " ")
        print(fibonacci_matrix(i))
    
    
    
