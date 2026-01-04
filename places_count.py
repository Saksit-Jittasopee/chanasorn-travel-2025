import pandas as pd
import matplotlib.pyplot as plt

# dataframe อ่าน csv
df = pd.read_csv("travel.csv")

# ขนาดของ plot
plt.figure(figsize=(10, 7))

# นับจำนวนสถานที่ที่ไปบ่อยสุด
places_mode = df['Places'].value_counts().head(15)
places_counts = places_mode.sort_values(ascending=True)

# Horizontal Bar Chart
bars = plt.barh(y=places_counts.index, width=places_counts.values, color='green')

# ตัวเลขบนกราฟ
for bar in bars:
    width = bar.get_width() # ดึงค่าความยาวของแท่ง (จำนวนครั้ง)
    plt.text(
        width,           # ตำแหน่งแกน X (ปลายสุดของแท่ง)
        bar.get_y() + bar.get_height()/2, # ตำแหน่งแกน Y (กึ่งกลางความหนาแท่ง)
        f' {int(width)}', # ข้อความ (เว้นวรรคข้างหน้าเล็กน้อยให้ไม่ติดกราฟ)
        ha='left',       # จัดให้ข้อความอยู่ทางขวาของจุดพิกัด (Left alignment starts text at x)
        va='center'      # จัดกึ่งกลางแนวตั้ง
    )

# จัดระยะขอบให้อัตโนมัติป้องกันชื่อตกขอบ
plt.tight_layout()

# กำหนดขอบบนให้ลงมา 80%, ขอบล่างให้เหลือพื้นที่ 40% และขอบซ้าย 20% ของความสูงกราฟ
plt.subplots_adjust(top=0.8, bottom=0.4, left=0.2)

# ชื่อแกน x,y, หัวข้อ
plt.xlabel('Places Visited')
plt.title("Most Chanasorn's Places Visited in 2025")

# plot กราฟ
plt.show()