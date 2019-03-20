#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. 
Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. 
You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. 
There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. 
The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, 
returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
"""
    
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]

def solution(S,P,Q):
    S = list(S)
    A = [1 if x=='A' else 0 for x in S]
    C = [1 if x=='C' else 0 for x in S]
    G = [1 if x=='G' else 0 for x in S]
    
    prefix_sum_A = prefix_sums(A)
    prefix_sum_C = prefix_sums(C)
    prefix_sum_G = prefix_sums(G)
    
    m = len(P)
    result = [0]*m
    for i in range(0,m):
        result_A = count_total(prefix_sum_A,P[i],Q[i])
        result_C = count_total(prefix_sum_C,P[i],Q[i])
        result_G = count_total(prefix_sum_G,P[i],Q[i])
        if result_A > 0:
            result[i] = 1
        elif result_C > 0:
            result[i] =  2
        elif result_G>0:
            result[i] =  3
        else:
            result[i] =  4
    return result
    

