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

 int main(void) {
    int N = 0;
     /* Read the value of N and the word. */
     scanf("%d\n", &N);
      
     char* str = new char[N];
     for (int i = 0; i < N; ++i) {
        scanf("%c\n",&str[i]);
     }

     int zeroes = 0;
     int i = N;

     while (str[--i]=='0') 
        zeroes++;

     printf("%d\n", zeroes);
     return 0;
 }