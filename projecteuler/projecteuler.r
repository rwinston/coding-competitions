# problem 1
#x <- seq(1,999)
#sum(x[x %% 3 ==0 | x %% 5 == 0])

# problem 1
# method 2
# Sn <- n*((a1+an)/2), where n <- floor(N/n), and an <- n*a1
#sum(333*((3+333*3)/2),199*((5+199*5)/2)-66*((15+66*15)/2))
 
## Problem 2
# returns a list of Fibonacci numbers less than n
fib <- function(n) {
 x <- c(length=10)
 x[1] <- 1; x[2] <- 2
 for (i in 3:n) {
  y <- x[i-1]+x[i-2];
  if (y > n){ break }
  else { x[i] <- y }
 }
 x
}
 
#sum (fib(4E6)[ seq(2,length(f),by=2) ])
#f <- fib(4E6)
#sum( f[f %% 2 == 0] ) 
 
# problem 3
# Sieve of Eratosthenes
sieve <- function(n) {
 a <- seq(2,n)
 b <- c()
 b[1] <- 2
 
 i <- 1
 while (length(a) > 0) {
  b[i] <- a[1]
  i <- i + 1
  a <- a[!(a %% a[1] == 0)]
 }
 b
}
 
pfactor <- function(x) {
 factors <- c()
 j <- 1
 primes <- sieve( floor(sqrt(x)) )
 for (prime in primes) {
  if (x %% prime == 0) {
   factors[j] <- prime
   j <- j + 1
 }
 }
 factors
}
 
# max( pfactor(600851475143) )

#problem 6
# method 1
sumdiff <- function(n) {
	sum(c(1:n))^2-sum(c(1:n)^2)
}

#problem 6
#method 2
sumdiff2 <- function(n) {
	#(1/4)*(n^2)*(1+n)^2 - (1/6)*n*(1+n)*(1+2*n)
	(1/12)*(n)*(-2-3*n+2*n^2+3*n^3)
}  

# try sumdiff(10E6) vs sumdiff2(10E6)

# Problem 5
# Iterative Euclidean algorithm
gcd <- function(a,b) {
	t <- 0
	while (b != 0) {
		t <- b
		b <- a %% b
		a <- t
	}
	a
}

# lcm of two numbers
lcm <- function(a,b) {
	abs(a * (b/(gcd(a,b))))
}

lcm_ <- function(xs) {
	l <- 1
	for (i in 1:(length(xs))) {
		l <- lcm(l,xs[i])
	}
	l
}

# Or, using a reduce operation defined as follows:
reduce <- function(op,x,xs) {
	y <- x
	for (i in 1:(length(xs)-1)) {
		y <- do.call(op, list(y, xs[i]))
	} 
	y
}
# reduce(lcm, 1, c(1:10))


# Problem 7 (nth prime)
# Try a naive solution first
# Return first n primes
nprime <- function(n) {
	if (n == 1) {
		return (2)
	}
		
	psofar <- c()
	psofar[1] <- 2
	j <- 2
	p <- 1
	i <- 2
	while (p < n)  {
		if ( all((i %% psofar) > 0) ) {
			psofar[j] <- i
			j <- j + 1
			p <- p + 1 
		}
		i <- i + 1
	}
	psofar
}

# tail(psofar(10001),1)
# Return a list of all palindromic numbers
# generated as a product of 2 N-digit numbers
pal <- function(N) {
 palindromes <- c()
 
 min_no <- 1*10^(N-1)
 max_no <- sum(9*10^(seq(0,N-1)))
 
 n <- 1
 for (i in seq(max_no,min_no,-1)) {
  for (j in seq(i,min_no,-1)) {
   p <- i * j
   digits <- floor(log10(p))
   x <- seq(0, digits %/% 2)
    if (all( ((p %/% 10^x) %% 10)==((p %/% 10^(digits-x)) %% 10) )) {
     palindromes[n] <- p
     n <- n + 1
    }
  }
 }
 max(palindromes)
}

# Problem 8
gprod <- function() {
 # Read number as string
 snum <- scan(file="number.dat", what=character(0),
  strip.white=TRUE, quiet=TRUE)
 
 # Concatenate lines into a single line
 snum <- paste(snum, collapse="", sep="")
  
 mp <- 0
 for (i in 1:(nchar(snum)-4)) {
  s <- substr(snum, i, i+4)
  m <- prod(as.numeric(strsplit(s,"")[[1]]))
  
  if (m > mp) {
   mp <- m
}
 
 }
 mp
}

## Problem 13
problem13 <- function() {
    nums <- scan("problem13.dat")
    s <- sum(nums)
    s %/% 10^(floor(log10(s))-9)
}

## Problem 16
sumdigits <- function(n) {
 digits <- floor(log10(n))
 s <- 0
 for (i in 0:digits) {
  s<- s + ((n %/% 10^(digits-i)) %% 10)
 }
 s
}

