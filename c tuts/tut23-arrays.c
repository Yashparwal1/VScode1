/*
* An array is a collection of data items of the same type.
* Items are stored at contigeous memory location.
* It can also store the collection of derived data types, such as pointers, structures etc.
* A one-demensional array is like a list.
* A two-dimentional array is like a table.
* The C lang. places no limits on the number of dimensions in an array.
* Some texts refer to one-dimensional arrays as vectors, two-dimensional array as matrices, and use the general terms arrays when the number of dimensions is unspecified or unimportant

=> Why do we need array:
* Code that has array is sometimes more organised and redable.
* If you were to store the marks in a test of 56 student, creating 56 vars. will make program messy.
* Solution to this is array.
* We can create arrays of integers and store the consecutive marks corrosponding to the roll no. in the array.

=> ADVANTSGES OF ARRAY:
1. It is used to represent multiple data itmes of same type by using only single name.
2. Accessing an item in an array is very fast.
3. 2-dimensional array makes it easy in mathematical applications as it is used to represent matrices.

=> PROPERTIES OF ARRAY:
1. Data in an array is stored in contiguous memory locations.
2. Each element of an array is of same size.
3. Any element of the array with given index can be accessed very quickly by using its address which can be calculated using the base address and the index.

=> SYNTAX for declaring arrays:
* datatype name[size];
* datatype name[size] = {x,y,z,....}; //size not req. in this case.
* datatype name[rows][columns]; //for 2-D arrays
* We can also initialize array one-by-one by accessing it using its index:
    * name[0] = 0;

=> DISADVANTAGES OF ARRAY:
1. Poor time complexity of insertion and deletion operation.
2. Wastage of mmory since arrays are fixed in size.
3. If there is enough space present in the memory but not in contiguous form, you will not be able to initialize your array.
4. It is not possible to increase the size of an array once you have declared the array.

*/

#include <stdio.h>
#include <conio.h>

// int main()
// {
// int marks[4] = {224, 3, 45, 8999}; //declaration with initialisation
// int marks[2][4] = {{224, 3, 45, 8999},{10,20,30,40}};
/* matrix representation like this 👇
       column 👇
row 👉10 01 02 03
       10 11 12 13
 */
// marks[0] = 20;

// for (int i = 0; i < 4; i++)
// {
//     printf("Enter the value of %d element of the array: ", i);
//     scanf("%d\n", &marks[i]); //we are asking the values here, means inicialising here

// }
// for (int i = 0; i < 4; i++)
// {
//     printf("The value of %d element of the array is %d\n", i,marks[i]);
// }

// for (int i = 0; i < 2; i++)
// {
//     for (int j = 0; j < 4; j++)
//     {
//         // printf("The value pf %d, %d element of the array is %d\n",i,j,marks[i][j]);
//         // to print the elements in matrix form 👇
//         printf("%d ",marks[i][j]);
//     }
//     printf("\n");
// }

// //we can initialise values like this also i.e. one by one for each location
// printf("Marks of student 1 is %d\n",marks[0]);
// marks[0] = 30; //we can change the value stored in [0]
// marks[1] = 40;
// marks[2] = 50;
// marks[3] = 60;
// printf("Marks of student 1 is %d",marks[0]);

//     return 0;
// }

// QUESTION - WAP to search an element of the array

// int main()
// {
//     int i,n,A[10],beg,end,mid;
//     for(i = 0; i < 10; i++)
//     {
//         printf("Enter the elements in increasing order: ");
//         scanf("%d",&A[i]);
//     }
//     printf("Elements in A[10] are: \n");
//     for (int i = 0; i < 10; i++)
//     {
//         printf("%d, ",A[i]);
//     }

//     printf("\nEnter the no. you want to search: ");
//     scanf("%d",&n);

//     beg=0;
//     end=9;
//     mid=(beg+end)/2;
//     printf("middle element is: %d",mid);

//     while (beg <= end && A[mid] != n)
//     {
//         if (A[mid] < n) //then search on right side
//         {
//             beg = mid + 1;
//         }
//         else             //then search on left side
//         {
//             end = mid - 1;
//         }
//         mid = (beg + end)/2;
//     }
//     if (n == A[mid])
//     {
//         printf("No. found : %d",n);
//     }
//     else
//     {
//         printf("no. not found");
//     }

//     return 0;
// }

// QUESTION -- TO read to number of values in an array and display it in reverse order.

// int main()
// {
//     int i, A[5];
//     for (int i = 0; i < 5; i++)
//     {
//         printf("Enter the numbers in array: ");
//         scanf("%d",&A[i]);
//     }
//     printf("The elements of array A[5] are: \n");
//     for (int i = 0; i < 5; i++)
//     {
//         printf("%d ",A[i]);
//     }
//     printf("\nThe reversed elements of array A[5] are: \n");
//     for (int i = 4; i >= 0; i--)
//     {
//         printf("%d ",A[i]);
//     }

//     return 0;

// }

// QUESTION -- to copy the elements of one array into another array.

