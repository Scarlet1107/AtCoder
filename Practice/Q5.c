#include <stdio.h>

int main() {
    int n = 5;
    int r = 0;
    for(int i = 1; i <= n; i++) {
        for(int j = i; j <= n; j++) {
            for(int k = 1; k <= j; k++) {
                r += 1;
            }
        }
    }
    printf("%d \n", r);
}