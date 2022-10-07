#include <stdio.h>
#include <conio.h>

int main()
{
    // int a=34;
    // int *ptra = &a;

    // printf("%d\n", ptra);
    // printf("%d\n", ptra+1);
    // printf("%d",sizeof(ptra));
    
    // char a = '3';
    // char *ptra = &a;
    // printf("%d\n", ptra);
    // ptra++;
    // printf("%d\n", ptra);
    // printf("%d\n", ptra-2);
    // printf("%d\n",sizeof(a));
    
    int arr[] = {1,2,3,4,5,6,7,8,9};
    printf("The value at position 3 of the array is %d\n", arr[3]);

    printf("address of first element in array %d\n", &arr[0]);//same
    printf("address of first element in array %d\n", arr);//same
    printf("address of second element in array %d\n", &arr[1]);//address of second place 
    printf("address of second element in array %d\n", arr + 1);// "  "  "  

    printf("Value at address of first element of the array is %d\n", *(&arr[0]));
    printf("Value at address of first element of the array is %d\n", arr[0]);//remove * and &
    printf("Value at address of first element of the array is %d\n", *(arr));
    printf("Value at address of second element in array %d\n", *(&arr[1])); 
    printf("Value at address of second element in array %d\n", arr[1]); 
    printf("Value at address of second element in array %d\n", *(arr + 1));  
    
    return 0;
}