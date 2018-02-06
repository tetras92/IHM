import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
	
	#############
	def __init__(self):
           super(MainWindow, self).__init__()
           self.resize(400,400)
           
           
           #########################################################"
           bar = self.menuBar()

           fileMenu = bar.addMenu("Fichier")

           OpenAct = QAction(QIcon("open.png"), "Open...", fileMenu)
           OpenAct.setShortcut("Ctrl+O")
           OpenAct.setStatusTip(self.tr("Open"))
           fileMenu.addAction(OpenAct)
           OpenAct.triggered.connect(self.openFile)
           
           SaveAct = QAction(QIcon("save.png"), "Save...", fileMenu)
           SaveAct.setShortcut("Ctrl+S")
           SaveAct.setStatusTip(self.tr("Save"))

           fileMenu.addAction(SaveAct)
           SaveAct.triggered.connect(self.saveFile)
           
           QuitAct = QAction(QIcon("quit.png"), "Quit...", fileMenu)
           QuitAct.setShortcut("Ctrl+X")
           QuitAct.setStatusTip(self.tr("Quit"))

           fileMenu.addAction(QuitAct)
           QuitAct.triggered.connect(self.quit)
           
            #########################################################"           
           
           fileToolBar = QToolBar("Open")
           fileToolBar.addAction(OpenAct)
           self.addToolBar(fileToolBar)
           
           fileToolBar = QToolBar("Save")
           fileToolBar.addAction(SaveAct)
           self.addToolBar(fileToolBar)
           
           fileToolBar = QToolBar("Quit")
           fileToolBar.addAction(QuitAct)
           self.addToolBar(fileToolBar)
           
           
           #########################################################"
           self.textEdit = QTextEdit(self)
           self.setCentralWidget(self.textEdit)
           #########################################################"
           
           super(MainWindow, self).statusBar()
           
           
           
#	###############
	def openFile(self):
           fileName = QFileDialog.getOpenFileName(self,"Open file","..")
#           print(fileName+"_______________")
           file = QFile(fileName)
           if file.open(QFile.ReadOnly | QFile.Text) :
               stream = QTextStream(file)
               self.textEdit.setPlainText(stream.readAll())      
	def saveFile(self):

         fileName = QFileDialog.getSaveFileName(self,"Save file","../untitled")
         file = QFile(fileName)
         if file.open(QFile.WriteOnly) :
             file.write(self.textEdit.toPlainText())
         print(fileName)		
#
#	###############
      def closeEvent(self, event):
          return
	def quit(self):
         quest = QMessageBox.question(self,"Quit","Voulez-vous quitter?","No","Yes")
         if quest == 1:
             self.close()

#      def closeEvent(self, event):
#         quest = QMessageBox.question(self,"Quit","Voulez-vous quitter?","No","Yes")
#         if quest == 1:
#         self.close()
#         else:
#         event.ignore()

def main(args):
#	print("Hello World")
    app = QApplication(args) 
    win = MainWindow()
    win.show()
    app.exec_()

if __name__ == "__main__":
	main(sys.argv) 
 


#R2: il manquait l'appel au constructeur de la superclasse QMain et l'instanciation de l'application QApplication()
#R5 : Pour connecter les actions aux slots, on fait : QuitAct.triggered.connect(self.quit) 