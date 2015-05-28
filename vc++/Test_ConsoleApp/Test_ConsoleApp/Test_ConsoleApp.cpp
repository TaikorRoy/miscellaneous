// obtaining file size
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

namespace test
{
   string string_a = "test name space";
}

int main () {
  streampos begin,end;
  ifstream myfile ("example.bin", ios::binary);
  begin = myfile.tellg();
  myfile.seekg (0, ios::end);
  end = myfile.tellg();
  myfile.close();
  cout << "size is: " << (end-begin) << " bytes.\n";
  cout << test::string_a;
  return 0;
}

