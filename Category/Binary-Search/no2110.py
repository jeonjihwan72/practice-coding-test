# 문제 
'''
도현이의 집 N개가 수직선 위에 있다.
각각의 집의 좌표는 x1, ... , xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고,
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
'''

# 입력
'''
첫째 줄에 집의 개수 N(2 <= N <= 200,000)과 공유기의 개수 C(2 <= C <= N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 <= xi <= 1,000,000,000)가 한 줄에 하나씩 주어진다.
'''

# 출력
'''
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
'''

def can_install(houses, C, distance):
    count = 1  # 첫 번째 집에 공유기 설치
    last_installed = houses[0]  # 마지막으로 설치된 공유기의 위치

    for i in range(1, len(houses)):
        if houses[i] - last_installed >= distance:  # 최소 거리 유지 가능하면 설치
            count += 1
            last_installed = houses[i]
            if count >= C:
                return True  # C개 이상 설치 가능하면 True 반환
    
    return False  # C개 설치 불가능하면 False 반환

def find_max_distance(N, C, houses):
    houses.sort()  # 집의 좌표를 정렬
    
    left, right = 1, houses[-1] - houses[0]  # 가능한 최소 거리 ~ 최대 거리
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 중간 거리 기준
        if can_install(houses, C, mid):  
            answer = mid  # 최적 거리 갱신
            left = mid + 1  # 더 넓은 간격을 시도
        else:
            right = mid - 1  # 간격을 줄여서 시도

    return answer

# 입력 처리
N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

# 결과 출력
print("======= Result =======")
print(find_max_distance(N, C, houses))
