#if 0
#include <stdio.h>

int main(void) {
	freopen("최소_최대.txt", "r", stdin);
	setbuf(stdout, NULL);
	int n;
	int min_val = 9876543210;
	int max_val = 0;
	int s[5];
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &s[i]);
	}
	for (int i = 0; i < n; i++) {
		if (s[i] > max_val) {
			max_val = s[i];
		}
		if (s[i]<min_val){
		min_val = s[i];
		}
	}
	printf("%d %d\n", min_val, max_val);
	return 0;
}
#endif