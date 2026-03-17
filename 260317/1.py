# 예제 1번 요일 구하기
a = int(input())
a %= 7
output = ["일", "월", "화", "수", "목", "금", "토"]
print(output[a] + "요일")