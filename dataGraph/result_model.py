import pandas as pd

df = pd.read_csv(r'C:\Users\HP\Desktop\dataset_graph\DisplayGraph\yt_sports_channels_stats.csv')


data_list = df.to_dict('records')


import matplotlib.pyplot as plt


subscriber_counts = [entry['subscriber_count'] for entry in data_list]
view_counts = [entry['view_count'] for entry in data_list]



# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(view_counts, subscriber_counts, alpha=0.5)
plt.title('Subscriber Count vs. View Count')
plt.xlabel('View Count')
plt.ylabel('Subscriber Count')
plt.grid(True)
plt.show()
