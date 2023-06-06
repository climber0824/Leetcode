// mergeSort
void merge(int arr[], int left[], int left_size, int right[], int right_size) {
    int i = 0, j = 0, k = 0;

    while (i < left_size && j < right_size) {
        if (left[i] <= right[j]) {
            arr[k] = left[i];
            i++;
        } else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    while (i < left_size) {
        arr[k] = left[i];
        i++;
        k++;
    }

    while (j < right_size) {
        arr[k] = right[j];
        j++;
        k++;
    }
}

// 合併排序遞迴函數
void mergeSort(int arr[], int size) {
    if (size <= 1) {
        return;
    }

    int mid = size / 2;
    int left[mid];
    int right[size - mid];

    // 分割陣列為兩個子陣列
    for (int i = 0; i < mid; i++) {
        left[i] = arr[i];
    }
    for (int i = mid; i < size; i++) {
        right[i - mid] = arr[i];
    }

    // 遞迴地對子陣列進行排序
    mergeSort(left, mid);
    mergeSort(right, size - mid);

    // 合併兩個已排序的子陣列
    merge(arr, left, mid, right, size - mid);
}

int comp(int *a, int *b) {
    return *a - *b;
}

// quickSort
// 交換兩個元素的值
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// 分割陣列並回傳分割點索引
int partition(int arr[], int low, int high) {
    int pivot = arr[high];  // 將最後一個元素設為基準點
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    
    swap(&arr[i+1], &arr[high]);
    
    return i + 1;
}

// 快速排序遞迴函數
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int partitionIdx = partition(arr, low, high);
        
        // 遞迴地對分割後的子陣列進行排序
        quickSort(arr, low, partitionIdx - 1);
        quickSort(arr, partitionIdx + 1, high);
    }
}


bool canMakeArithmeticProgression(int* arr, int arrSize){
    //mergeSort(arr, arrSize);
    //qsort(arr, arrSize, sizeof(int), comp);
    quickSort(arr, 0, arrSize - 1);
    int diff = arr[1] - arr[0];
    
    for (int i = 2; i < arrSize; i++) {
        if (arr[i] - arr[i-1] != diff) return false;
    }
    return true;
}
