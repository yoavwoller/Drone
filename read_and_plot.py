import matplotlib.pyplot as plt
import json
from geopy import distance

json_f = open('landingData.JSON')
data = json.load(json_f)

lat_long_list = []
for entry in data:
    print(entry)
    cur = entry["time_boot_ms"], entry['lat']/(10**7), entry['lon']/(10**7)
    lat_long_list.append(cur)

target_pog = (- 35.3632296, 149.1652651)

print(lat_long_list)
lat_long_list.sort(key=lambda x: x[0])
print(lat_long_list)

deviation_vs_time = []
for entry in lat_long_list:
    entry_coords = entry[1], entry[2]
    cur = entry[0], round(distance.distance(entry_coords, target_pog).m, 2)
    deviation_vs_time.append(cur)

print(deviation_vs_time)

time = []
deviation = []
for e in deviation_vs_time:
    deviation.append(e[1]*100)
    time.append(e[0])

print(deviation)
print(time)


# red dashes, blue squares and green triangles
plt.plot(time, deviation, 'ro', time, deviation, 'k')
plt.axis([63000, 82000, 0, 300])
plt.show()






