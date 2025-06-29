/*
 * Solution Template for Javelin
 * 
 * Australian Informatics Olympiad 2024
 * 
 * This file is provided to assist with reading of input and writing of output
 * for the problem. You may modify this file however you wish, or
 * you may choose not to use this file at all.
 */

 #include <cstdio>

 /* N is the number of students. */
 int N;
 
 /*
  * D contains the distances. Note that the array starts from 0, and so the
  * values are D[0] to D[N-1].
  */
 int D[200005];
 
 int answer;

 int main(void) {
     /* Read the value of N and the distances. */
     scanf("%d", &N);
     for (int i = 0; i < N; i++) {
         scanf("%d", &D[i]);
     }
 
     /*
      * TODO: This is where you should compute your solution. Store the number
      * of current leaders that there were during the competition into the
      * variable answer.
      */
      answer = 1;
      int maxSoFar = D[0];
      for (int i = 1; i < N; ++i) {
        if (D[i] > maxSoFar) {
            answer++;
            maxSoFar = D[i];
        }
      }
  
     /* Write the answer. */
     printf("%d\n", answer);

     
     return 0;
 }