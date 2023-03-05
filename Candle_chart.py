import matplotlib.pyplot as plt
import mpl_finance as mpf
import numpy as np

# Generate sample data
price = np.array([100, 105, 110, 100, 95, 105, 120, 125, 115, 110, 115, 105])
time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Define candlestick width
candle_width = 0.5

# Calculate the number of candles based on the time length of each candle
time_length = 3
num_candles = int(len(time) / time_length)

# Reshape the price and time arrays into a matrix with the specified number of candles
price_matrix = np.reshape(price[:num_candles*time_length], (num_candles, time_length))
time_matrix = np.reshape(time[:num_candles*time_length], (num_candles, time_length))

# Calculate the candlestick values
open_values = price_matrix[:, 0]
high_values = np.max(price_matrix, axis=1)
low_values = np.min(price_matrix, axis=1)
close_values = price_matrix[:, -1]

# Create a new figure and set the title
fig, ax = plt.subplots(figsize=(16,8))
ax.set_title('Candlestick Chart')

# Plot the candlestick chart
mpf.candlestick2_ochl(ax, open_values, close_values, high_values, low_values, width=candle_width)

# Set the x-axis tick labels to the midpoint of each candle
ax.set_xticks(np.arange(time_length/2, len(time_matrix)*time_length, time_length))
ax.set_xticklabels(time_matrix[:, 0])

# Display the chart
plt.show()