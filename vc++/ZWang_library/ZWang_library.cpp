#include "ZWang_library.h"
namespace ZWANG
{
	void call_from_dll(const string &str)
	{
		cout << str << endl;
		cout << "Success!" << endl;
	}
}