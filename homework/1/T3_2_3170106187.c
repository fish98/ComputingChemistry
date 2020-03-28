#include <stdio.h>
#include <math.h>

int main(){

//
// Calculate quadratic equation solutions  
// x^2 + (-10^t - 1)x + 10^t = 0 
//

    int t;
    double a, b, c, x1, x2;
    printf("Enter t\n");
    scanf("%d", &t);
	a = 1.0;
	b = pow(-10, t) - 1;
	c = pow(10, t);

	x1 = (-1 * b + sqrt(b * b - 4 * a * c)) / 2 / a;
	x2 = (-1 * b - sqrt(b * b - 4 * a * c)) / 2 / a;

//
// Note 
// Surprisingly found x2 equals 0 only when t is above 17 but not 11 in C
//

	printf("Solution x1 = %f\n" , x1);
	printf("Solution x2 = %f\n" , x2);

}

//
// Arthor: Jiongchi Yu
// Date: 2020.3.28
//

