#if 0
#include <stdio.h>
#include <string.h>
int main(void) {
	int i, n, num, temp;
	char op[7];
	int stack[10000] = {0};
	int top = -1;
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%s", op);
		if (strcmp(op,"push")==0) {
			scanf("%d", &num);
			top++;
			stack[top] = num;
		}
		else if (strcmp(op,"pop")==0) {
			if (top == -1) {
				printf("%d\n", top);
				continue;
			}
			temp = stack[top];
			top--;
			printf("%d\n", temp);
		}
		else if (strcmp(op,"size")==0) {
			printf("%d\n", top + 1);
		}
		else if (strcmp(op,"empty")==0) {
			if (top == -1) {
				printf("%d\n", 1);
			}
			else {
				printf("%d\n", 0);
			}
		}
		else {
			if (top == -1) {
				printf("%d\n", top);
				continue;
			}
			printf("%d\n", stack[top]);
		}
	}
	return 0;
}
#endif