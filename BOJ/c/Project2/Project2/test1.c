#if 0
#include <stdio.h>

int main(void) {
	FILE *fp;
	fp = fopen("test1.txt", "r");
	int a, b;

	fscanf(fp,"%d %d", &a, &b);
	printf("%d\n", a + b);

	fclose(fp);
	return 0;
}
#endif