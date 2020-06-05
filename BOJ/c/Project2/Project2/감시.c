#if 1
#include <stdio.h>

void observe(int index);
void cctvCheck(int y, int x, int num, int d);
void detect(int ny, int nx, int d);
int zCount(int c);

int temp_d1, temp_d2, temp_d3, count;
int temp[8][8] = { 0 };
int N, M;
int cnt = 0;
int min = 9876543210;
int cctv[6] = {
		0,4,2,4,4,1
};
int direct[4][2] = {
	{-1,0},
	{0,1},
	{1,0},
	{0,-1}
};
int d2[2][2] = {
	{0,2},
	{1,3}
};
int d3[4][2] = {
	{0,1},
	{1,2},
	{2,3},
	{3,0}
};
int d4[4][3] = {
	{0,1,2},
	{1,2,3},
	{2,3,0},
	{3,0,1},
};
int matrix[8][8] = { 0 };
int cctvList[8][3] = { 0 };


int main(void) {
	freopen("°¨½Ã.txt", "r", stdin);
	setbuf(stdout, NULL);

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &matrix[i][j]);
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if ((matrix[i][j] >= 1) && (matrix[i][j] <= 5)) {
				cctvList[cnt][0] = i;
				cctvList[cnt][1] = j;
				cctvList[cnt][2] = matrix[i][j];
				cnt++;
			}
		}
	}

	observe(0);
	printf("%d\n", min);

	return 0;
}

void observe(int index) {
	if (index == cnt) {
		count = zCount(0);
		if (count < min) {
			 min = count;
		}
		printf("%d\n", count);
		return;
	}
	int idx = cctv[cctvList[index][2]];
	for (int i = 0; i < idx; i++) {
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				temp[r][c] = matrix[r][c];
			}
		}
		cctvCheck(cctvList[index][0], cctvList[index][1], cctvList[index][2], i);
		observe(index + 1);
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				matrix[r][c] = temp[r][c];
			}
		}
	}
}
void cctvCheck(int y, int x, int num, int d) {
	if (num == 1) {
		detect(y,x,d);
	}
	else if ((num == 2) || (num == 3)) {
		if (num == 2) {
			temp_d1 = d2[d][0];
			temp_d2 = d2[d][1];
		}
		else {
			temp_d1 = d3[d][0];
			temp_d2 = d3[d][1];
		}
		detect(y, x, temp_d1);
		detect(y, x, temp_d2);
	}
	else if (num == 4) {
		temp_d1 = d4[d][0];
		temp_d2 = d4[d][1];
		temp_d3 = d4[d][2];
		detect(y, x, temp_d1);
		detect(y, x, temp_d2);
		detect(y, x, temp_d3);
	}
	else {
		for (int idx = 0; idx < 4; idx++) {
			detect(y,x,idx);
		}
	}
}
void detect(int ny, int nx, int d) {
	ny += direct[d][0];
	nx += direct[d][1];
	while (((ny >= 0) && (ny < N)) && ((nx >= 0) && (nx < M)) && (matrix[ny][nx] != 6)) {
		if (matrix[ny][nx] == 0) {
			matrix[ny][nx] = -1;
		}
		ny += direct[d][0];
		nx += direct[d][1];
	}
}
int zCount(int c) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (matrix[i][j] == 0) {
				c++;
			}
		}
	}
	return c;
}
#endif