class PowerCalculator:
    def power(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result

power_calculator = PowerCalculator()
x = 2
n = 5
print(power_calculator.power(x, n)) 