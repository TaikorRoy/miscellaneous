#include "stdafx.h"
#include "ZWang_library.h"
using namespace std;
using namespace ZWANG;
int _tmain(int argc, _TCHAR* argv[])
{
	call_from_dll("Hello worldxxxx!");
	call_from_dll();
	cin.get();
	return 0;
}
