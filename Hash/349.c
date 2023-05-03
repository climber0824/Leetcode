/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    int *count1 = (int*)calloc(1001, sizeof(int));
    int *res = (int*)malloc(sizeof(int)*1000);
    int idx = 0;

    for (int i = 0; i < nums1Size; i++) {
        count1[nums1[i]] = 1;        
    }

    for (int i = 0; i < nums2Size; i++) {
        if (count1[nums2[i]] > 0) {            
            count1[nums2[i]] = 0;
            res[idx++] = nums2[i];            
        }
    }
    *returnSize = idx;
    return res;
}
