#if 0
#include <stdio.h>
int fibo(int x);
int main(void) {
	int n,result;
	scanf("%d", &n);
	result=fibo(n);
	printf("%d\n", result);
	return 0;
}
int fibo(int x) {
	if (x == 0) {
		return 0;
	}
	else if (x == 1) {
		return 1;
	}
	else {
		return fibo(x - 1) + fibo(x - 2);
	}
}
#endif