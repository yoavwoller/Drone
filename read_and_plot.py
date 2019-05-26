import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import json
from geopy import distance

# constants
latlong_exponent = 10**7
msec_to_sec = 1/1000
m_to_cm = 100

# givens
target_pog = (- 35.3632296, 149.1652651)


# class definitions
class DataPoint:
    def __init__(self, time, lat, long):
        self.time = time
        self.lat = lat
        self.long = long


# read data from file
json_f = open('landingData.JSON')
data = json.load(json_f)

# organize into data structure
point_list = []
for entry in data:
    point_list.append(DataPoint(time=entry["time_boot_ms"],
                                lat=entry['lat']/latlong_exponent,
                                long=entry['lon']/latlong_exponent))

# sort points by time in increasing order
point_list.sort(key=lambda x: x.time)

# collect and compute data to plot
deviation_to_time = []
for point in point_list:
    deviation = round(distance.distance((point.lat, point.long), target_pog).m, 2)
    deviation_to_time.append((point.time * msec_to_sec, deviation * m_to_cm))

# prepare data to plot
data_in_array = np.array(deviation_to_time)
transposed = data_in_array.T
x, y = transposed

# plot data
fig, ax = plt.subplots(1, 1)
ax.set_xlim(63, 82)
ax.set_ylim(0, 300)
ax.plot(x, y, 'ro')
ax.plot(x, y, 'b-')
plt.xlabel('Time (seconds)')
plt.ylabel('Deviation from POG (cm)')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
plt.grid(True)
plt.show()
