// Most Basic C program i used to write while penetrating a website's web server for checking the OS command injection vulnebility if possible 
// by exploiting  the facility of copmpiling and running the C program on the system terminal 


#include<stdio.h>
#include<stdlib.h>

int main()
   {
   
         system("clear");
         system("pwd && ls");   // system call to check the command injection possiblity 
         // outputs the present working directory and list out the content of the present directory 
   
   // server is vulnerable to command injection if list out the the content on the system . 
         
   
   // this code can be use for testing those web applications which provides the compiler running features. 
return 0; 
   
   }
   
 // end of program 
