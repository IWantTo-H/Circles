import random
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
import io
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QPen, QColor


template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>534</width>
    <height>528</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>440</y>
      <width>101</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Нажать</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>534</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.btn = self.pushButton
        self.btn.clicked.connect(self.draw)

        self.circle = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor("yellow"), 2))

        for x, y, radius in self.circle:
            painter.drawEllipse(x - radius, y - radius, 2 * radius, 2 * radius)

    def draw(self):
        width = self.width()
        height = self.height()
        x = random.randint(50, width - 50)
        y = random.randint(50, height - 50)
        radius = random.randint(20, 80)
        self.circle.append((x, y, radius))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Circle()
    window.show()
    sys.exit(app.exec())
