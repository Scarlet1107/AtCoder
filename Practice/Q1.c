#include <stdio.h>

int main() {
    int n = 4;
    int r = 0;
    for(int i = 1; i <= n; i++) {
        for(int j = i; j <= n; j++) {
            r += 1;
        }
    }
    printf("%d \n", r);
}