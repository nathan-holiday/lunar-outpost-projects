import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import os
from datetime import datetime

#=====Config=====
INPUT_FILE = '/ros2_ws/temperature_log.csv'
OUTPUT_FILE_STEM = 'C_vs_t_graph'
OUTPUT_FILE_FOLDER = 'graphs'
#================

os.makedirs(OUTPUT_FILE_FOLDER, exist_ok=True)

plt.style.use('seaborn-v0_8-whitegrid')

df = pd.read_csv(INPUT_FILE)
df.timestamp = pd.to_datetime(df.timestamp)

fig,ax = plt.subplots()

x = df.timestamp
y = df.temperature_c

ax.plot(x,y)

ax.set(
    title = 'Temperature over time',
    xlabel = 'Time',
    ylabel = 'Temperature(C)'
)

#fix time axis display
ax.tick_params(axis='x', rotation=45)
locator = mdates.AutoDateLocator()
formatter = mdates.ConciseDateFormatter(locator)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)

plt.margins(x=0)
plt.tight_layout()

#save file with current time at the end of name
now = datetime.now()
file_name = OUTPUT_FILE_FOLDER + '/' + OUTPUT_FILE_STEM + '-' + now.strftime('%m-%d-%y-%H-%M-%S') + '.png'
plt.savefig(file_name)
