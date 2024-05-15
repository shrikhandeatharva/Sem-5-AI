#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 100

void constantFolding(char code[][MAX_LINE_LENGTH], int n, char optimizedCode[][MAX_LINE_LENGTH]) {
    for (int i = 0; i < n; i++) {
        char *line = code[i];
        char *delim = " ";
        char *token = strtok(line, delim);
        char optimizedLine[MAX_LINE_LENGTH] = "";

        while (token != NULL) {
            if (strchr("+-*/^", token[0]) != NULL && strlen(token) == 1) {
                char *op1 = strtok(NULL, delim);
                char *op2 = strtok(NULL, delim);
                int val1 = atoi(op1);
                int val2 = atoi(op2);

                int result;
                switch (token[0]) {
                    case '+':
                        result = val1 + val2;
                        break;
                    case '-':
                        result = val1 - val2;
                        break;
                    case '*':
                        result = val1 * val2;
                        break;
                    case '/':
                        result = val1 / val2;
                        break;
                    case '^':
                        result = 1;
                        break;
                }
                char temp[MAX_LINE_LENGTH];
                sprintf(temp, "%d", result);
                strcat(optimizedLine, temp);
                strcat(optimizedLine, " ");
                strcat(optimizedLine, token);
                strcat(optimizedLine, " ");
            } else {
                strcat(optimizedLine, token);
                strcat(optimizedLine, " ");
            }
            token = strtok(NULL, delim);
        }
        strcpy(optimizedCode[i], optimizedLine);
    }
}
int main() {
    char code[][MAX_LINE_LENGTH] = {
        "temp = 0",
        "i = 0",
        "L1: if i >= n goto L6",
        "min_idx = i",
        "j = i + 1",
        "L2: if j >= n goto L4",
        "t1 = arr[j]",
        "t2 = arr[min_idx]",
        "if t1 >= t2 goto L3",
        "min_idx = j",
        "L3: j = j + 1",
        "goto L2",
        "L4: t3 = arr[i]",
        "t4 = arr[min_idx]",
        "if t3 == t4 goto L5",
        "t5 = arr[i]",
        "arr[i] = arr[min_idx]",
        "arr[min_idx] = t5",
        "L5: i = i + 1",
        "goto L1",
        "L6: end"
    };
    int n = sizeof(code) / sizeof(code[0]);
    char optimizedCode[n][MAX_LINE_LENGTH];
    constantFolding(code, n, optimizedCode);
    printf("\nOptimized 3-address code:\n");
    for (int i = 0; i < n; i++) {
        printf("%s\n", optimizedCode[i]);
    }
    return 0;
}