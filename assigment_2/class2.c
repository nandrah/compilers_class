#include <example.h>
#include "folder/preprocessor.h"
// Literally does_not_exists.h does not exists
// What will the preprocessor does in this case?
#include "does_not_exists.h" 


#define PI 3.1416

int main(){
    
#if PI==3.1417
    printf("This is the value of PI %f", PI);
#else
	printf("Hello World!");
#endif	
	return 0

}

#undef PI
int not_main(){
    printf("This is the value of PI %f", PI);

}

// This is a syntax error, how the preprocessor will handle this scenario?
#include "error.h 

