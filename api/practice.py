import pandas as pd
import os
import glob
from Backend.Backend.settings import BASE_DIR
from datetime import datetime, date

from PIL._imaging import display

path = os.path.join(BASE_DIR / 'media')
extension = 'csv'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
csv_file = result[0]
df = pd.read_csv(csv_file)
df["stufull_name"] = df["stuf_name"] + df["stul_name"]
# print(df["stufull_name"])

df["Username"] = df["stufull_name"].str[:4] + df["stufull_name"].str[-4:]
print(df["Username"])

df["stu_dob"] = pd.to_datetime(df['stu_dob'], dayfirst=True)
print(df["stu_dob"])
today = date.today()


def age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


df['Age'] = df['stu_dob'].apply(age)

print(df['Age'])

for i in df['Age']:
    if i <= 18:
        print('Kid', i)
    elif 18 < i <= 40:
        print('Adult', i)
    elif i > 40:
        print('Old Age', i)


