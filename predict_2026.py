import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# dataframe อ่าน csv
df = pd.read_csv('travel_predict.csv')

# Prepare Data
x = df[['Month_Num']]
y = df['Travel_Count']

# Training
model = LinearRegression()
model.fit(x, y)

# Set to 2D Array
X_future_2026 = np.arange(13, 25).reshape(-1, 1)

# Testing
y_predict_2026 = model.predict(X_future_2026)

# ติบลบไม่ได้
y_predict_2026 = np.maximum(y_predict_2026, 0)

# สร้าง DataFrame เปรียบเทียบ
months_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
comparison_df = pd.DataFrame({
    'Month': months_name,
    'Actually (2025)': y,
    'Predicted (2026)': y_predict_2026.flatten()
})

# Bar Chart Compare
comparison_df.plot(x='Month', kind='bar', figsize=(12, 6))
plt.title('Comparison: Actually (2025) vs Predicted (2026)')
plt.ylabel('Travel Count')
plt.xticks(rotation=0)
plt.show()