#include <stdio.h>
#include <stdlib.h>

#define NEW_LINE 10 // LF in ASCII


int main () {
   double matrix [3][3];
   double result [3][3] = {{0,0,0},{0,0,0},{0,0,0}};;
   int i, j, k;
   FILE * fp;
   char line[128];
   char *ptr;
   double number;

   fp = fopen ("matrix_data.dat", "r");
   
   // Read matrix from file
   for (i = 0; i < 3; i++) {
	   for (j = 0; j < 3; j++){
		   fgets(line, sizeof line, fp);
		   number = strtod(line, &ptr);
		   if(*ptr != NEW_LINE) {
				printf("Invalid number: %s\n", line);
				printf("Please introduce only numbers\n");
				exit(0);
			}
		   matrix[i][j] = number;
	   }
   }
   
   // Print initial matrix
   printf("Initial Matrix:\n");
   for (i = 0; i < 3; i++) {
	   for (j = 0; j < 3; j++){
		   printf("%g \n", matrix[i][j]);
	   }
   }
   
   // Multiply matrix
   for (i = 0; i < 3; i++) {
	   for (j = 0; j < 3; j++){
		   for (k = 0; k < 3; k++) {
				result[i][j] +=  matrix[i][k] * matrix[k][j];
		   }
	   }
   }
   
   // Print result matrix
   printf("\nResult Matrix:\n");
	for (i = 0; i < 3; i++) {
	   for (j = 0; j < 3; j++){
		   printf("%g \n", result[i][j]);
	   }
   }

   fclose(fp);
   
   return(0);
}
