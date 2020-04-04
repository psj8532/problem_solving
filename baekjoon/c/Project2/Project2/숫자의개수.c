#if 1
#include <stdio.h>
//#define _CRT_SECURE_NO_WARNINGS
int main(void) {
	int a, b, c = 0;
	int sum_val = 0;
	char s[100];
	int num[10] = { 0 };
	int *p;
	int i;
	p = num;
	scanf("%d %d %d", &a, &b, &c);
	sum_val = a * b * c;
	printf("%d\n", sum_val);
	sprintf(s, "%d", num);
	printf("%s ", s);
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
		printf("%s", s);
	}

	return 0;
}
#endif