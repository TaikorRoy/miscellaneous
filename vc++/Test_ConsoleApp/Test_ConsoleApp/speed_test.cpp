#include <cstdlib>
#include <iostream>

using namespace std;
int main()
{
    int max_c = rand();
    int min_c = rand();
    int buffer;
   while(true)
   {

    buffer = rand();
    if(buffer > max_c)
    {
        max_c = buffer;
    }
    buffer = rand();
    if(buffer < min_c)
    {
        min_c = buffer;
    }
   cout << "Max" << max_c << "    " << "Min" << min_c << "\n";
   }
}
