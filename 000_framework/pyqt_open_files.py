'''
qt開檔教學
https://steam.oxxostudio.tw/category/python/pyqt5/qfiledialog.html

python qt package to windows 11 exe
  auto-py-to-exe 2.43.3
  https://pypi.org/project/auto-py-to-exe/
  Packaging PyQt5 applications for Windows with PyInstaller & InstallForge Turn your PyQt5 application into a distributable installer for Windows
  https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/
  Python application packaged for Windows 11 using pyside6-deploy complains about numpy installation
  https://stackoverflow.com/questions/77747671/python-application-packaged-for-windows-11-using-pyside6-deploy-complains-about
  
Python QT version: 5 
Note : Qt 6.6.0 Released 10th of October 2023!
'''


from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

def open():
    filePath , filterType = QtWidgets.QFileDialog.getOpenFileNames()  # 選擇檔案對話視窗
    print(filePath , filterType)
    print("Hi 你好 QT.")

btn = QtWidgets.QPushButton(Form)  # 加入按鈕
btn.move(20, 20)
btn.setText('開啟檔案')
btn.clicked.connect(open)

Form.show()
sys.exit(app.exec_())