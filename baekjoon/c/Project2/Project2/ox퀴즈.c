#if 0
#include <stdio.h>

int main(void) {
	int t,tc,i;
	int cnt,grade;
	scanf("%d", &tc);
	for (t = 0; t < tc; t++) {
		char sheet[81];
		int score[81] = { 0 };
		i = 0;
		while (1) {
			scanf("%c", &sheet[i]);
			if (sheet[i] == NULL) {
				break;
			}
			i++;
		}
		i = 0;
		cnt = 0;
		grade = 0;
		while (sheet[i] != NULL) {
			if (sheet[i] == 'O') {
				cnt += 1;
			}
			else {
				cnt = 0;
			}
			score[i] = cnt;
			i++;
		}
		for (i = 0; i < 81; i++) {
			grade += score[i];
		}
		printf("%d\n", grade);
	}
	return 0;
}
#endif