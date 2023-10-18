/* Create the following array in the program:

char str_1[] = "Structures data";
Create another character array in the program with the name str_2 and length 20. 
Copy the contents of the str_1 array to the str_2 array.

P.S. There is no need to display anything on the screen, just create arrays in accordance with the task.
*/

#include <iostream>
#include <cstring>

int main(void)
{
    using namespace std;
    char str_1[] = "Structures data";
    char str_2[20];
    strcpy(str_2, str_1);
   return 0;
}