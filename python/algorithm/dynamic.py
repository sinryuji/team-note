# 피보나치 수열 재귀 함수
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

# 한 번 계산된 결과를 메머이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 수열을 재귀함수, 탑다운 다이나믹 프로그래밍 방식으로 구현
def fibo_dynamic(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계싼한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 2
n = 99

# 피보나치 수열을 반복문, 바텀업 다이나믹 프로그래밍 방식으로 구현
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
