// array reversal exercise

#include<stdio.h>

// void arrayrev(int arr[])
// {
//     printf("Before reversing the array: \n");
//     for (int i = 0; i < 6; i++)
//     {
//         printf("%d\t",arr[i]);
//     }
//     printf("\nAfter reversing the array: \n");
//     for (int i = 5; i >= 0; i--)
//     {
//         printf("%d\t",arr[i]);
//     } 
// }
// int main()
// {
//     int arr[] = {1,2,3,4,5,6};
//     arrayrev(arr);
//     return 0;
// }

void arrayrev(int arr[])
{
    int temp;
    //swap item i with item 6-i means when i=0 the first element will be swapped with (6-i)=6-0=6th element that is last element.4
    for (int i = 0; i < 7/2; i++)
    {
        temp = arr[i];
        arr[i] = arr[6-i];
        arr[6-i] = temp; 
    }   
}
int main()
{
    int arr[] = {1,2,3,4,5,6,7},n;
    
    // n = sizeof(arr)/sizeof(arr[0]);
    printf("Before reversing the array: \n");
    for ( int i = 0; i < 7; i++)
    {
        printf("The value  of element %d is %d\n",i,arr[i]);
    }
    arrayrev(arr);
    printf("After reversing the array: \n");
    for ( int i = 0; i < 7; i++)
    {
        printf("The value  of element %d is %d\n",i,arr[i]);
    }
}