#if 0
#include <stdio.h>

int main(void) {
	freopen("최소_최대.txt", "r", stdin);
	setbuf(stdout, NULL);
	int n;
	int min_val;
	int max_val;;
	int s[1000000];
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &s[i]);
	}
	max_val = s[0];
	min_val = s[0];
	for (int i = 1; i < n; i++) {
		if (s[i] > max_val) {
			max_val = s[i];
		}
		else if (s[i] < min_val) {
			min_val = s[i];
		}
		else {
			continue;
		}
	}
	printf("%d %d\n", min_val, max_val);
	return 0;
}
#endif