#if 0
#include <stdio.h>
#include <stdbool.h>

bool checkUp(int y, int *x, int l, int s[][100]);
int checkDown(int y, int *x, int v, int l, int s[][100], int N);

int main(void) {
	freopen("°æ»ç·Î.txt", "r", stdin);
	setbuf(stdout, NULL);

	int matrix[100][100] = { 0 };
	int matrix_rotate[100][100] = { 0 };
	int i, j, N, L, r, c, cnt,val;
	int road = 0;
	int *p;
	int *pc;
	p = matrix;
	pc = &c;

	scanf("%d %d", &N, &L);
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			scanf("%d", &matrix[i][j]);
		}
	}

	for (r = 0; r < N; r++) {
		c = cnt = 1;
		val = matrix[r][0];
		while (c != N) {
			if (matrix[r][c] == val) {
				cnt++;
			}
			else if (val - matrix[r][c] == -1 && N - 1) {
				if (cnt >= L && checkUp(r, c, L, p)) {
					c += 1;
					continue;
				}
				else {
					break;
				}
			}
			else if (val - matrix[r][c] == -1 && cnt >= L) {
				if (checkUp(r, c, L,p)) {
					cnt = 1;
					val = matrix[r][c];
				}
				else {
					break;
				}
			}
			else if (val - matrix[r][c] == 1) {
				printf("%d", c);
				c = checkDown(r, pc, matrix[r][c], L, p, N);
				printf("%d\n", c);
				if (c!=-1) {
					cnt = 0;
					val = matrix[r][c];
				}
				else {
					break;
				}
			}
			else {
				break;
			}
			c++;
		}
		if (c == N) {
			printf("%d right\n", r);
			road++;
		}
	}

	for (j = 0; j < N; j++) {
		for (i = 0; i < N; i++) {
			matrix_rotate[j][i] = matrix[i][j];
		}
	}
	for (i = 0; i < N; i++) {
		for (j = 0; j < N; j++) {
			matrix[i][j] = matrix_rotate[i][j];
		}
	}

	for (r = 0; r < N; r++) {
		c = cnt = 1;
		val = matrix[r][0];
		while (c != N) {
			if (matrix[r][c] == val) {
				cnt++;
			}
			else if (val - matrix[r][c] == -1 && N - 1) {
				if (cnt >= L && checkUp(r, c, L, p)) {
					c += 1;
					continue;
				}
				else {
					break;
				}
			}
			else if (val - matrix[r][c] == -1 && cnt >= L) {
				if (checkUp(r, c, L, p)) {
					cnt = 1;
					val = matrix[r][c];
				}
				else {
					break;
				}
			}
			else if (val - matrix[r][c] == 1) {
				c = checkDown(r, pc, matrix[r][c], L, p, N);
				if (c!=-1) {
					cnt = 0;
					val = matrix[r][c];
				}
				else {
					break;
				}
			}
			else {
				break;
			}
			c++;
		}
		if (c == N) {
			printf("%d down\n", r);
			road++;
		}
	}

	printf("%d", road);
	return 0;
}

bool checkUp(int y, int *x, int l, int s[][100]) {
	if (*x - l == 0)
		return true;
	else if (*x - l > 0 && s[y][*x - l - 1] <= s[y][*x - l])
		return true;
	return false;
}

int checkDown(int y, int *x, int v,int l,int s[][100], int N) {
	for (int j = x + 1; j < *x + l;j++) {
		if (*x + l <= N && s[y][j] == v) {
			continue;
		}
		else {
			return -1;
		}
	}
	if (*x + l == N){
		return N - 1;
	}
	else if (*x + l < N && s[y][*x + l - 1] >= s[y][*x + l]) {
		return x + l - 1;
	}
	else {
		return -1;
	}
}
#endif