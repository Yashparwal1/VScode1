4 stages behind the secene!!

1. Preprocessing
    ignores comments, expand macros, includes header files

    all these are stored in name.i file

2. Compilation
    name.i file is converted into Assembly level instructions and stored in name.s file


3. Assembly
    The name.s file which contains Assembly code is now converted into machine code (binary code) and stored in 
    name.o which contains binary codes.

4. Linking
    Linker combines all .o files into one exe file



# DATATYPES in C
* Basic datatype: int, char, float, double
* Derived datatype: array, pointer, structure, union
* Enumeration datatype: enum
* Void datatype: void

# FOR LOOPS
=> Properties of initialisation expression
> We can initiliase more than one variable.
> This expression is optional.

=> Properties of conditional expression
> It checks for specific condition to be satisfied. If it is not, the loop is terminated.

> It can have more than one condition. However the loop will iterate until the last condition becomes false. And other conditions wil be treated as statements. 

> It is also optional.

> *** It can perform the task of exp1 and exp3. i.e. we can initialise the variables as well as update the loop variable in this expression.

> We can pass zero or non zero value in exp2. However in C, any non-zero value is true and zero is false by default.

=> Properties of inc/dec expression
> This exp is used to update loop variable.
> We can update more than one varibale as the same time.
> It is also optional.

# Functions are used to devide a large c program into smaller pieces
* A Function can be called multiple times to provide reusability and modularity to C program.
* Aka procedure or sunroutine

=> SYNTAX:
return_type function_name(datatype parameter1,datatype parameter2,... )
{
    code to be executed;
}

ADVANTAGES:
1. We can avoid rewriting same logic through functions
2. We can devide work among fellow programmers using functions.
3. We can easily debug a program using function.

DECLARATION , DEFINATION AND CALL:
1. A function is declared to tell a compiler about its existence 
2. A function is defined to get some task done
3. A function is called in order to be used.

TYPES OF FUNCTION:
1. Library function - Functions included in C header files.
2. User-defined function - Functions created by programmer to reduce complexicity of the program.

FUNCTION CODE EXAMPLES:
* Without arguments and without return value
* Without arguments and with return value
* With argument and without return value
* With argument and with return value.

# What is recursive function?
Recursive function or Recursion is a process when a function calls a copy of itself to work on a smaller problem.

* Any function which calls itself is called recursive function.

A termination condition is imposed on such functions to stop them executing copies of themselves forever.

* Any problem that can be solved recursively can also be solved iteratively.

# CALL BY VALUE & CALL BY REFERENCE

* When a function is called, the values (expression) that are passed in the call are called arguments or actual parameters

* Formal parameters are local variables which are assigned values from the arguments when the function is called.

==> TYPES OF FUNCTION CALLS:

In C, we can call function in 2 ways based on how we specify the arguments.

1. Call by Value
when we copies values of actual parameters in formal parameters (simple)

=> When we call a function by value. it means thet we are passing the values of thr arguments which are copied into formal parameters of the function.
=>Which means that the original values remain unchanged and only the parameters inside the function changes.


2. Call by Reference1
we give address of the actual parameter (&x).
func1(int *a){ *a }
main(){int x=7; func1(&x);}

=> The call by reference method of passing arguments in a C function copies the address of the arguments into the formal parameters.
=> Addresses of the actual arguments are copied and then assigned to the corrosponding formal arguments


# ARRAY
* An array is a collection of data items of the same type.
* Items are stored at contigeous memory location.
* It can also store the collection of derived data types, such as pointers, structures etc.
* A one-demensional array is like a list.
* A two-dimentional array is like a table.
* The C lang. places no limits on the number of dimensions in an array.
* Some texts refer to one-dimensional arrays as vectors, two-dimensional array asmatrices, and use the general terms arrays when the number of dimensions is unspecified or unimportant

=> Why do we need array:
* Code that has array is sometimes more organised and redable.
* If you were to store the marks in a test of 56 student, creating 56 vars. will make program messy.
* Solution to this is array.
* We can create arrays of integers and store the consecutive marks corrosponding to the roll no. in the array.

=> ADVANTSGES OF ARRAY:
1. It is used to represent multiple data itmes of same type by using only single name.
2. Accessing an item in an array is very fast.
3. 2-dimensional array makes it easy in mathematical applications as it is used to represent matrices.
 
=> DISADVANTAGES OF ARRAY:
1. Poor time complexity of insertion and deletion operation.
2. Wastage of mmory since arrays are fixed in size.
3. If there is enough space present in the memory but not n contiguous form, you will not be able to initialize your array. 
4. It is not possible to increase the size of an array once you have declared the array.
 
=> PROPERTIES OF ARRAY:
1. Data in an array is stored in contiguous memory locations.
2. Each element of an array is of same size.
3. Any element of the array with given index can be accessed very quickly by using its address very quickly by using its address which can be calculated using the base address and the index.

=> SYNTAX for declaring arrays:
* datatype name[size]; 
* datatype name[size] = {x,y,z,....}; //size not req. in this case. 
* datatype name[rows][columns]; //for 2-D arrays
* We can also initialize array one-by-one by accessing it using its index:
    * name[0] = 0;

# PROBLEMS IN UISNG GETS(), SCANF(), FGETS() FUNCTIONS .............

//**********************************************************************************************
    // gets(arr);          
    //    not able to use gets after scanf, it takes "enter" of scanf as input and skips the gets function
    //    scanf() reads an integer and leaves a newline character in the buffer. So gets() only reads newline and the string in gets() is ignored by the program.
    
    // ------------------------------------------------------------------------------------------
    
    // when scanf() is used in loop
    // because every scanf() leaves a newline character in a buffer that is read by the next scanf.

    // ------------------------------------------------------------------------------------------

    // How to Solve the Above Problem?  
    /* 
    We can make scanf() to read a new line by using an extra \n, i.e., scanf(“%d\n”, &x) . In fact scanf(“%d “, &x) also works (Note the extra space).
    We can add a getchar() after scanf() to read an extra newline.
    */ 
   
//**********************************************************************************************
