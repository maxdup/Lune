#-------------------------------------------------
#
# Project created by QtCreator 2014-10-20T14:08:19
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = NeoLune01
TEMPLATE = app


SOURCES += main.cpp\
    views/mainwindow.cpp \
    views/topbar.cpp \
    views/nav.cpp

HEADERS  += \
    views/mainwindow.h \
    views/topbar.h \
    views/nav.h

OTHER_FILES +=

RESOURCES += \
    views/qss/qss.qrc \
    img/img.qrc
