import matplotlib.pyplot as plt

data = [
    {"x": 1, "y": 5, "label": "A", "color": "red", "marker": "o"},
    {"x": 2, "y": 4, "label": "B", "color": "blue", "marker": "^"},
    {"x": 3, "y": 6, "label": "C", "color": "green", "marker": "s"},
    {"x": 4, "y": 3, "label": "D", "color": "purple", "marker": "D"},
]

for i in data:
    plt.scatter(i["x"], i["y"], label = i["label"], color = i["color"], marker = i["marker"])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()


plt.show()