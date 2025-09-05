import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#load dataset

data = pd.read_csv('experience_salary.csv')

x = data[['yearsExperience']]
y = data[['salary']]


model = LinearRegression()
model.fit(x,y)

data["predictedsalary"] = model.predict(x)
print('model coefficient (slope)', round(float(model.coef_[0]),2))
print('model intercept (Base salary)', round(float(model.intercept_),2))

plt.scatter(x,y,color='blue',label = 'actual dta')
plt.plot(x,data["predictedsalary"], color ='red', label='regression line')
plt.xlabel('Years of experience ')
plt.ylabel('salary ')
plt.title("salary vs experinece")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()