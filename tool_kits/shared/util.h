#pragma once
#include <string>
#include <map>

#define DEMO_GLOBAL_APP_KEY			""
#define DEMO_GLOBAL_TEST_APP_KEY	""

class QString
{
public:
	static std::string GetGUID();
	static std::string GetMd5(const std::string& input);
	static void NIMFreeBuf(void *data);
};

class QPath
{
public:
	static std::wstring GetAppPath(); //��ȡexe����Ŀ¼�������"\\"
	static std::wstring GetUserAppDataDir(const std::string& app_account);
	static std::wstring GetLocalAppDataDir();
	static std::wstring GetNimAppDataDir(const std::wstring& app_data_dir);  // "...Local\\Netease\\Nim\\"
	static void			AddNewEnvironment(const std::wstring& directory); // ���һ��·���� exe �Ļ�������
};

class QCommand
{
public:
	static void ParseCommand(const std::wstring &cmd);
	static bool AppStartWidthCommand(const std::wstring &app, const std::wstring &cmd);
	static bool RestartApp(const std::wstring &cmd);
	static std::wstring Get(const std::wstring &key);
	static void Set(const std::wstring &key, const std::wstring &value);
	static void Erase(const std::wstring &key);
private:
	static std::map<std::wstring,std::wstring> key_value_;
};