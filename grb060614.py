


import matplotlib.pyplot as plt

#read file
data_file = 'C:/Users/Dell/Documents/Rband.txt'  
date = []
magnitude = []
sigma = []
instrument = []
with open(data_file, 'r') as file:
    next(file)  # Skip the header line
    for line in file:
        if line.startswith('[days]'):
            continue  
        values = line.strip().split()
        date.append(float(values[0]))
        magnitude.append(float(values[1]))
        sigma.append(float(values[2]))
        instrument.append(values[3])

#Assigning  color to each instrument
color_mapping = {
    'D1.5m+DFOSC': 'blue',
    'SSO': 'red',
    'Watcher': 'green',
    'VLT+FORS2': 'purple',
    'VLT+FORS1': 'orange'
}

#Plotting 
plt.figure(figsize=(8, 6))
for i in range(len(date)):
    plt.errorbar(date[i], magnitude[i], yerr=sigma[i], fmt='o', markersize=4, color=color_mapping[instrument[i]])
#add a legend box
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=7, label=instrument)
                   for instrument, color in color_mapping.items()]
plt.legend(handles=legend_elements)

plt.xlabel('Time [days]')
plt.ylabel('Magnitude')
plt.title('GRB 060614 ')
plt.grid(True)
plt.show()

