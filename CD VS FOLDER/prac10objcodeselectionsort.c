#include <stdio.h>

void selectionSort(int arr[], int n) {
    int i, j, minIndex, temp;
    for (i = 0; i < n - 1; i++) {
        minIndex = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        // Swap the found minimum element with the first element
        temp = arr[minIndex];
        arr[minIndex] = arr[i];
        arr[i] = temp;
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    selectionSort(arr, n);
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}

// 1. start
// 2. MOV i,0
// 3. MOV j,0
// 4. loop outer
// 5. cmple n, i, imp loop
// 6. cmple n, j, imp (11)
// 7. MOV arr[j], t1
// 8. MOV t2, arr[mid_indx]
// 9. COMP t1, t2
// 10. MOV min_indx, j 
// 11. add j, 1
// 12. MOV j, t3
// 13. MOV t4, arr[j]
// 14. MOV t5, t2
// 15. MOVE t2, t4
// 16. MOV t4, t5, add j, 1
// 17. MOV t6, j 
// 18. MOV i, t6
// 19. MOV j, i 
// 20. loop end 
// 21. loop
// 22. imp loop

