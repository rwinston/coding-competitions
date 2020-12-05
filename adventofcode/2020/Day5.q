data:"\n"vs data;

/Part 1
calculateSeat:{[t]
f:{c:(floor(count x)%2);?[y=z;c#x;(c)_x]};
row:f/[til 128;-3_t;"F"];
seat:f/[til 8;-3#t;"L"];
(row*8)+seat
}; 

/ Part 1
seats:raze calculateSeat each data;
/ Part 2
first({(min x)+til(1+(max x)-(min x))} seats) except seats

