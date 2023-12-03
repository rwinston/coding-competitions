data:read0 `:part1.dat;
tab:update move:`$move,n:"J"$n from select from flip(`move`n)!flip {" " vs x}each data;

/ part 1
pos:(0;0);
lambda:`forward`down`up!({x+(1;0)};{x+(0;-1)};{x+(0;1)});
moves:lambda@tab`move;
last {x*y}\[sum(moves)@\:pos];

/ test 
data:read0 `:part1_test.dat;
tab:update move:`$move,n:"J"$n from select from flip(`move`n)!flip {" " vs x}each data;

