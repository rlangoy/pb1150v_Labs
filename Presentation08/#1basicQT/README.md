Pre requirements
Installation of PyQT6

##
Icons from https://fonts.google.com/icons 
  folder_open_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg
  save_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg
  Licenced under Apache License, Version 2.0 (https://www.apache.org/licenses/LICENSE-2.0.html)

##  basicQT.py <br>
  Er en worksop template for bygging av en tekst editor
  Emner som bli belyst :
  
    Strukturen til et windows program
    App vs Window
    QApplication vs QMainWindow
    
    Hva er QtWidgets
    
    App - Eventer
    Hvorfor eventer i Window
    QWidgets - Events 
      Hvordan får tilgang til event funksjonene. exempel: closeEvent(QEvent)
      arv og polymorphism
    QWidgets properties
      window title
      Window Icon
      QIcon(..)
      Window (size/pros) <- setGeometry(QRect)
      QRect..
    
    Windows / Appsettings storage
    QSettings
      laste inn settings hvis de eksisterer    (Geomentry)
      lagre settings closeEvent(QCloseEvent)   (Geomentry)
    
    QMainWindow -central widget
      sette inn QPlainTextEdit (Tekst felt) som central widget
      
    QPlainTextEdit --  Lese / Skrive tekst
    	.setPlainText("Vis tekst til bruker")
    	.toPlainText()   # les ut teksten	
      
    QMainWindow - Menu Bar
       self.menuBar().addAction(QAction) 
       QAction("&Open File", self).triggered.connect( customActionFunc)
       QT  -- .connect -- <- connects kobler til egen funksjon
   
    QFileDialog  - QT fil dialog.
		QFileDialog().exec()   # Vise if __name__ == '__main__':  i if __name__ == '__main__':
		QFileDialog.selectedFiles()[0]  <- Liste over valge filer
	   
    Save/load from file rep forelesning #4

  
  
