#if 0
#include <stdio.h>
int main(void) {
    int s[9];
    int maxval,maxidx;

    for (int i = 0; i < 9; i++) {
        scanf("%d", &s[i]);
    }
    maxval = s[0];
    maxidx = 1;
    for (int i = 1; i < 9; i++) {
        if (s[i] > maxval) {
            maxval = s[i];
            maxidx = i+1;
        }
    }
    printf("%d\n", maxval);
    printf("%d\n", maxidx);
    return 0;
 }
#endif