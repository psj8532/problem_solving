#if 0
#include <stdio.h>

int main(void) {
    freopen("A+B-4.txt", "r", stdin);
    setbuf(stdout, NULL);
    int a, b;
    while ((scanf("%d %d", &a, &b)) != EOF) {
        printf("%d\n", a + b);
    }
    return 0;
}
#endif