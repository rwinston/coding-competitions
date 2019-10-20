/ --------
/ Problem 1
input:read0`:c:/Users/rory/advent/problem1_in.txt

/ part 1
sum raze -1 1 inp="("

/ part 2
1+first where -1=sums raze -1 1 inp="("

/ --------
/ Problem 2
input:flip ("III";"x") 0:`:c:/Users/rory/advent/problem2_in.txt

/ part 1
sum {(min s)+sum 2*s:.[*]'[x cross x] 1 2 5} each input

/ part 2
sum {(prd x)+2*sum 2#asc x} each input

/ -------
/ Problem 3
/ part 1
input:raze read0`:c:/Users/rory/advent/problem3_in.txt
xs:{$[x="<";-1;x=">";1;0]}each input
ys:{$[x="v";-1;x="^";1;0]}each input
/ see the grid plus instructions
/ ((sums xs),'sums ys),'input
count distinct (enlist (0 0)),(sums xs),'sums ys

/ part 2
santa:{sums x where y=(sums count each input) mod 2}
count distinct (enlist (0 0)),(santa[xs;0],'santa[ys;0]),(santa[xs;1],'santa[ys;1])

/ --------
/ Problem 4
/ part 1
chk:{[hash]{first where not x="0"} raze string hash}
t:5;i:0 / target is 5 leading zeroes
while[t-chk[md5 seed,string i];i+:1]

/ part 2
t:6;i:0
while[t-chk[md5 seed,string i];i+:1]

/ --------
/ Problem 5
/ part 1
f1:{2<(sum x in "aeiou")}
f2:{0<sum (prev x)=x}
f3:{not any x like/:("*",'("ab";"cd";"pq";"xy"),\:"*")}
sum {all (f1;f2;f3)@\:x} each input

/ part 2	
f4:{1<sum first each 1_'deltas each value group x@0 1+/:til count x}
f5:{0<sum (prev prev x)=x} 

/---------
/ Problem 6
/ part 1
input:raze read0`:c:/sandbox/adventofcode/2015/data/problem6_in.txt
dispatch:`on`off`toggle!({x|1b};{x&0b};{(~:)x});
l:{[x]enlist (dispatch`$x[2]),"I"$"," vs/:(x[0];x[1])}'[{x@0 2 3} each {reverse " " vs x}each input]
{@[grid;s+til coords[x[1;0];x[1;1]]-s:coords[x[2;0];x[2;1]];x[0]]} each raze l
