// Most Basic C program i used to write while penetrating a website's web server for checking the OS command injection vulnebility if possible 
// by exploiting  the facility of copmpiling and running the C program on the system terminal 


#include<stdio.h>
#include<stdlib.h>

int main()
   {
   
         system("clear");
         system("pwd && ls");   // system call to check the command injection possiblity 
         // outputs the present working directory and list out the content of the present directory 
         
return 0; 
   
   }
   
 // end of program 
