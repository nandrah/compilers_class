#include <stdio.h>
#include <stdlib.h>


int main () {
   float matrix [3][3];
   float result [3][3] = {{0,0,0},{0,0,0},{0,0,0}};;
   int i, j, k;
   FILE * fp;

   fp = fopen ("matrix_data.dat", "r");
   
   // Read matrix from file
   for (i = 0; i < 3; i++) {
	   for (j = 0; j < 3; j++){
		   fscanf(fp, "%g", &matrix[i][j]);
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
	for (i = 0; i < 3; i++) {
	   for (j = 0; j < 3; j++){
		   printf("%g \n", result[i][j]);
	   }
   }

   fclose(fp);
   
   return(0);
}
