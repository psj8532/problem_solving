#if 0
#include <stdio.h>

int main(void) {
	int i, n,max;
	int grade[1001];
	double result=0.0;
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d", &grade[i]);
	}
	max = 0;
	for (i = 0; i < n; i++) {
		if (grade[i] > max) {
			max = grade[i];
		}
	}
	for (i = 0; i < n; i++) {
		result =result + (double)grade[i] / (double)max * 100;
	}
	result /= (double)n;
	printf("%lf\n", result);
	return 0;
}
#endif