#if 0
#include <stdio.h>

int main(void) {
	int i, n, op, num, temp;
	int stack[10000] = {0};
	int top = -1;
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%s", &op);
		if (op == "push") {
			scanf("%d", &num);
			top += 1;
			stack[top] = num;
		}
		else if (op == "pop") {
			if (top == -1) {
				printf("%d\n", top);
				continue;
			}
			temp = stack[top];
			top -= 1;
			printf("%d\n", temp);
		}
		else if (op == "size") {
			printf("%d\n", top + 1);
		}
		else if (op == "empty") {
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