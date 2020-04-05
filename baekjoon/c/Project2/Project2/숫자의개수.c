#if 0
#include <stdio.h>
int main(void) {
	int a, b, c = 0;
	int val = 0;
	char s[100];
	int num[10] = { 0 };
	int* p;
	int i;
	p = num;
	scanf("%d %d %d", &a, &b, &c);
	val = a * b * c;
	sprintf(s, "%d", val);
	for (i = 0; i < 100; i++) {
		if (s[i] == NULL) {
			break;
		}
		else {
			if (s[i] == '0') {
				p[0] += 1;
			}
			else if (s[i] == '1') {
				p[1] += 1;
			}
			else if (s[i] == '2') {
				p[2] += 1;
			}
			else if (s[i] == '3') {
				p[3] += 1;
			}
			else if (s[i] == '4') {
				p[4] += 1;
			}
			else if (s[i] == '5') {
				p[5] += 1;
			}
			else if (s[i] == '6') {
				p[6] += 1;
			}
			else if (s[i] == '7') {
				p[7] += 1;
			}
			else if (s[i] == '8') {
				p[8] += 1;
			}
			else if (s[i] == '9') {
				p[9] += 1;
			}
			else {
				continue;
			}
		}
	}
	for (i = 0; i < 10; i++) {
		printf("%d\n", p[i]);
	}

	return 0;
}
#endif