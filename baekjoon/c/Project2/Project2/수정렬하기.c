#if 1
#include <stdio.h>
int selection_sort(int s[], int n);
int main(void) {
	int i,n;
	int arr[1001];
	int result;
	int *p;
	p = arr;
	scanf("%d", &n);
	for (i = 0; i < n; i++) {
		scanf("%d", p + i);
	}
	result = selection_sort(p,n);
	for (i = 0; i < n; i++) {
		printf("%d\n", *(p+i));
	}
	return 0;
}
int selection_sort(int s[], int n) {
	int i, j,min,temp;
	for (i = 0; i < n - 1; i++) {
		min = s[i];
		for (j = i + 1; j < n; j++) {
			if (s[j] < min) {
				min = s[j];
				temp = s[i];
				s[i] = s[j];
				s[j] = temp;
			}
		}
	}
	return s;
}
#endif