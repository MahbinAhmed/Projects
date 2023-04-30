#include <stdio.h>
#include <math.h>

void arrayPrint2(int arr[], int arr_size)
{
    printf("{");
    for (int i = 0; i < arr_size; i++)
    {
        printf("%d", arr[i]);
        if (i != (arr_size - 1))
        {
            printf(",");
        }
    }
    printf("}\n");
}

int ascendReverse(int array[], int arr_len)
{
    int temp;
    for (int j = 0; j < arr_len; j++)
    {
        for (int i = 0; i < arr_len; i++)
        {
            if (array[i] > array[i + 1])
            {
                temp = array[i + 1];
                array[i + 1] = array[i];
                array[i] = temp;
            }
        }
    }
}

int main()
{
    /*Question-1 | Word Done*/
    /*
    int test_cases;
    int x,d1,d2;
    scanf("%d",&test_cases);

    for(int i=0;i<test_cases;i++){
        scanf("%d %d %d", &x , &d1, &d2);
        int mul = x*d1;
        int result = (mul/d2)+((mul%d2)!=0);
        // int result2 = ceil(result);
        printf("%d", result);
        printf("\n");
    }
    */

    /*Question-3 | Lily Can Do It!*/
    /**/
    int array[] = {7, 19, 1, 12, 16, 21, 13};
    int arr_len = sizeof(array) / sizeof(array[0]);
    printf("%d\n",arr_len);
    ascendReverse(array, arr_len);
    arrayPrint2(array, arr_len);
}