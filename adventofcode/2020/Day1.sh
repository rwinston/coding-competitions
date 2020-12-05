#!/bin/bash
# AWK

# Data in a file called p1
# Part 1
awk 'BEGIN {} {A[$1]=2020-$1} END { for (i in A) {if (A[i] in A) print(A[i]*i)} }' p1

# Part 2
awk 'BEGIN {} {A[$1]=$1} END {for (i in A) {for (j in A){if (i!=j) {k=2020-(i+j); if(k in A){ print(i*j*k); break}}}}}' p1
