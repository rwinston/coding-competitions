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

 /* N is the number of letters in the word. */
int N;
int K; 

 int main(void) {
     /* Read the value of N and the word. */
     scanf("%d %d\n", &N, &K);
     

     int caught = 0;
     int i = 0;
     while (++i<=N) {
        i += K;
        caught++;
     }
     
     printf("%d\n",(N-caught));
     return 0;
 }