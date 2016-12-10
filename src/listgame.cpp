#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	unsigned long long X = 0;
	scanf("%llu", &X);

	unsigned int prime_factors = 0;
	unsigned long long divisor = 3;

	unsigned long long Xsqrt = ceil(sqrt(X));

	while (!(X % 2))
	{
		X /= 2;
		prime_factors++;
		//printf("2 ");
	}
	
	while ((X>1) && !(!prime_factors && divisor > Xsqrt))
	{
		while (!(X % divisor))
		{
			X /= divisor;
			//printf("%llu ", divisor);
			prime_factors++;
		}
		divisor++;
		divisor++;
	}

	if (!prime_factors) 
		prime_factors=1;

	printf("%u\n", prime_factors);
	
	return(0);
}