# Problem 9
# Pythagorean Triple
ptriple <- function() {
 
 sum <- 0
 a <- 0; b <- 0; c <- 0;
 m <- 0
 
 for (m in 1:1000) {
  for (n in m:1000) {
  a <- n^2-m^2
  b <- 2*m*n
  c <- n^2 + m^2
  
  if (all(a^2 + b^2 == c^2, sum(a,b,c)==1000)) {
   return(prod(a,b,c))
  }
 }
 }
}

## Problem 16
sumdigits <- function(n) {
 digits <- floor(log10(n))
 s <- 0
 for (i in 0:digits) {
  s<- s + ((n %/% 10^(digits-i)) %% 10)
 }
 s
}
 
# Calculate the sum of digits in the decimal representation of 2^n
# Only works for smaller values of n
bsum <- function(n) {
 s <- 0
 e <- floor(log10(2^n))
 for (i in seq(e,0,-1)) {
  s <- s + (((2^n) %/% 10^i) %% 10)
 }
 s
} 
 
# Also doesnt seem to work
bsum2 <- function(n) { 
 s <- 0
 strn <- formatC(2^n, format="fg")
 sum(as.numeric(strsplit(strn,"")[[1]]))
}

# s<-system("echo '2^1000' | bc", intern=T)

# For problem 11, we need to import an arbitrary precision
# library (e.g. gmp), or use the arbitrary precision algorithm
problem11 <- function() {
}

problem11 <- function() {
    numbers <- scan("problem11.dat")
    m <- matrix(as.numeric(numbers), 20, byrow=TRUE)
    maxprd <- 0
    N <- 20; n <- 4
    prd1 <- 0; prd2 <- 0; prd3 <- 0
    dims <- dim(m)
    a <- (n-1)
    x <- c(0:a)
    for (i in 1:(dims[1])) {
        for (j in 1:(dims[2])) {
            prd1 <- ifelse(j <= N-a, prod(m[i,j+x]), 0) # row prod
            prd2 <- ifelse(i  <= N-a, prod(m[i+x,j]), 0) # column prod
            # lower right diagonal 
            prd3 <- ifelse(i <= N-a && j <= N-a, prod(diag(m[i:(i+a),j:(j+a)])),0)
            # lower left diagonal
            prd4 <- ifelse(i <= N-a && j > a, prod(diag(m[i:(i+a),j:(j-a)])), 0)
            maxprd <- max(prd1,prd2,prd3,prd4,maxprd)
        }
    }
    maxprd  
}

## Problem 14
# Collatz conjecture
problem14 <- function(N) {
	#collatz <- scan("collatz.dat", what=list(cn=0,cx=0))
	maxChain <- 0
	chains <- rep(0,N)
	x <- 1
	for (i in 1:N) {
		n <- i
		chain <- 0
		
		while(n > 1) {
			n <- ifelse(n %% 2 == 0, n/2, 3*n+1)
			chain <- chain + 1
			if (n < N && chains[n] > 0) {
			    chain <- chain + chains[n]
			 	break
			}
			
		}
		chains[i] <- chain
		
		if (chain > maxChain) {
			maxChain <- chain
			x <- i
		}
	}
	x
}

## Problem 25
# This overflows at around F_1477
problem25 <- function(N) {
	n <- 2
	fib1 <- log10(2)
	fib2 <- log10(3)
	fib <- 0
	
	while ( fib < N ) {
		fib <- floor(fib1 + fib2)
		fib2 <- fib1
		fib1 <- fib
		n <- n + 1
	} 
	print(paste("fib",fib))
	n
}

problem25_2 <- function(N) {
	phi <- (1+sqrt(5))/2
	
	f <- 1/sqrt(5)
	n <- 1
	fib <- 0
	
	while(fib < N) {
		fib <- floor(n*log10(phi)-log10(5)/2) + 1
		#print(paste(f*(phi^n),fib,n))
		n <- n + 1
	} 
	n-1
}


# Trial Division
tdiv <- function(n) {
 primes <- sieve(floor(sqrt(n)))
 factors <- c()
 i <- 1
 curr <- 0
 
 for (p in primes) {
  while (n %% p == 0) {
   curr <- curr + 1
   n <- n %/% p
  }
  factors[i] <- curr
  i <- i + 1
  curr <- 0
 }
 
 factors
}
 
## Problem 12
# Method 1
# This is a slow solution
problem12 <- function(N) {
 n <- 0 # current triangular number Tn
 i <- 5 # \sum_{i=1}^n{i} 
 
 while (TRUE) { 
  n <- (i*(i+1))/2
  factors <- tdiv(n) 
  print(n)
  if (prod(factors+1) >= N) {
   return(n)
  }
  i <- i + 1
 }
}

T <- function(n) {
	(n*(n+1))/2
}

# Problem 18
problem18 <- function() {
tree <- scan(file="problem18.dat", sep=" ", strip.white=TRUE)
 for (level in ceiling(-1+sqrt(1+8*length(dat))/2):2) {
	print(paste("===> level",level))
	for (node in T(level-1):(T(level-2)+1)) {
		print(paste("max(",tree[node+level-1],",",tree[node+level],")"))
		tree[node] <- tree[node] + max(tree[node+level-1], tree[node+level])
	}
 }
 tree[1]
}

