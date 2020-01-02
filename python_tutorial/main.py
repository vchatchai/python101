from fibo import fib, fib2
import fibo
import importlib
print(fibo.__name__)
print(fib(1000))
print(fibo.fib2(100))
importlib.reload(fibo)
