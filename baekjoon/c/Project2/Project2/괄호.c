#if 0
#include <stdio.h>

int main(void) {
	freopen("°ýÈ£.txt", "r", stdin);
	setbuf(stdout, NULL);
	char stack[50] = { 0 };
	char word[50];
	int top;
	int tc, j;
	int check;
	scanf("%d", &tc);
	for (int i = 0; i < tc; i++) {
		scanf("%s", word);
		top = -1;
		check = 1;
		j = 0;
		while(word[j]!=NULL){
			if (word[j]== '(') {
				top++;
				stack[top] = word[j];
			}
			else {
				if (top > -1) {
					stack[top] = 0;
					top--;
				}
				else {
					check = 0;
					break;
				}

			}
			j++;
		}
		if (top != -1) {
			check = 0;
		}
		if (check) {
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}
	return 0;
}
#endif