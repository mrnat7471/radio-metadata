import time
import json

with open('music.json', 'r') as f:
    json = json.load(f)
    songs = json['songs']

a = False
while a == False:
    currentTime = round(time.time())
    endTime = currentTime+30
    print(currentTime)

    for song in songs:
        unix = song['time']
        title = song['title']
        if(unix >= currentTime and unix <= endTime):
            print(title)
            f = open("song.txt", "w")
            f.write(title)
            f.close()
        else:
            pass

    time.sleep(5)