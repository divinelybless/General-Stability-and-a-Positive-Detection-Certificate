"""Finite-dimensional projective quantum persistence; VR H1 over F2."""
from pathlib import Path
import numpy as np

def rays(energies, times, weights):
    return np.sqrt(np.asarray(weights))[None, :] * np.exp(
        -1j * np.asarray(times)[:, None] * np.asarray(energies)[None, :]
    )

def fsdist(A, B=None):
    if B is None:
        B = A
    return np.arccos(np.clip(np.abs(A @ B.conj().T), 0, 1))

def vr_h1(D):
    """Finite VR H1 bars via complete 2-skeleton boundary reduction over F2.
    Filtration uses simplex diameter; edges precede triangles at ties.
    The implementation is intended for small point clouds.
    """
    n = len(D)
    edges = [(float(D[i,j]), i,j) for i in range(n) for j in range(i+1,n)]
    edges.sort(key=lambda z:(z[0],z[1],z[2]))
    pos = {(i,j):k for k,(_,i,j) in enumerate(edges)}
    parent = list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    births=set()
    for k,(_,i,j) in enumerate(edges):
        a,b=find(i),find(j)
        if a!=b:
            parent[b]=a
        else:
            births.add(k)
    triangles=[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                a,b,c=pos[i,j],pos[i,k],pos[j,k]
                triangles.append((max(edges[a][0],edges[b][0],edges[c][0]),a,b,c))
    triangles.sort(key=lambda z:z[0])
    pivots={}
    pairs=[]
    for death,a,b,c in triangles:
        col=(1<<a)^(1<<b)^(1<<c)
        while col:
            low=col.bit_length()-1
            if low not in pivots:
                pivots[low]=col
                if low in births and death>edges[low][0]+1e-12:
                    pairs.append((edges[low][0],death))
                break
            col ^= pivots[low]
    return np.array(sorted(pairs,key=lambda x:x[1]-x[0],reverse=True)).reshape((-1,2))
