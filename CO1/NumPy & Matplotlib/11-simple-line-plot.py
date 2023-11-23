import matplotlib.pyplot as plt

numbers = input("Enter x values, separated by spaces: ").split()
x = [float(i) for i in numbers]

numbers = input("Enter y values, separated by spaces: ").split()
y = [float(i) for i in numbers]

plt.plot(x, y, marker = 'o', linestyle = '-', color = 'b', label = 'Data Points')

plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend() 

plt.show()

