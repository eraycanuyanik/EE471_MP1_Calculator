from custom_classes import Calculator

# Create an instance of the Calculator class
my_calc = Calculator()

step1 = my_calc.add(10, 5)
step2 = my_calc.multiply(step1, 2)
final_result = my_calc.divide(step2, 3)

print(final_result)