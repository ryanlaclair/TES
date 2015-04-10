"""
"""

import sys
from PyQt4 import QtGui, QtCore
import tes
#from tes.views.tes_main_window import TesMainWindow

def main():
    """
    """

    app = QtGui.QApplication(sys.argv)
    mw = tes.TesMainWindow()
    mw.raise_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
