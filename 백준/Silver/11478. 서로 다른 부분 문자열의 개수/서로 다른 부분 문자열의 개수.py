s = input()
substring_set = set()
for i in range(len(s)):
    for j in range(len(s), i, -1):
        substring_set.add(s[i:j])

count = len(substring_set)
print(count)