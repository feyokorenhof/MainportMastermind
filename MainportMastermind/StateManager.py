import os
import csv
class State:
    MAINMENU='mainmenu'
    DOBBELEN='dobbelen'
    SPELVORDERING='spelvordering'

states = State

state = states.MAINMENU
muted = False

players = []

def saveState():
    csv_file = 'saves/save.csv'
    csv_columns = ['naam', 'inventaris']
    print(os.path.exists(csv_file))
    path = os.path.realpath(csv_file).replace('\\', '\\')
    with open(path, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in players[0]:
            writer.writerow(data)

        
    exit()
