// #include <stdio.h>
// void selectionSort(int arr[], int n) {
//  int i, j, min_idx;
//  for (i = 0; i < n - 1; i++) {
//  min_idx = i;
//  for (j = i + 1; j < n; j++) {
//  if (arr[j] < arr[min_idx]) {
//  min_idx = j;
//  }
//  }
//  if (min_idx != i) {
//  int temp = arr[i];
//  arr[i] = arr[min_idx];
//  arr[min_idx] = temp;
//  }
//  }
// }
// int main() {
//  int arr[] = {61, 25, 13, 22, 15};
//  int n = sizeof(arr) / sizeof(arr[0]);
//  int i;
//  printf("Original array: ");
//  for (i = 0; i < n; i++) {
//  printf("%d ", arr[i]);
//  }
//  printf("\n");
//  selectionSort(arr, n);
//  printf("Sorted array: ");
//  for (i = 0; i < n; i++) {
//  printf("%d ", arr[i]);
//  }
//  printf("\n");
//  return 0;
// } 

#include <stdio.h>

void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

void selectionSort(int arr[], int n) {
    int temp = 0;
    int i, j, min_idx;
    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        if (i != min_idx) {
            swap(&arr[i], &arr[min_idx]);
        }
    }
}

int main() {
    int arr[] = {29, 10, 14, 37, 13};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("// Selection Sort Three-Address Code\n\n");
    printf("temp = 0;\n");
    printf("i = 0;\n");
    printf("L1: if (i >= %d) goto L6;\n", n);
    printf("min_idx = i;\n");
    printf("j = i + 1;\n");
    
    int temp = 0;
    int i = 0;
    int min_idx = 0;
    int j = 0;
    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            printf("t1 = arr[%d];\n", j);
            printf("t2 = arr[%d];\n", min_idx);
            printf("if (t1 >= t2) goto L3;\n");
            printf("min_idx = %d;\n", j);
            printf("L3: j = %d + 1;\n", j);
        }
        if (i != min_idx) {
            printf("t3 = arr[%d];\n", i);
            printf("t4 = arr[%d];\n", min_idx);
            printf("if (t3 == t4) goto L5;\n");
            printf("t5 = arr[%d];\n", i);
            printf("arr[%d] = arr[%d];\n", i, min_idx);
            printf("arr[%d] = t5;\n", min_idx);
            printf("L5: i = %d + 1;\n", i);
        }
        printf("goto L1;\n");
    }

    printf("L6: end;\n");

    return 0;
}