#!/usr/bin/python3
# creating pascal triangle


def pascal_triangle(n):
    holder = []
    if n <= 0:
        return holder
    else:
        for i in range(1, n+1):
            subholder = []
            c = 1
            for j in range(1, i+1):
                subholder.append(c * (i - j) // j)
        holder.append(subholder)
