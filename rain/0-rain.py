#!/usr/bin/python3

def rain(walls):
    counter = 0
    width = 0
    height = 0
    path = []
    gap = []
    track = False
    for temp_one in walls:
        if counter == 0:
            if temp_one == 0:
                track = False
                counter += 1
            
            elif temp_one > 0:
                path.append(temp_one)
                track = True
                counter += 1
            continue

        if counter > len(walls):
            if temp_one == 0:
                break;

        if counter > 0:
            if temp_one < 1 and track:
                width += 1
                counter += 1
                continue
                


        if counter > 0:
            if temp_one > 1:
                gap.append(width)
                width = 0
                track = True
                path.append(temp_one)
                counter += 1
                continue

    print(gap)
    print(path)

walls = [0, 1, 0, 2, 0, 3, 0, 4]
rain(walls)

wall = [2, 0, 0, 4, 0, 0, 1, 0]
rain(wall)
