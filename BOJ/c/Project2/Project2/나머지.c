#if 0
#include <stdio.h>
#define SIZE 10
#define temp 42
int main(void) {
	int i, num;
	int cnt = 0;
	int arr[temp] = { 0 };

	for (i = 0; i < SIZE;i++) {
		scanf("%d", &num);
		num %= temp;
		arr[num] += 1;
	}
	for (i = 0; i < temp; i++) {
		if (arr[i] > 0) {
			cnt += 1;
		}
	}
	printf("%d\n", cnt);
	return 0;
}
#endif