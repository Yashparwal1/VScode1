==> 1991 by Sun Microsystem - James Goshlin
==> Initially it was called Oak 
  
## Java Execution Process:

- Compilation:  In Java, your source code is first compiled by the Java compiler (e.g., javac). The compiler generates bytecode files (.class) from your source code.
- Bytecode:     Java source code is compiled into platform-independent bytecode, which is a low-level representation of your code. This bytecode can be executed on any platform with a Java Virtual Machine (JVM).
- JVM:          To run a Java program, you need a JVM installed on the target machine. The JVM interprets and executes the bytecode. It provides a layer of abstraction, allowing Java programs to be platform-independent.
- Execution:    The JVM loads the bytecode files, verifies them, and then executes the Java program. It performs just-in-time (JIT) compilation and various optimizations to improve performance during execution.
- Garbage Collection:   Java includes automatic memory management through garbage collection, which manages memory allocation and deallocation for you.

## C/C++ Execution Process:

- Compilation:    In C and C++, source code is compiled by the C/C++ compiler (e.g., gcc for C or g++ for C++) into machine code specific to the target platform. This results in binary executable files (e.g., .out, .exe).
- Machine Code:   The generated binary executable contains machine code that is specific to the hardware and operating system it was compiled for. This means that C/C++ programs are not inherently platform-independent.
- Direct Execution:   The generated binary executable is run directly by the operating system. There is no intermediate bytecode or virtual machine. This results in potentially faster and more efficient code execution.
- Manual Memory:   Management: In C and C++, memory allocation and deallocation are manual. Developers need to allocate and free memory explicitly. This provides more control but can also lead to memory-related bugs.
 
## What is this byte code?
 
- A low-level representation of code that is designed to be executed by a virtual machine. 
- used in languages like Java and some other to achieve platform-independence and runtime portability.
- concept of "write once, run anywhere" (WORA)
- C# also uses bytecode with CLR (Common Language Runtime)

## what does it look like if i open the bytecode file?

- non human readable code in binary fomrat
- a series of binary ins. meant to be executed by a vurtual machine
            ca fe ba be 00 00 00 34 00 0e 0a 00 06 00 16 0a 00
            0c 00 1a 0a 00 0e 00 16 0a 00 18 00 1e 0a 00 0e 00
            20 0a 00 0e 00 26 0a 00 1e 00 28 0a 00 2a 00 2c 0a
            00 0e 00 2e 0a 00 30 00 32 0a 00 32 00 34 0a 00 3a
- to examine or manipulate bytecode, we can use tools like javap (available in jdk) --- allows us to disassemble 

## If its in the binary format then why its not called machine code directly.

- its diff. from traditional machine code
- both are in binary form but have different purposes.

--- M/C is machine dependent and is executed directly by CPU
--- B/C is not machine independent and is executed by virtual machine

--- M/C - low level ins.
--- B/C - typically higher level ins. than machine code 


## STRINGS

String is a non primitive datatype, because it references a memory location where data is stored in the heap memory (or string constant pool).
 -- It references a memory where an object is actually placed. Therefore var of non primitive datatype are also known as Object Reference Datatype (or reference datatype)
 -- This ORD lives in the stack memory and the object to which it points always lives in heap memory.
 -- the stack holds a pointer to the object on the heap.
 -- THUS, all non-primitive datatypes are simply called objects which are created by instantiating a class.

 -- STRING is the sequence(array) of characters  
    eg. char[] c = {'y', 'a', 's', 'h'}
        [String s = new String(c);] --- is same as --- [String s="yash";]
        <<we have an interface in java to represent Sequence character called "CharSequence">>
 -- String is a class (already defined) which hava many methods.
    string class is defined like this --> 
    public final class String extends Object implements CharSequence, Serializable, Comparable {___}
        <why String class is final?>

-- Since String is a class, so we can create its object too.
    String s = new String();
    This object 's' is immutable
    when we write String s = "yash". ---> This also creates an object.
    <<So whats the diff. here??>> ---> the concept of String Constant Pool (SCP) applied here


-- To create String, 3 classes are there:
    1. String   2. StringBuffer     3. StringBuilder
    So total 4 ways to create String (3 with these and 1 directly)

### immutablity
    - always related to string objects not literals
    - used for "String Object" i.e. String objects are immutable
    - once it is created, its data or state cannot be changed but a new string object is created.
    
    String s = new String("yash") //"yash" object and literal are created in heap and SCP resp.
    s.concat(" parwal")
    sop(s) --> yash // because s is still pointing to "yash" object, though " parwal" literal is created in SCP and "yash parwal" object is created in heap.
    s = s.concat(" java")
    sop(s) --> yash java // now s is pointing to "yash java", and also " java" literal is created in scp

