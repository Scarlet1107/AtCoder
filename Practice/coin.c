#include <stdio.h>
#include <stdlib.h>

#define INFTY 99999

int min(int a, int b) {
    if (a < b) {
        return a;
    } else {
        return b;
    }
}

int main(int argc, char const *argv[]) {
    int i, j;
    int n;        // 硬貨の種類
    int payment;  // 支払い金額

    // ファイルから入力を読み取る
    FILE *file = fopen("Ex10Q1input.txt", "r");
    if (file == NULL) {
        printf("ファイルを開けませんでした\n");
        return 1;
    }

    fscanf(file, "%d", &n);
    int coin[n];  // 硬貨の額面
    for (i = 0; i < n; i++) {
        fscanf(file, "%d", &coin[i]);
    }

    fscanf(file, "%d", &payment);
    fclose(file);

    // dpテーブルとコインのトレーステーブル
    int dp[payment + 1];  // jセント支払うためにdp[j]枚の硬貨が必要
    int trace[payment + 1]; // jセント支払うために最後に使った硬貨のインデックス

    // 初期化
    for (i = 0; i <= payment; i++) {
        dp[i] = INFTY;
        trace[i] = -1;
    }

    dp[0] = 0;  // 0セントを払うために必要な枚数は0

    // 全ての硬貨について
    for (i = 0; i < n; i++) {
        // 支払金額がjセントのときに, coin[i]セントで払う
        for (j = coin[i]; j <= payment; j++) {
            if (dp[j - coin[i]] + 1 < dp[j]) {
                dp[j] = dp[j - coin[i]] + 1;
                trace[j] = i;  // 最後に使った硬貨のインデックスを記録
            }
        }
    }

    // 結果を表示
    if (dp[payment] == INFTY) {
        printf("支払いは不可能です\n");
    } else {
        printf("必要な最小硬貨枚数: %d\n", dp[payment]);
        printf("使用した硬貨:\n");
        int amount = payment;
        int count[n];
        for (i = 0; i < n; i++) {
            count[i] = 0;
        }

        while (amount > 0) {
            int coin_index = trace[amount];
            count[coin_index]++;
            amount -= coin[coin_index];
        }

        for (i = 0; i < n; i++) {
            if (count[i] > 0) {
                printf("%dセントの硬貨: %d枚\n", coin[i], count[i]);
            }
        }
    }

    return 0;
}
