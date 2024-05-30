import time
import math

def square_root(number):
    return math.sqrt(number)

def invoke_after_delay(number, delay):
    print("Wynik: ")
    time.sleep(delay / 1000) 
    result = square_root(number)
    print(result)

invoke_after_delay(16, 2000)  
invoke_after_delay(100, 5000)  
invoke_after_delay(25000, 10000)  
