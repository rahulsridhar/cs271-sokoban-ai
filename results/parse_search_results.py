import csv
from os import listdir
from os.path import isfile, join


def parse_file(filename, path):
    
    # Parse A* files
    writeFile = open(filename, 'w+')
    writer = csv.writer(writeFile)
    data = [['Document', '#States', 'RunningTime (in ns)', '#Moves']]
    writer.writerows(data)

    mypath = path
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for i in onlyfiles:
        if('.txt' not in i):
            continue
        count = 0
        #print i
        f = open(mypath+i,'r')
        x = f.readlines()
        for j, text in enumerate(x):
            if(count == 3):
                data = [[i, int(states), time, int(moves)]]
                writer.writerows(data)
                break
            if 'visited' in text:
                states = text.split("visited = ",1)[1] 
                count = count + 1
            if 'time =' in text:
                time = text.split("time = ",1)[1] 
                wordlist = text.split()
                time = wordlist[wordlist.index("=") + 1]
                count = count + 1
            if 'goal =' in text:
                moves = text.split("goal = ",1)[1] 
                count = count + 1        
            if('No solution found' in text):
                data = [[i, -1, -1, -1]]
                writer.writerows(data)
                break
            if(j==(len(x) - 1) and count!=3):
                data = [[i, -1, -1, -1]]
                writer.writerows(data)
                break
    writeFile.close()


parse_file('a_star.csv', 'a_star/')
parse_file('ida_star.csv', 'ida_star/')
parse_file('bfs.csv', 'bfs/')
