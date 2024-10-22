import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PIL import Image

class WebpToJpgConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Webp to JPG Converter')
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.label = QLabel('Select a .webp file to convert')
        layout.addWidget(self.label)

        self.btn_select = QPushButton('Select File', self)
        self.btn_select.clicked.connect(self.select_file)
        layout.addWidget(self.btn_select)

        self.btn_convert = QPushButton('Convert', self)
        self.btn_convert.clicked.connect(self.convert_file)
        self.btn_convert.setEnabled(False)
        layout.addWidget(self.btn_convert)

        central_widget.setLayout(layout)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Webp File', '', 'Webp Files (*.webp)')
        if file_name:
            self.webp_file = file_name
            self.label.setText(f'Selected file: {file_name}')
            self.btn_convert.setEnabled(True)

    def convert_file(self):
        if hasattr(self, 'webp_file'):
            jpg_file = self.webp_file.rsplit('.', 1)[0] + '.jpg'
            try:
                with Image.open(self.webp_file) as img:
                    img.convert('RGB').save(jpg_file, 'JPEG')
                self.label.setText(f'Conversion successful!\nSaved as: {jpg_file}')
            except Exception as e:
                self.label.setText(f'Error during conversion: {str(e)}')
        else:
            self.label.setText('Please select a file first')

def main():
    app = QApplication(sys.argv)
    converter = WebpToJpgConverter()
    converter.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()