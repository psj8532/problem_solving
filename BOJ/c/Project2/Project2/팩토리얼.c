#if 0
#include <stdio.h>
int factorial(int i);
int main(void) {
	int n,result;
	scanf("%d", &n);

	result = factorial(n);
	printf("%d\n", result);
	return 0;
}
int factorial(int x) {
	if (x == 0) {
		return 0;
	}
	if (x == 1) {
		return 1;
	}
	else {
		return x * factorial(x - 1);
	}
}
#endif