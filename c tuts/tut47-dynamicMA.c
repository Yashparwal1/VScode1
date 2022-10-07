/* Dynamic Memory Allocation is a technique of allocating memory for the variables in Run-Time
 * SIze of a Data Structure can be changed in runtimr.
 * Memoy assigned to a program in a typical achitecture can be broken down into four segments:
   1. Code
   2. Static/Global variables
   3. Stack -- used for static memory allocation and its allocation is dealt with when the program is         compiled
   4. Heap -- used for dynamic memory allocation
 * FUNCTION of  DMA:
    1. malloc() - memory allocation
      * It reserves a block of memory with the give amount of bytes.
      * the return value is a void pointer to the allocated space.
      * Therefore the void pointer need to be casted to the appropriate type as per the requirements.
      * However, if the space is insufficient, allocation of memory fails and it returns a NULL pointer.
      *** All the values at allocated memory are initialized to garbage values.
      * SYNTAX: ptr=(ptr-type*) malloc(size_in_bytes);
      * eg.     ptr=(int*) malloc(3 * sizeof(int));

    2. callor() - contigous allocation
      * It reserves n block of memory with the given amount of bytes.
      * the return value is a void pointer to the allocated space.
      * therefore the voide pointer needs to be casted to the appropriate type as per the requirements.
      * However, if the space is insufficient, allocation of memory fails and it returns a NULL pointer.
      *** All the values at allocated memory are initialised to 0.

      * SYNTAX: ptr=(ptr-type*) calloc(n, size_in_bytes);
      * eg.     ptr=(int*) calloc(5, 3*sizeof(int));

    3. realloc() - Reallocaton
      * If the dynamically allocated memory is insufficient we can change the size of previously allocated memory using realloc() functionn

      *SYNTAX: ptr==(ptr-type*) realloc(ptr, new_size_in_bytes);

    4. free()  - used to free
      * if the dynamically allocated memory is not reuired anymore, we can free it using free() function.
      * This will free the memory beinng used by the program in the heap.
      * SYNTAX: free(ptr);
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
  int i, *ptr;
  ptr = (int*) malloc(3 * sizeof(ptr));
  // int* ptr = malloc(3*sizeof(*ptr));
  for (int i = 0; i < 4; i++)  
  {
    printf("enter the value no %d of the array:\n", i, ptr[i]);
    scanf("%d", &ptr[i]);
  }
  for (int i = 0; i < 6; i++)
  {
    printf("%d ", ptr[i]);
  }

  // jab hum malloc me 2 assign kar dete or for loop i < 4 kar dete h toh wo 3, 4 ko garbage value ni leta kyoki wo scanf ki value hi print karta h.

  // // use of mallc()
  // int *ptr, n;
  // printf("Enter the size of array: ");
  // scanf("%d",&n);
  // ptr = (int *)malloc(n * sizeof(int));

  // for (int i = 0; i < n; i++)
  // {
  //   printf("Enter the elements: ");
  //   scanf("%d", &ptr[i]);
  // }
  // printf("The values are: \n");
  // for (int i = 0; i < n; i++)
  // {
  //   printf("%d ", ptr[i]);
  // }

  // // use of calloc()
  // int *ptr, n;
  // printf("Enter the size of array: ");
  // scanf("%d",&n);
  // ptr = (int *)calloc(n, sizeof(int));

  // for (int i = 0; i < n; i++)
  // {
  //   printf("Enter the elements: ");
  //   scanf("%d", &ptr[i]);
  // }
  // printf("The values are: \n");
  // for (int i = 0; i < n; i++)
  // {
  //   printf("%d ", ptr[i]);
  // }

  // //use of realloc()

  // printf("Enter the size of new array: ");
  // scanf("%d",&n);
  // ptr = (int *)realloc(ptr, n*sizeof(int));

  // for (int i = 0; i < n; i++)
  // {
  //   printf("Enter the elements: ");
  //   scanf("%d", &ptr[i]);
  // }
  // printf("The NEW values are: \n");
  // for (int i = 0; i < n; i++)
  // {
  //   printf("%d ", ptr[i]);
  // }
  // free(ptr);

  // for (int i = 0; i < n; i++)
  // {
  //   printf("%d ", ptr[i]);
  // }

  // something extra...........................

  // int index = 0, i, n, *marks, ans;
  // printf("Enter the size of arrar: ");
  // scanf("%d",&n);
  // marks = (int*) calloc(n, sizeof(int));
  // // printf("The memory is successfully allocated using malloc()\nmarks = %p",marks);

  // do
  // {
  //   printf("Enter marks: ");
  //   scanf("%d", &marks[index]);
  //   printf("Would you like to add more marks (1 for yes and 0 for no)?? ");
  //   scanf("%d",&ans);
  //   if (ans == 1)
  //   {
  //     index++;
  //     marks = (int*) realloc(marks, (index+1)*sizeof(int));
  //   }
  //   printf("Memory is successfully reallocated using realloc().......\nbase address- %p\n",marks);
  // } while (ans == 1);

  // for (int i = 0; i <= index; i++)
  // {
  //   printf("marks of students %d are %d\n",i,marks[i]);
  // }

  // free(marks);

  return 0;
}