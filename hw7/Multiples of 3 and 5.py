def solution(number):
    return sum(int(i) for i in range(number) if i % 3 == 0 or i % 5 == 0)