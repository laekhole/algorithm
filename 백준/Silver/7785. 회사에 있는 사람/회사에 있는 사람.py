import sys
N = int(sys.stdin.readline())
pe = {}

for _ in range(N):
  p, c = sys.stdin.readline().split()

  if c == 'enter':
    pe[p] = 'enter'
  else:
    if pe[p]:
      del pe[p]

for people in sorted(pe, reverse=True):
  print(people)