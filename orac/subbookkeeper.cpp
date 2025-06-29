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
 
 /* word is the word with one missing letter */
 char word[200005];
 
 int answer = 0;
 int main(void) {
     /* Read the value of N and the word. */
     scanf("%d", &N);
     scanf("%s", word);
 
     /*
      * TODO: This is where you should compute your solution. Store the largest
      * score that Rebecca can achieve into the variable answer.
      */
     
     for (int i = 0; i < N; ++i) {
        if (word[i] == '?') {
            if (i==(N-1)) {
                word[i] = word[i-1];
            } else {
                word[i] = word[i+1];
            }
        }

        if (i>0 &&(word[i] == word[i-1])) {
            answer++;
        }
     }
 
     /* Write the answer. */
     printf("%d\n", answer);
 
     return 0;
 }