#include "top.h"

Top::Top(QWidget *parent) :
    QWidget(parent)
{
    QWidget *mw = parent;
    bool maxed = false;
    this->setObjectName("topbar");
    QHBoxLayout *layout = new QHBoxLayout();

    QLabel *lab  = new QLabel("okay");
    //layout.add
    this->setLayout(layout);

    QWidget *controls = new QWidget();
    controls->setObjectName("wcontrols");
    //QBoxLayout *controls_l = new QBoxLayout(this);
}
