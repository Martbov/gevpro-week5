#!usr/bin/python3.4

import sys
from PyQt4 import QtGui, QtCore
from collections import Counter


class UnigramCounter(QtGui.QWidget):
	""" A program that counts unigrams in sentences from a given file """

	def __init__(self, argv):
		super(UnigramCounter, self).__init__()
		self.setWindowTitle('UnigramCounter')
		self.setGeometry(500, 200, 400, 400)
		self.sentences = open(argv[1])
		self.unigramCounter = Counter()
		self.initUI()

	def initUI(self):
		""" Initializes the graphic interface """
		self.wordLabel = QtGui.QLabel('Word')
		self.frequencyLabel = QtGui.QLabel('Frequency')

		self.grid = QtGui.QGridLayout()
		self.grid.setSpacing(10)

		self.grid.addWidget(self.wordLabel, 1, 0)
		self.grid.addWidget(self.frequencyLabel, 1, 1)
		
		count = 1
		for word, value in self.freqCounter():
			self.grid.addWidget(QtGui.QLabel('#'+str(count) + ' '+word))
			self.grid.addWidget(QtGui.QLabel(str(value)))
			count += 1

		self.setLayout(self.grid)

	def freqCounter(self):
		""" Counts unigrams using Counter data structure and returns 20 most frequent ones """
		for line in self.sentences:
			self.unigramCounter.update(line.split())
		return self.unigramCounter.most_common(20)


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	uCounter = UnigramCounter(sys.argv)
	uCounter.show()
	app.exec_()