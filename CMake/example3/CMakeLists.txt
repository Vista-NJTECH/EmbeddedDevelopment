PROJECT (HELLO)

ADD_SUBDIRECTORY (src bin)

INSTALL (FILES COPYRIGHT README DESTINATION /usr/local/share/doc/cmake_test/)

INSTALL (PROGRAMS runIt.sh DESTINATION /usr/local/bin)

INSTALL (DIRECTORY doc/ DESTINATION /usr/local/share/doc/cmake_test)