mode:{key[d] where max[c]=c:count each value d:group x};
minm:{key[d] where min[c]=c:count each value d:group x};
f:{2 sv raze y@'flip x};

/ test
test:{"J"$enlist each x}@/:read0 `:test.dat;
198 ~ f[test;mode] * f[test;minm]

/ part 1
data:{"J"$enlist each x}@/:read0 `:part1.dat;
f[data;mode] * f[data;minm]

/ part 2
data:{"J"$'x}@/:read0 `:part1.dat;
mode:{m:last deltas count each g asc key g:group x;$[m>0;1;m=0;1;0]};
f:{[x;i] .debug,:(x;i);$[(count x)=1;x;.z.s[x where (x[;i]=mode[x[;i]]);i+1] ] };
g:{[x;i] .debug,:(x;i);$[(count x)=1;x;.z.s[x where (x[;i]=not mode[x[;i]]);i+1] ] };
first prd 2 sv/:'(f[data;0];g[data;0])

