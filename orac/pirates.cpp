/*
 * Solution Template for Subbookkeeper
 * 
 * Australian Informatics Olympiad 2024
 * 
 * This file is provided to assist with reading of input and writing of output
 * for the problem. You may modify this file however you wish, or
 * you may choose not to use this file at all.
 */

#include <cstdio>
#include <cmath>
 /* N is the number of letters in the word. */

 int main(void) {
    int L = 0;
    int B = 0;
    int S = 0;

     /* Read the value of N and the word. */
    scanf("%d\n", &L);
    scanf("%d\n", &B);
    scanf("%d\n", &S);

    int d1 =  B + S;
    int d2  = (L-B) + (L-S);  
    
    int answer = (d1 < d2) ? d1 : d2;
    printf("%d\n", answer);    

    return 0;
 }