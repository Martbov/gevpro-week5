#!usr/bin/python3.4

import sys
from PyQt4 import QtGui, QtCore
from collections import Counter


class NgramCounter(QtGui.QWidget):
	""" A program that counts unigrams or bigrams based on the user's preference """

	def __init__(self):
		super(NgramCounter, self).__init__()
		self.setWindowTitle('NgramCounter')
		self.setGeometry(500, 200, 400, 400)
		self.ngramCounter = Counter()
		self.unigramCounter = Counter()
		self.initUI()
		

	def initUI(self):
		""" Initializes the graphic interface """
		self.fileSelect = QtGui.QPushButton('Choose file', self)
		self.methodSelect = QtGui.QComboBox()
		self.fileLabel = QtGui.QLabel('File:')
		self.methodLabel = QtGui.QLabel('Method:')
		self.methodSelect.addItems(['Unigrams', 'Bigrams'])
		self.fileSelect.clicked.connect(self.freqDisplay)
		self.methodSelect.currentIndexChanged['QString'].connect(self.methodChange)
		self.textBox = QtGui.QTextEdit()
		self.textBox.setReadOnly(True)

		self.grid = QtGui.QGridLayout()
		self.grid.setSpacing(10)
		self.grid.addWidget(self.methodSelect, 1, 1)
		self.grid.addWidget(self.fileSelect, 2, 1)
		self.grid.addWidget(self.fileLabel, 2, 0)
		self.grid.addWidget(self.methodLabel, 1, 0)
		self.grid.addWidget(self.textBox, 3, 0,)
		self.setLayout(self.grid)

	def methodChange(self):
		""" Lets the user change the method from unigram to bigram and vice versa """
		method = 1
		if self.methodSelect.currentText() == 'Bigrams':
			method = 2
		return method

	def freqDisplay(self):
		""" Creates the text shown in textbox for the unigrams or bigrams based on the chosen method """
		self.sentences = QtGui.QFileDialog.getOpenFileName(self)
		self.textBox.clear()
		if self.methodChange() == 1:
			self.textBox.clear()
			count = 1
			for word, value in self.freqCounter():
				self.textBox.append('#'+str(count) + ' {:15} {:>10}'.format(word, value))
				count += 1
		else:
			self.textBox.clear()
			bigramsDic = {}
			for line in open(self.sentences):
				words = line.split()
				for i in range(len(line.split())-1):
					wordPair = ''.join(words[:2])
					biGram = []
					biGram.append(wordPair)
					self.ngramCounter.update(biGram)
					bigramsDic[wordPair] = words[:2]
					words.pop(0)
			count = 1		
			for bigram in self.ngramCounter.most_common(20):
				self.textBox.append('#'+str(count) + ' ' + ' '.join(bigramsDic.get(str(bigram[0])))+'    '+str(bigram[1]))
				count += 1	

	def freqCounter(self):
		""" Counts unigrams using Counter data structure and returns 20 most frequent ones """
		for line in open(self.sentences):
			self.unigramCounter.update(line.split())
		return self.unigramCounter.most_common(20)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	n = NgramCounter()
	n.show()
	app.exec_()
