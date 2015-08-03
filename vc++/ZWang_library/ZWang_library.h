#ifndef _ZWANG
#define _ZWANG
#include <iostream>
#include <string>
namespace ZWANG
{
	using namespace std;
	__declspec(dllexport) void call_from_dll(const string &str = "Call the funtion from dll.");
}
#endif _ZWANG