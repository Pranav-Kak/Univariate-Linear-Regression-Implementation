import numpy as np

n = int(input("Enter the size of training data:"))

x = np.zeros(n)  # features
y = np.zeros(n)  # response
h = np.zeros(n)  # hypothesis

print("Enter feature vector")
for i in range(n):
    x[i] = float(input())
print("Enter response vector")
for i in range(n):
    y[i] = float(input())
print("Enter initial values of intercept and slope")
print("(Use any random value like setting both to 1)")
a = float(input())
b = float(input())


def hypothesis():
    for i in range(n):
        h[i] = a + b*x[i]


hypothesis()  # intializing h with intial values of a and b given by user

# used in calculating the new value of intercept


def aFormula():
    total: float = 0
    for i in range(n):
        total = total + h[i] - y[i]
    return total

# used in calculating the new value of slope


def bFormula():
    total: float = 0
    for i in range(n):
        total = total + (h[i] - y[i])*x[i]
    return total


print("Enter Learning rate")
print("(Use a small random value like 0.01)")
l = float(input())
print("Enter Number of Iterations")
print("(Use a large random value like 10000)")
it = int(input())

# updating our intercept and slope
for i in range(it):
    a = a - (l/n)*aFormula()
    b = b - (l/n)*bFormula()
    hypothesis()

print("The value of intercept and slope of our hypothesis after training are:")
print(a, b)

t = int(input("Enter the size of Test Data:"))
test = np.zeros(t)
print("Enter test data:")
for i in range(t):
    test[i] = float(input())
print("Predicted values for given test data:")
for i in range(t):
    test[i] = a + b*test[i]
print(test)
