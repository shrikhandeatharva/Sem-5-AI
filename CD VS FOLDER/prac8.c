#include <stdio.h>
void selectionSort(int arr[], int n) {
 int i, j, min_idx;
 for (i = 0; i < n - 1; i++) {
 min_idx = i;
 for (j = i + 1; j < n; j++) {
 if (arr[j] < arr[min_idx]) {
 min_idx = j;
 }
 }
 if (min_idx != i) {
 int temp = arr[i];
 arr[i] = arr[min_idx];
 arr[min_idx] = temp;
 }
 }
}
int main() {
 int arr[] = {61, 25, 13, 22, 15};
 int n = sizeof(arr) / sizeof(arr[0]);
 int i;
 printf("Original array: ");
 for (i = 0; i < n; i++) {
 printf("%d ", arr[i]);
 }
 printf("\n");
 selectionSort(arr, n);
 printf("Sorted array: ");
 for (i = 0; i < n; i++) {
 printf("%d ", arr[i]);
 }
 printf("\n");
 return 0;
} 