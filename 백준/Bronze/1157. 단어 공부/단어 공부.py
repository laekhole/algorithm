word = input().lower()

# 알파벳별 개수를 저장하는 딕셔너리
counts = {}

# 각 알파벳의 개수를 세어 딕셔너리에 저장
for char in word:
    if char.isalpha():
        counts[char] = counts.get(char, 0) + 1

# 딕셔너리에서 가장 큰 값을 찾음
max_count = max(counts.values())

# 딕셔너리에서 가장 큰 값을 가지는 키를 찾음
max_chars = [char.upper() for char, count in counts.items() if count == max_count]

# 출력
if len(max_chars) == 1:
    print(max_chars[0])
else:
    print('?')