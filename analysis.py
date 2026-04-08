# analysis.py

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("log.csv", names=["timestamp", "size", "time", "speed"])

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour
df["speed_kb"] = df["speed"] 

print("\n===== STATISTICS =====")
print("Average Speed:", df["speed_kb"].mean(), "KB/s")
print("Max Speed:", df["speed_kb"].max(), "KB/s")
print("Min Speed:", df["speed_kb"].min(), "KB/s")

hourly = df.groupby("hour")["speed_kb"].mean()
busiest_hour = hourly.idxmin()

print("Busiest Hour (slowest):", busiest_hour)

# Plot graph
plt.plot(df["timestamp"], df["speed_kb"], marker='o')
plt.xlabel("Time")
plt.ylabel("Speed (kB/s)")
plt.title("Download Speed Over Time")
plt.xticks(rotation=45)
plt.tight_layout()

# Save graph (important for submission)
plt.savefig("speed_graph.png")

plt.show()