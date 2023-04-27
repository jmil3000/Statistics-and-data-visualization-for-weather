import csv
import math
import random
import statistics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read temperature data from CSV file
with open('temp_data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Extract temperatures from data and convert to float
temperatures = [float(row[1]) for row in data[1:]]

# Compute the sample mean
print("#1: ")
sample_mean = sum(temperatures) / len(temperatures)
print("Sample mean: ", sample_mean)

# Compute the sample median
sorted_temperatures = sorted(temperatures)
mid = len(sorted_temperatures) // 2
sample_median = (sorted_temperatures[mid] + sorted_temperatures[-mid-1]) / 2 if len(sorted_temperatures) % 2 == 0 else sorted_temperatures[mid]
print("Sample median: ", sample_median)

# Compute the sample variance
print("#2: ")
sample_variance = sum((t - sample_mean) ** 2 for t in temperatures) / (len(temperatures) - 1)
print("Sample variance: ", sample_variance)

# Compute the sample standard deviation
sample_stddev = math.sqrt(sample_variance)
print("Sample standard deviation: ", sample_stddev)

# Use Simple Random Sampling to select 20 samples
print("#3: ")
samples = random.sample(temperatures, 20)

# Compute the sample mean of the 20 samples
sample_mean_20 = sum(samples) / len(samples)
print("Sample mean (20 samples): ", sample_mean_20)

# Compute the sample variance of the 20 samples
sample_variance_20 = sum((t - sample_mean_20) ** 2 for t in samples) / (len(samples) - 1)
print("Sample variance (20 samples): ", sample_variance_20)

# Discuss results
#################
print("#4: ")
print("The results found in parts one two and three represent the mean, median, variance, and standard deviation for the sample,") 
print("as well as the mean and variance for the SRS of 20 samples.")
print("The mean represents the average value from the sample. The median is the true center of the sample")
print("The variance and standard deviation show the change and variability in the sample data points")

# Calculate the number of values to trim for 5%, 10%, and 20% trimmed mean
print("#5: ")
trim_5 = math.ceil(0.05 * len(temperatures))
trim_10 = math.ceil(0.10 * len(temperatures))
trim_20 = math.ceil(0.20 * len(temperatures))

# Sort the temperatures in ascending order
sorted_temps = sorted(temperatures)

# Calculate the trimmed means
trimmed_mean_5 = sum(sorted_temps[trim_5:-trim_5]) / (len(temperatures) - 2 * trim_5)
trimmed_mean_10 = sum(sorted_temps[trim_10:-trim_10]) / (len(temperatures) - 2 * trim_10)
trimmed_mean_20 = sum(sorted_temps[trim_20:-trim_20]) / (len(temperatures) - 2 * trim_20)

# Print the trimmed means
print("5% trimmed mean: ", trimmed_mean_5)
print("10% trimmed mean: ", trimmed_mean_10)
print("20% trimmed mean: ", trimmed_mean_20)

# Calculate the indices of the quartiles
print("#6: ")
n = len(sorted_temps)
q1_index = math.floor(0.25 * (n+1)) - 1
q3_index = math.floor(0.75 * (n+1)) - 1

# Calculate the quartile values
q1 = sorted_temps[q1_index]
q3 = sorted_temps[q3_index]

# Print the quartile values
print("First quartile (Q1): ", q1)
print("Third quartile (Q3): ", q3)

# Calculate the mode and median (this time with statistics module)
print("#7: ")
mode = statistics.mode(temperatures)
median = statistics.median(temperatures)

# Plot the dot plot
plt.plot(temperatures, [0]*len(temperatures), 'o')
plt.title("Dot Plot of Temperatures")
plt.xlabel("Temperature (F)")
plt.yticks([])
plt.show()

# Print the mode and median
print("Mode: ", mode)
print("Median: ", median)

# Construct histogram
print("#8: ")
plt.hist(temperatures, bins=20, edgecolor='black')
plt.title("Histogram of Temperatures")
plt.xlabel("Temperature (F)")
plt.ylabel("Frequency")
plt.show()

# Construct boxplot
print("#9: ")
plt.boxplot(temperatures)
plt.title("Boxplot of Temperatures")
plt.ylabel("Temperature (F)")
plt.show()
print("No outliers are find")

# Load the dataset
temp_data = pd.read_csv("temp_data.csv")

# Filter to just the first week of the year
first_week = temp_data[temp_data["Date"].between("1/1/2022", "1/7/2022")]

# Calculate the mean and standard deviation of temperatures in the first week
mean = np.mean(first_week["Temp"])
std_dev = np.std(first_week["Temp"])

# Predict the temperature for each day in the first week of next year
next_year_temps = []
for _ in range(1, 8):
    # Use a normal distribution to generate a random temperature based on the mean and standard deviation
    temp = np.random.normal(mean, std_dev)
    next_year_temps.append(temp)
print("#10: ")
print("Predicted temperatures for the first week of next year:")
for i, temp in enumerate(next_year_temps):
    print("1/{}/{}, {:.2f} degrees".format(i+1, 2023, temp))