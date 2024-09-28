#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
    int i, j, k;
    int n;  // 入力される自然数の個数

    // ファイルから入力を読み取る
    FILE *file = fopen("Ex10Q2input.txt", "r");
    if (file == NULL) {
        printf("ファイルを開けませんでした\n");
        return 1;
    }

    fscanf(file, "%d", &n);

    int a[n];  // 入力される自然数

    for (i = 0; i < n; i++) {
        fscanf(file, "%d", &a[i]);
    }
    fclose(file);

    int b = 77 * n;  // 77の倍数を作るための最大値（全ての和が最大の場合）

    // dpテーブル: dp[i][j]はi番目の自然数を使ってjを作れるかどうか。作れる->1，作れない->0。
    int dp[n + 1][b + 1];

    // 初期化
    for (i = 0; i <= n; i++) {
        for (j = 0; j <= b; j++) {
            dp[i][j] = 0;
        }
    }

    dp[0][0] = 1;  // 0個の和で0は作れる

    for (i = 0; i < n; i++) {
        for (j = 0; j <= b; j++) {
            // i番目の自然数を使わずにjを作れるなら、i+1番目の自然数を考えてもjを作れる
            if (dp[i][j]) {
                dp[i + 1][j] = 1;
                // i番目の自然数を使う場合
                if (j + a[i] <= b) {
                    dp[i + 1][j + a[i]] = 1;
                }
            }
        }
    }

    int count = 0;

    // 77の倍数を数える
    for (j = 77; j <= b; j += 77) {
        if (dp[n][j]) {
            count++;
        }
    }

    printf("作成可能な77の倍数の個数: %d\n", count);

    return 0;
}
