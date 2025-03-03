# 문제 
'''
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... S(k-1) < Sk > S(k+1) > ... S(N-1) > SN 을 만족한다면,
그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10,20,30,25,20}과 {10,20,30,40}, {50,40,25,10}은 바이토닉 수열이지만,
{1,2,3,2,1,2,3,2,1}과 {10,20,30,40,20,30}은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다.
(1 <= N <= 1,000, 1 <= Ai <= 1,000)
'''

# 출력
'''
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.
'''

# def check_bitonic(array):
#     is_bitonic = True
#     rising = True
    
#     for i in range(0,len(array)-1):
#         if rising == True and array[i] < array[i+1]:
#             continue
#         elif rising == True and array[i] > array[i+1]:
#             rising = False
#             continue
#         elif rising == False and array[i] > array[i+1]:
#             continue
#         elif rising == False and array[i] < array[i+1]:
#             is_bitonic = False
#             break
    
#     return is_bitonic

def longest_bitonic_subsequence(N, A):
    # 증가 부분 수열 (LIS)
    dp_incr = [1] * N  
    for i in range(N):
        for j in range(i):
            if A[j] < A[i]:
                dp_incr[i] = max(dp_incr[i], dp_incr[j] + 1)

    # 감소 부분 수열 (LDS)
    dp_decr = [1] * N  
    for i in range(N-1, -1, -1):
        for j in range(i+1, N):
            if A[j] < A[i]:
                dp_decr[i] = max(dp_decr[i], dp_decr[j] + 1)

    # 가장 긴 바이토닉 부분 수열 찾기
    max_length = 0
    for i in range(N):
        max_length = max(max_length, dp_incr[i] + dp_decr[i] - 1)

    return max_length

# 입력 받기
N = int(input("N: "))
A = list(map(int, input().split()))

# 결과 출력
print(longest_bitonic_subsequence(N, A))
