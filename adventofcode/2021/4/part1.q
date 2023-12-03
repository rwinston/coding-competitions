data: read0 `:test.dat;
nums:"J"$'"," vs first data;
p:raze {"J"$x}@/:'({x where not ""~/:x} each data);
pp:-1_{5 cut 25#x}each ({25_x}\)p;



data: read0 `:part1.dat;
nums:"J"$'"," vs first data;
data:1_data;
data:data where {not x~""} each data;
p:raze flip ("JJJJJ";3 3 3 3 2) 0:data;
pp:-1_{25#x}each ({25_x}\)p;

