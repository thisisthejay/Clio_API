import pandas as pd
file = pd.read_csv('attorney.csv')
file.to_json(r'attorney.json',orient='records')