import pandas as pd

names = pd.Series(['apple', 'oranges', 'kiwi'])
df = names.to_frame(name = None)

df['prices'] = [50, 60, 80]
print(df)
