import pandas as pd

marks = pd.read_csv('./CO1/mark.csv')

marks = marks.eval('Total = m1 + m2 + m3')

print("\nAverage m1 marks: ", marks['m1'].mean())
print("Average m2 marks: ", marks['m2'].mean())
print("Average m3 marks: ", marks['m3'].mean())

print("\nStudent with highest total marks:")
print(marks.loc[marks['Total'].idxmax()])

marks = marks.drop(marks['Total'].idxmax())

print("\nStudent with second highest total marks:") 
print(marks.loc[marks['Total'].idxmax()])




