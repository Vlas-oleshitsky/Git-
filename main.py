import sys
import random
from PyQt6 import QtWidgets, QtGui, QtCore


class YellowCirclesApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Git и случайные окружности')

        self.pushButton = QtWidgets.QPushButton('Создать круги', self)
        self.pushButton.setGeometry(200, 430, 100, 30)
        self.pushButton.clicked.connect(self.create_circle)

        self.graphicsView = QtWidgets.QGraphicsView(self)
        self.graphicsView.setGeometry(0, 0, 500, 400)

    def create_circle(self):
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        for _ in range(random.randint(1, 10)):
            diameter = random.randint(10, 100)
            color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            ellipse = QtWidgets.QGraphicsEllipseItem(0, 0, diameter, diameter)
            ellipse.setBrush(QtGui.QBrush(color))
            ellipse.setPos(random.randint(0, 450), random.randint(0, 350))
            scene.addItem(ellipse)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = YellowCirclesApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
