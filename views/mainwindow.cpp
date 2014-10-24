#include "mainwindow.h"
#include "topbar.h"
#include <QtGui>
#include <QWidget>
#include <QGridLayout>
#include <QSizeGrip>
#include <QFrame>
#include <QStackedLayout>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    this->setObjectName("mainwindow");

    QFontDatabase::addApplicationFont(":luneicons.otf");
    QFile File(":general.qss");
    File.open(QFile::ReadOnly);
    QString StyleSheet = QLatin1String(File.readAll());
    this->setStyleSheet(StyleSheet);

    this->setWindowFlags(Qt::FramelessWindowHint);
    this->setWindowIcon(QIcon(":lune.png"));
    this->setWindowTitle("Lune");

    QWidget *lune = new QWidget(this);
    QGridLayout *window_ctrl_layout = new QGridLayout(lune);
    window_ctrl_layout->setContentsMargins(0,0,0,0);
    lune->setLayout(window_ctrl_layout);

    QSizeGrip *grip1 = new QSizeGrip(lune);
    QSizeGrip *grip2 = new QSizeGrip(lune);
    QSizeGrip *grip3 = new QSizeGrip(lune);
    QSizeGrip *grip4 = new QSizeGrip(lune);
    grip1->setSizePolicy(QSizePolicy::Minimum, QSizePolicy::Minimum);
    grip2->setSizePolicy(QSizePolicy::Minimum, QSizePolicy::Minimum);
    window_ctrl_layout->addWidget(grip1, 0, 0);
    window_ctrl_layout->addWidget(grip2, 0, 2);
    window_ctrl_layout->addWidget(grip3, 2, 2);
    window_ctrl_layout->addWidget(grip4, 2, 0);

    this->setCentralWidget(lune);
    TopBar *top = new TopBar(lune);

    QWidget *app_container = new QWidget();
    window_ctrl_layout->addWidget(top, 0, 1);
    window_ctrl_layout->addWidget(app_container, 1, 1);

    QVBoxLayout *main_container = new QVBoxLayout();
    app_container->setLayout(main_container);

    QWidget *content_v = new QWidget();
    QWidget *library_v = new QWidget();

    QFrame *stack_container = new QFrame();

    content_v->setLayout(new QVBoxLayout());
    content_v->layout()->addWidget(library_v);
    //content_v->layout()->addWidget(status_v);
    content_v->setContentsMargins(0,0,0,0);

    QStackedLayout *view_stack = new QStackedLayout();
    view_stack->addWidget(content_v);
    //view_stack->addWidget(settings_v);

    stack_container->setLayout(view_stack);

    main_container->addWidget(stack_container);
}

MainWindow::~MainWindow()
{

}
