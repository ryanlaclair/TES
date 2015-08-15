#! /usr/local/bin/python
"""
File:       tes_gui.py

Author:     Ryan LaClair <rgl8828@rit.edu>
"""

import sys
from PyQt4 import QtGui, QtCore
import tes

def main():
    """The main entry point for the TES program graphical user interface.
    """

    app = QtGui.QApplication(sys.argv)
    mw = tes.TesMainWindow()
    mw.raise_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
