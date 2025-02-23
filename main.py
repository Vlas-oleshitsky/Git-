import sys
import random
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.uic import loadUi


class YellowCirclesApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.create_circle)

    def create_circle(self):
        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        for _ in range(random.randint(1, 10)):
            diameter = random.randint(10, 100)
            ellipse = QtWidgets.QGraphicsEllipseItem(0, 0, diameter, diameter)
            ellipse.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.yellow))
            ellipse.setPos(random.randint(0, 300), random.randint(0, 300))
            scene.addItem(ellipse)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = YellowCirclesApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
