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
    csv_columns = ['naam', 'inventaris', 'haven']
    path = os.path.realpath(csv_file).replace('\\', '\\')
    if len(players) <= 0:
        with open(path, 'wb') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for e in range(5):
                writer.writerow('')
        
        exit()
    else:
        with open(path, 'wb') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for p in players:
                writer.writerow(p)    
        
        exit()