// int main()
// {
//     int i, n, arr1[100], arr2[50];
//     printf("How much elements you want to store in the Array: ");
//     scanf("%d", &n);
//     for (int i = 0; i < n; i++)
//     {
//         printf("Enter the elements of array: ");
//         scanf("%d", &arr1[i]);
//     }
//     printf("The elements of arr1[] are: \n");
//     for (int i = 0; i < n; i++)
//     {
//         printf("%d ", arr1[i]);
//     }
//     for (int i = 0; i < n; i++)
//     {
//         arr2[i] = arr1[i];
//     }
//     printf("\nThe elements of arr2[] are: \n");
//     for (int i = 0; i < n; i++)
//     {
//         printf("%d ", arr2[i]);
//     }

//     return 0;
// }

// QUESTION -- WAP TO FIND THE NO OF DUPLICATE ELEMENTS IN AN ARRAY

// int main()
// {
//     int i,j,t=0,arr1[100] = {2,2,6,8,8}, arr2[100], arr3[100], duplicate=0,final=0;
//     for(int i = 0; i < 5; i++)
//     {
//         printf("%5d ",arr1[i]);
//     }
//     {
//     for (int i = 0; i < 5; i++)
//         t = t + 1;
//     }
//     printf("\nTotal elements in array are: %d",t);
//     /* Copy the elements into another array */
//     for (int i = 0; i < 5; i++)
//     {
//         arr2[i] = arr1[i];
//         arr3[i] = 0;
//     }
//     /* ------- marks the elements as duplicate */
//     for (int i = 0; i < 5; i++)
//     {
//         for (int j = 0; j < 5; j++)
//         {
//             if (arr1[i] == arr2[j])
//             {
//                 arr3[j] = duplicate;
//                 duplicate++;
//             }
//         }
//         duplicate = 0;
//     }
//     for (int i = 0; i < 5; i++)
//     {
//         if (arr3[i] == 1)
//         {
//             final++;
//         }

//     }
//     printf("\nThe total no. of duplicate elements are: %d",final);

//     return 0;
// }

// QUESTION -- WAP TO ADD TWO 3x3 MATRICES

// int main()
// {
//     int i, j, A[3][3], B[3][3], C[3][3], ld=0, rd=0;
//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
//             printf("Enter the elements in A : ");
//             scanf("%d", &A[i][j]);
//         }
//     }
// printf("\n");
// for (int i = 0; i < 3; i++)
// {
//     for (int j = 0; j < 3; j++)
//     {
//         printf("Enter the elements in B : ");
//         scanf("%d", &B[i][j]);
//     }
// }

// display the matrix if you want
// Now addition of 2 matrix
// for (int i = 0; i < 3; i++)
// {
//     for (int j = 0; j < 3; j++)
//     {
//         C[i][j] = A[i][j] + B[i][j];
//     }
// }
// printf("the sum is = \n");
// for (int i = 0; i < 3; i++)
// {
//     for (int j = 0; j < 3; j++)
//     {
//         printf("%5d", C[i][j]);
//     }
//     printf("\n");
// }

// now transpose of a matrix
// for (int i = 0; i < 3; i++)
// {
//     for (int j = 0; j < 3; j++)
//     {
//         B[i][j] = A[j][i];
//     }
// }
// printf("The transpose of A = \n");
// for (int i = 0; i < 3; i++)
// {
//     for (int j = 0; j < 3; j++)
//     {
//         printf("%5d", B[i][j]);
//     }
//     printf("\n");
// }

// now sum of elements of left diagonal and sum of elements of right diagonal

//     for (int i = 0; i < 3; i++)
//     {
//         for (int j = 0; j < 3; j++)
//         {
//             printf("%5d", A[i][j]);
//         }
//         printf("\n");
//     }
//     for (int i = 0; i < 3; i++)
//     {
//         ld = ld + A[i][i];
//     }
//     j=2;
//     for (int i = 0; i < 3; i++)
//     {
//         rd = rd + A[i][j];
//         j--;
//     }
//     printf("Sum of left diagonal elements is = %d\n", ld);
//     printf("Sum of right diagonal elements is = %d", rd);
//     return 0;
// }

// WAP to convert decimal no. into binary no.

// int main()
// {
//     int i,no,n,arr[10];
//     printf("Enter the no. you want to convert into binary: ");
//     scanf("%d",&n);
//     no = n;
//     for (i = 0; n > 0; i++)
//     {
//         arr[i] = n%2;
//         n = n/2;
//     }
//     printf("Binary no. of %d is = \n",no);
//     for (i=i-1; i>=0; i--)
//     {
//         printf("%d",arr[i]);
//     }
//     return 0;
// }

int main()
{
    int a[10], i, j, temp;
    for (int i = 0; i < 10; i++)
    {
        printf("Enter the elements in A : ");
        scanf("%d", &a[i]);
    }
    printf("Array is: \n");
    for (i = 0; i < 10; i++)
    {
        printf("%5d", a[i]);
    }

    temp = a[1];
    a[1] = a[9];
    a[9] = temp;

    printf("\nNOW array is: \n");
    for (i = 0; i < 10; i++)
    {
        printf("%5d", a[i]);
    }
}