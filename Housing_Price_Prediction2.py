import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Dataset
data = {
    'area': [1400, 1600, 1700, 1875, 1100, 1550,2350, 2450, 1425, 1700],
    'bedrooms': [3, 3, 2, 4, 2, 3, 4, 4, 2, 3],
    'price': [245000, 312000, 279000, 308000, 199000, 219000, 405000, 324000, 319000, 255000]
}

df = pd.DataFrame(data)

# Features and target variable
X = df[['area', 'bedrooms']]
y = df['price']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Compare actual vs predicted values
for actual, predicted in zip(y_test, y_pred):
    print(f"Actual: {actual}, Predicted: {predicted:.2f}")

# Calculate the Mean Absolute Error
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

# Visualize the actual vs predicted prices
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs Predicted Prices")
plt.show()
