##simple visualisation of data from examples folder

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys 
import os
from pathlib              import Path
from ietfdata.datatracker import *
from ietfdata.rfcindex    import *

# =============================================================================
# 
# # =============================================================================



sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



# =============================================================================

streams = {}
total = 0
legacy = 0

ri = RFCIndex()
for rfc in ri.rfcs():
    total += 1
    if rfc.stream == "Legacy":
        legacy += 1
    if rfc.stream in streams:
        streams[rfc.stream] += 1
    else:
        streams[rfc.stream] = 0

# for stream in streams:
#     print(f"{stream:11} : {streams[stream]:5d} ", end="")
#     print(f"({streams[stream] / total * 100:4.1f}%)", end="")
#     if stream != "Legacy":
#         print(f"  ({streams[stream] / (total - legacy) * 100:4.1f}% excluding legacy)", end="")
#     print(f"")

#run main func of rfc-streams.py
data = streams
df = pd.DataFrame.from_dict(data, orient='index')
df.plot(kind='bar', legend=False)
plt.title('RFC Streams')
plt.ylabel('Number of RFCs')
plt.xlabel('Stream')
#add lines to show percentages
plt.axhline(y=streams['IETF'], color='r', linestyle='-', label='IETF')
plt.axhline(y=streams['IRTF'], color='g', linestyle='-', label='IRTF')
plt.axhline(y=streams['Legacy'], color='b', linestyle='-', label='Legacy')
plt.axhline(y=streams['IAB'], color='y', linestyle='-', label='IAB')
# add percentage numbers and stream name to each line
plt.text(0, streams['IETF'], f"IETF={streams['IETF'] / total * 100:4.1f}%", ha='center', va='bottom')
plt.text(1, streams['IRTF'], f"IRTF={streams['IRTF'] / total * 100:4.1f}%", ha='center', va='bottom')
plt.text(2, streams['Legacy'], f"Legacy={streams['Legacy'] / total * 100:4.1f}%", ha='center', va='bottom')
plt.text(3, streams['IAB'], f"IAB={streams['IAB'] / total * 100:4.1f}%", ha='center', va='bottom')

plt.legend()
plt.show()

# =============================================================================




