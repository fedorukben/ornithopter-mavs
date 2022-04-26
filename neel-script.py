#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

def normalize(raw):
    return [float(i)/max(raw) for i in raw]
#labels=['Chickadee','Tern', 'Pigeon', 'Lark', 'Finch']
#markers = [0.2,0.4,0.6,0.8,1.0]
#str_markers = ["0", "1", "2", "3", "4", "5"]
ll = normalize([87.5,545,292.75,166.7,114.3])
RR = normalize([2617.67,16452.47,8824.43,5012.678,3428.102])
ff = normalize([13.66,2.859,7.894,9.394,12])
ww = normalize([11,100,358.7,31,21])

labels = ['Wing Length', 'Reynold\'s Number', 'Wingbeat Frequency', 'Weight']
markers = [0.25, 0.5, 0.75, 1.0]
str_markers = ["0",'1','2','3','4']


#chickadee = normalize([87.5,2617.67,13.66,11])
#tern = normalize([545,16452.47,2.859,100])
#pigeon = normalize([292.75,8824.43,7.894,358.7])
#lark = normalize([166.7,5012.678,9.394,31])
#finch = normalize([114.3,3428.102,12,21])

def make_radar_chart(name, stats, fig, attribute_labels=labels,
                     plot_markers=markers, plot_str_markers=str_markers):

    labels = np.array(attribute_labels)

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    for idx,stat in enumerate(stats):
        stats[idx] = np.concatenate((stat,[stat[0]]))
    angles = np.concatenate((angles,[angles[0]]))

    #fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    print(angles)
    for stat in stats:
        print(stat)
    for stat in stats:
        ax.plot(angles, stat, 'o-', linewidth=2)
        ax.fill(angles, stat, alpha=0.25)
    #ax.set_thetagrids(angles * 180/np.pi, labels)
    plt.yticks(markers)
    ax.set_title(name)
    ax.grid(True)

    #ax.legend()
    ax.legend(['Chickadee','','Tern','','Pigeon','','Lark','','Finch'])



    #return plt.show()

fig = plt.figure()

data = [ll,RR,ff,ww]
birds = [[],[],[],[],[]]
for i,d in enumerate(data):
    for j,x in enumerate(d):
        birds[j].append(x)
print(birds)

make_radar_chart("Try1", birds, fig)
#make_radar_chart("Try", [1,2,3,4,5], fig)


plt.show()
