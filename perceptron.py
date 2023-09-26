class Perceptron:
    def __init__(self, weight1, weight2, learnRate, threshold) -> None:
        self.weight1 = weight1
        self.weight2 = weight2
        self.learnRate = learnRate
        self.threshold = threshold

    def stepFunction(self, sum):
        return 1 if sum >= self.threshold else 0
        
    def train(self, input) -> None:
        updated = True
        print("\nWeight 1", "|", "Weight 2")
        while(updated):
            updated = False
            for i in input:
                sum = (self.weight1 * i[0]) + (self.weight2 * i[1])
                output = self.stepFunction(sum)
                print("{:.2f}".format(self.weight1), "   |", "{:.2f}".format(self.weight2))
                if output != i[2]:
                    updated = False
                    deltaWeight1 = self.learnRate * (i[2] - output) * i[0]
                    self.weight1 = self.weight1 + deltaWeight1
                    deltaWeight2 = self.learnRate * (i[2] - output) * i[1]
                    self.weight2 = self.weight2 + deltaWeight2

    def predict(self, a):
        sum = (self.weight1 * a[0]) + (self.weight2 * a[1])
        return self.stepFunction(sum)

x1 = int(input("Enter value 1: "))
x2 = int(input("Enter value 2: "))

weight1 = float(input("Enter weight 1: "))
weight2 = float(input("Enter weight 2: "))

learnRate = float(input("Enter learning rate: "))
threshold = int(input("Enter threshold: "))

data = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]

trainingData = [x1, x2]

perceptron = Perceptron(weight1, weight2, learnRate, threshold)

perceptron.train(data)
print("\nInput:", trainingData, "\nOutput:", perceptron.predict(trainingData))


