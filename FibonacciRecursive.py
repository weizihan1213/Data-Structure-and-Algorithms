def fibonacci(num):
  if num < 2:
    return num
  return fibonacci(num - 1) + fibonacci(num - 2)

def fibonacciIter(n):
  results = [0, 1]
  for i in range(2, n+1):
    results.append(results[i-1] + results[i-2])
  return results[n]

print(fibonacci(0))
print(fibonacciIter(0))

print(fibonacci(4))
print(fibonacciIter(4))