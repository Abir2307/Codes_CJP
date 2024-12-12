'''
Problem Description
Vyom just learned about binary numbers. One day his tutor gave him T similar tasks and asked him to find the answer for them. As the number of tasks is more and also the size of input in each task is large, he concluded that manual calculation will be tough, so he decided to write a program for that.

Given T binary strings of varying lengths which consists of only 0s and 1s. He will be given two values A and B which indicates cost of one occurrence of sub strings "01" and "10". The total cost of the given string will be the sum of the costs of all "01" and "10". His task is to minimize the cost of given strings in each case, by rearranging it in any order. After he rearrange the string, he has to find the hamming distance between the original string and the rearranged string and print it in each case. In case of invalid input, print "INVALID". If there are more than one rearrangement which gives least cost, then consider the string which gives minimum hamming distance.

As Vyom is new to binary strings, he is a bit confused. Can you help Vyom to implement!

Note: The sub strings are considered in an overlapping manner i.e., in the string 010, there is one "01" and one "10".

Constraints
1 <= length of string <= 10^5

0 <= A,B <= 10^4

Input
First line consists of T the number of test cases.

For each test case there will be two lines, first line consists of the binary string and the second line consists of A and B separated by space.

Output
For each string, print the hamming distance in a new line.

Refer Examples section for more clarity.

Time Limit (secs)
1

Examples
Example 1

Input

2

0100

3 2

000

4 5

Output

2

0

Explanation

Here, cost of original string viz. 0100 is 5, because there is one occurrence of both "01" and "10". Now this string can be transformed into a new string viz. 1000 which is having one occurrence of "10". The cost of transformed string= (number of occurrences of "01")*3 + (number of occurrences of "10")*2 = 0*3 + 1*2 = 2 which is the minimum possible and the hamming distance of original and transformed string 2.

The string 000 has the cost of 0 which is minimum, and hence no need to do any transformation. So the hamming distance will be 0.

Example 2

Input

1

01001a10

1 2

Output

INVALID

Explanation

The given string is not binary string.'''
# Solution
def min_cost_and_find_hamming_distance(T, test_cases):
    results=[]
    for t in range(T):
        binary_string,cost=test_cases[t]
        if not all( c in '01' for c in binary_string):
            results.append('INVALID')
            continue
        A,B=map(int,cost.split())
        count_0=binary_string.count('0')
        count_1=len(binary_string)-count_0
        if A<B:
            rearranged_string='0'*count_0+'1'*count_1
        else:
            rearranged_string='1'*count_1+'0'*count_0
        hamming_distance=0
        for i in range(len(binary_string)):
            if binary_string[i]!=rearranged_string[i]:
                hamming_distance+=1
        results.append(hamming_distance)
    for res in results:
        print(res)
# Input parsing
T=int(input())
test_cases=[]
for _ in range(T):
    binary_string=input().strip()
    cost=input().strip()
    test_cases.append((binary_string,cost))
min_cost_and_find_hamming_distance(T,test_cases)