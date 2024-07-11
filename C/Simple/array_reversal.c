#include<stdio.h>

void arrayReversal(int arr[], int arr_size)
{
    int i,temp;
    for (i=0;i<arr_size/2;i++){
        temp = arr[i];
        arr[i] = arr[arr_size-i-1];
        arr[arr_size-i-1] = temp;
    }
}

void arrayPrint(int arr[])
{
    int i;
    for (i=0;i<7;i++){
        printf("Value of index %d is %d\n",i,arr[i]);
    }
}

void arrayPrint2(int arr[], int arr_size){
    printf("{");
    for (int i=0;i<arr_size;i++){
        printf("%d",arr[i]);
        if (i!=(arr_size-1)){
            printf(",");
        }
    }
    printf("}\n");
}

int main()
{
    int array[] = {5,64,57,78,34,654,54};
    int arr_size;
    printf("Array before reversal:- \n");
    if (sizeof(array)!=0){
        arr_size = sizeof(array)/sizeof(array[0]);
    }
    else{
        arr_size = 0;
    }
    arrayPrint2(array,arr_size);
    arrayReversal(array, arr_size);
    printf("Array after reversal:- \n");
    arrayPrint2(array,arr_size);
}