#ifndef TOPBAR_H
#define TOPBAR_H

#include <QWidget>

class TopBar : public QWidget
{
    Q_OBJECT
public:
    explicit TopBar(QWidget *parent = 0);
    ~TopBar();

signals:

public slots:
    void shutdown();
    void maximize();
    void minimize();
    void windowed();
    void settings();
    void toggleMaximized();
};

#endif // TOPBAR_H
