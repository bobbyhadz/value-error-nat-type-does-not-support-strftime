# ValueError: NaTType does not support strftime

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl'],
    'salary': [175.1, 180.2, 190.3],
    'date_joined': ['2022-01-25', '2022-02-31', '2023-01-01']
})

date = pd.to_datetime(
    df['date_joined'],
    errors='coerce'
).dt.strftime('%Y-%m-%d')

print(date)