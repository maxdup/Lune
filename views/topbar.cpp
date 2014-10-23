#include <QtGui>
#include <QLabel>
#include <QBoxLayout>
#include <QPushButton>
#include "topbar.h"

TopBar::TopBar(QWidget *parent) :
    QWidget(parent)
{
    this->setObjectName("topbar");
    QHBoxLayout *layout = new QHBoxLayout();
    this->setLayout(layout);

    QWidget *controls = new QWidget();
    controls->setObjectName("wcontrols");

    QBoxLayout *controls_l = new QBoxLayout(QBoxLayout::RightToLeft);
    QPushButton *resize = new QPushButton("^");
    QPushButton *shutdown = new QPushButton(";");
    QPushButton *minimize = new QPushButton("_");
    QPushButton *settings = new QPushButton("?");
    QObject::connect(resize, SIGNAL(clicked()), this, SLOT(toggle_maximized()));
    QObject::connect(shutdown, SIGNAL(clicked()), this, SLOT(shutdown()));
    QObject::connect(minimize, SIGNAL(clicked()), this, SLOT(minimize()));
    QObject::connect(settings, SIGNAL(clicked()), this, SLOT(settings()));
    controls_l->addWidget(shutdown);
    controls_l->addWidget(resize);
    controls_l->addWidget(minimize);
    controls_l->addWidget(settings);
    controls->setLayout(controls_l);

    layout->addWidget(new QLabel("Lune"));
    layout->addStretch();
    layout->addWidget(controls);
    layout->setContentsMargins(0,15, 0, 0);
}

void TopBar::shutdown(){ exit(0); }
void TopBar::maximize(){}
void TopBar::minimize(){}
void TopBar::windowed(){}
void TopBar::settings(){}
void TopBar::toggleMaximized(){}

TopBar::~TopBar()
{

}
