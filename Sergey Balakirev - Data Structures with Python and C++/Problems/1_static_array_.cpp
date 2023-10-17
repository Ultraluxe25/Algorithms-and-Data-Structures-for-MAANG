/* Feat 3. Create a static array in the main() function in the program called ar, 
consisting of 15 elements of int types, using the following syntax:

<type of elements> <array name>[array size];

Then, enter the value -1 in all elements. After this, write the number 100 into the fifth element (counting starts from one).

P.S.
There is no need to display anything on the screen, just create an array in accordance with the task.
*/

#include <iostream>

using namespace std;

int main(void) {
    int ar[15];
    for (int i = 0; i < 15; i++) {
        ar[i] = -1;
    }
    
    ar[4] = 100;
    return 0;
}