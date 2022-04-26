import matplotlib.pyplot as plt
#import pandas as pd

ll = [87.5,545,292.75,166.7,114.3]
RR = [2617.67,16452.47,8824.43,5012.678,3428.102]
ff = [13.66,2.859,7.894,9.394,12]

#print(len(ll))
#print(len(RR))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(ll, RR, ff)
ax.set_xlabel("Wing Length (mm)")
ax.set_ylabel("Reynold's Number")
ax.set_zlabel("Wingbeat Frequency")

plt.show()
