#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);

	int N = 0, M = 0;

	while (1)
	{
		// break if no more test cases
		scanf("%d %d", &N, &M);
		if ((N == 0) && (M == 0))
			break;

		//printf("%d %d", N, M);

		// allocate memory to store the cd collections
		int* jack_collection = new int[N];
		int* jill_collection = new int[M];

		// populate the cd collection arrays
		for (int i = 0; i < N; i++)
			scanf("%d", &jack_collection[i]);
		for (int i = 0; i < M; i++)
			scanf("%d", &jill_collection[i]);

		// count the number that are the same
		int both = 0, i = 0, e = 0;
		//printf("\t%d %d \t%d %d", i,N,e,M);
		while ((i < N) && (e < M))
		{
			if (jack_collection[i] == jill_collection[e])
			{
				both++;
				i++;
				e++;
			}
			else if (jack_collection[i] > jill_collection[e])
				e++;
			else
				i++;
		}
		printf("%d\n", both);

		// free the memory storing the cd collections
		delete[] jack_collection;
		delete[] jill_collection;
	}

	return(0);
}