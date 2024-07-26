'''A positive integer d is said to be a factor of another positive integer Nif when N is divided by d,the remainder obtained is zero.For example, for number 12 there are 6 factors 1,2,3,4,6,12.Every integers has two i.e., 1 and itself
Constraints:
1<N<10000000000
1<k<600
You can assume that N will have no prime factors which are larger than 13
Example:
input:12,3
output:4
Explanation:N is 12,k is 3.The factors of 12 are(1,2,3,4,6,12).The highest factor is 12 and the third highest factor is 4.The output must be 4.'''
N,k=map(int,input().split())
for deno in range(N,0,-1):
    if N%deno==0:
        k-=1
    if k==0:
        print(deno)
        break
if k!=0:
    print('1')

def large(N, k):
    for deno in range(N, 0, -1):
        if N % deno == 0:
            k -= 1
            if k == 0:
                return deno
    return 1

N, k = map(int, input().split())
print(large(N, k))
