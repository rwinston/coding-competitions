/ Part 1
data:"J"$read0 `:data.csv
sum(1_deltas data)>0

/ Test 
test:"J"$read0 `:test.dat
5i~sum(1_deltas sum each 2_{1_x,y}\[3#0;test])>0

/ Part 2
sum(1_deltas sum each 2_{1_x,y}\[3#0;data])>0
