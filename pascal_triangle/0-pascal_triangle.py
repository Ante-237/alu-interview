#!/usr/bin/python3
# creating pascal triangle
from math import factorial


def pascal_triangle(n):
    holder = []
    if n <= 0:
        return holder
    else:
        for i in range(n):
            subholder = []
            for j in range(i+1):
                subholder.append(factorial(i)//(factorial(j)*factorial(i-j)))
        holder.append(subholder)
