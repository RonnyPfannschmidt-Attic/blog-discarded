=============================
wrapping pro/toolkit strings
=============================


:date: 2008-03-03 00:00
:tags: pro_toolkit, c++, old


As part of my internship i have to work with Pro/Toolkit.
Their api isn't exactly nice, so i decided to write a set C++ wrappers.

The first part is an abstraction of their various wide string definitions::

	template <class Holder, size_t Len>
	class WString {
		/// mutable for easy passing to api calls
		Holder mutable data;

		void from_string(char const* str) {
			ProStringToWstring(data, const_cast<char*>(str));
		}
		void from_string(wchar_t const* str) {
			ProWstringCopy(
				const_cast<wchar_t*>(str),
				data,
				PRO_VALUE_UNUSED);
		}
	public:
		WString(char const* str = NULL) { from_string(str ? str : ""); }
		WString(std::string const & str) { from_string(str.c_str()); }
		WString(Holder const & str) { from_string(str); }

		operator std::string () const {
			// !! prevent multibyte character overflows
			char str[Len*3];
			ProWstringToString(str, data);
			return std::string(str);
		}
		wchar_t const * begin() const { return data; }
		wchar_t const * end() const { return data + Len; }

		operator Holder & () const { return data; }

		WString & operator =(WString const & str) {
			from_string(str);
			return *this;
		}
	};
	typedef WString<ProName, PRO_NAME_SIZE> Name;
	typedef WString<ProPath, PRO_PATH_SIZE> Path;
	typedef WString<ProLine, PRO_LINE_SIZE> Line;
	typedef WString<ProFileName ,PRO_FILE_NAME_SIZE> FileName;

Whats the use ?
================

This class keeps away all all common explicit string/wstring conversations and is usable with the orginal api.
It supports RAII, but it doesnt support Exceptions.
