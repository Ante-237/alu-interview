#!/usr/bin/python3
# creating pascal triangle
''' pascal triangle '''


def pascal_triangle(n):
    """ the only function """
    holder = []
    if n <= 0:
        return holder
    else:
        for i in range(1, n+1):
            subholder = []
            c = 1
            for j in range(1, i+1):
                c = c * (i - j) // j
                subholder.append(c)
        holder.append(subholder)
    return holder
