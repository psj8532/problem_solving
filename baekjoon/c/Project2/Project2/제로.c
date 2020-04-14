#if 0
#include <stdio.h>

int main(void) {
	int stack[100000];
	int top = -1;
	int i,k,num;
	int sum = 0;

	scanf("%d", &k);
	for (i = 0; i < k; i++) {
		scanf("%d", &num);
		if (num != 0) {
			top++;
			stack[top] = num;
			sum += num;
		}
		else {
			sum -= stack[top];
			stack[top] = 0;
			top--;
		}
	}
	printf("%d\n", sum);

	return 0;
}
#endif