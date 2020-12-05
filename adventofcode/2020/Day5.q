data:"\n"vs data;

/Part 1
calculateSeat:{[t]
row:first{c:(floor(count x)%2);?[y="F";c#x;(c)_x]}/[til 128;-3_t];
seat:first{c:(floor(count x)%2);?[y="L";c#x;(c)_x]}/[til 8;-3#t];
(row*8)+seat
} 

/ Part 2
seats:calculateSeat each data;
({(min x)+til(1+(max x)-(min x))} seats) except seats

