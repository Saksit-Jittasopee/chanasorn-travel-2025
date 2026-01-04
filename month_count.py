import pandas as pd
import matplotlib.pyplot as plt

# dataframe อ่าน csv
df = pd.read_csv("travel.csv")

# เรียงเดือนให้เป็นตามลำดับนี้
months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 
                'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)

# ขนาดของ plot
plt.figure(figsize=(10, 7))

# นับจำนวนสถานที่จากเดือน
monthly_counts = df['Month'].value_counts().sort_index()

# Bar Chart
bars = plt.bar(monthly_counts.index, monthly_counts.values, color='red', width=0.6)

# ตัวเลขบนกราฟ
for bar in bars:
    yval = bar.get_height()  # ดึงความสูงของกราฟ (จำนวน)
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # ตำแหน่งแกน X (กึ่งกลางแท่ง)
        yval,                               # ตำแหน่งแกน Y (ยอดกราฟ)
        int(yval),                          # ข้อความที่จะแสดง (แปลงเป็นจำนวนเต็ม)
        ha='center',    # จัดกึ่งกลางแนวนอน
        va='bottom'     # จัดให้ตัวหนังสืออยู่เหนือจุดที่กำหนด (ไม่ทับกราฟ)
    )

# แก้ปัญหาตัวหนังสือทับกัน - หมุนชื่อหนัง 45 องศา
plt.xticks(rotation=45, ha='right')

# จัดระยะขอบให้อัตโนมัติป้องกันชื่อตกขอบ
plt.tight_layout()

# กำหนดขอบบนให้ลงมา 80%, ขอบล่างให้เหลือพื้นที่ 40% และขอบซ้าย 10% ของความสูงกราฟ
plt.subplots_adjust(top=0.8, bottom=0.4, left=0.1)

# ชื่อแกน x,y, หัวข้อ
plt.xlabel('Month')
plt.ylabel('Places Count')
plt.title("Chanasorn's Travel Rate per Month in 2025")

# plot กราฟ
plt.show()