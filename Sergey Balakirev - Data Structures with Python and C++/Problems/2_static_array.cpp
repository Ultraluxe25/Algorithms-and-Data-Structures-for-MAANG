/* Feat 4. Create a static array in the program called ar, consisting of 7 elements of char types, 
using the following syntax:

<type of elements> <array name>[array size];

Fill this entire array with the characters 'a', 'b', 'c', 'd', 'e', ​​'f', 'g' in order. 
Then, after the 'b' character, insert a new value (symbol) '#' so that
so that the array ar ends up containing the values:

'a', 'b', '#', 'c', 'd', 'e', ​​'f'

P.S. There is no need to display anything on the screen, just create an array in accordance with the task.
*/

#include <iostream>

int main(void)
{
    using namespace std;
    
    char ar[7];
    ar[0] = 'a';
    ar[1] = 'b';
    ar[2] = 'c';
    ar[3] = 'd';
    ar[4] = 'e';
    ar[5] = 'f';
    ar[6] = 'g';
    
    for (int i = 6; i > 2; i--) {
        ar[i] = ar[i - 1];
    }
    ar[2] = '#';
    return 0;
}