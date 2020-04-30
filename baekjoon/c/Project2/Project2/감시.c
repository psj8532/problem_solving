#if 1
#include <stdio.h>

void observe(int index, int s[][8], int cnt, int cL[][3]);
void cctvCheck(int y, int x, int num, int d, int mt[][8]);
int detect(int ny, int nx, int d, int mt[][8]);
int zCount(int c, int mt[][8]);

int temp_d1, temp_d2, temp_d3, count;
int temp[8][8] = { 0 };
int N, M;
int min = 9876543210;
int cctv[6] = {
		0,4,2,4,4.1
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

int main(void) {
	freopen("°¨½Ã.txt", "r", stdin);
	setbuf(stdout, NULL);

	int matrix[8][8] = {0};
	int top = -1;
	int cctvList[8][3] = { 0 };
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &matrix[i][j]);
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if ((matrix[i][j] >= 1) && (matrix[i][j] <= 5)) {
				top++;
				cctvList[top][0] = i;
				cctvList[top][1] = j;
				cctvList[top][2] = matrix[i][j];
				
			}
		}
	}

	observe(0, matrix, top+1, cctvList);
	printf("%d\n", min);

	return 0;
}

void observe(int index, int s[][8], int cnt, int cL[][3]) {
	if (index == cnt) {
		count = zCount(0, s);
		if (count < min) {
			 min = count;
		}
		return;
	}
	int idx = cctv[cL[index][2]];
	for (int i = 0; i < idx; i++) {
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				temp[r][c] = s[r][c];
			}
		}
		cctvCheck(cL[index][0], cL[index][1], cL[index][2], i, s);
		observe(index + 1, s, cnt, cL);
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				s[r][c] = temp[r][c];
			}
		}
	}
}
void cctvCheck(int y, int x, int num, int d, int mt[][8]) {
	if (num == 1) {
		mt = detect(y,x,d,mt);
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
		mt = detect(y, x, temp_d1, mt);
		mt = detect(y, x, temp_d2, mt);
	}
	else if (num == 4) {
		temp_d1 = d4[d][0];
		temp_d2 = d4[d][1];
		temp_d3 = d4[d][2];
		mt = detect(y, x, temp_d1, mt);
		mt = detect(y, x, temp_d2, mt);
		mt = detect(y, x, temp_d3, mt);
	}
	else {
		for (int idx = 0; idx < 4; idx++) {
			detect(y,x,idx,mt);
		}
	}
}
int detect(int ny, int nx, int d, int mt[][8]) {
	ny += direct[d][0];
	nx += direct[d][1];
	while (((ny >= 0) && (ny < N)) && ((nx >= 0) && (nx < M)) && (mt[ny][nx] != 6)) {
		if (mt[ny][nx] == 0) {
			mt[ny][nx] = -1;
		}
		ny += direct[d][0];
		nx += direct[d][1];
	}
	return mt[8][8];
}
int zCount(int c, int mt[][8]) {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (mt[i][j] == 0) {
				c++;
			}
		}
	}
	return c;
}
#endif