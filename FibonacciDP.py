mem = {}
calculation = 0
def fibonacciDP(n):
  global calculation
  calculation += 1
  if n in mem:
    return mem[n]
  elif n < 2:
    return n
  else:
    mem[n] = fibonacciDP(n-1) + fibonacciDP(n-2)
    return mem[n]

print(fibonacciDP(10))
print(calculation)