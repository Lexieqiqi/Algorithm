import queue
import time

def getSymbols(file):
	f = open(file)
	line = f.readline()
	num_sym = int(line.strip())
	symbols = []
	index = 1
	while True:
		line = f.readline()
		if line!='':
			symbols.append(HuffmanNode(symbol = str(index),freq = int(line.strip()),code=''))
			index = index+1
		if not line:
			break
	return symbols

class HuffmanNode:
	def __init__(self,symbol=None,freq=None,code='',procode=None):
		self.symbol = symbol
		self.freq = freq
		self.codeWord = code
		self.procode = procode
		self.parent = None
		self.lChild = None
		self.rChild = None


def FindMin(a,b):
	if len(a)==0:
		return b.pop(0)
	if len(b)==0:
		return a.pop(0)
	if a[0].freq>b[0].freq:
		return b.pop(0)
	return a.pop(0)

class CreateHuffmanTree:
	def __init__(self,queue):
		self.queue = queue
		self.code = ''

	def huffman(self):
		self.queue.sort(key=lambda item:item.freq)
		Fqueue = self.queue[:]
		Squeue = []
		while not (len(Fqueue) == 0 and len(Squeue)==1):
			lNode = FindMin(Fqueue,Squeue)
			rNode = FindMin(Fqueue,Squeue)
			if lNode.freq>rNode.freq:
				lNode.codeWord = '1'
				rNode.codeWord = '0'
			else:
				lNode.codeWord = '0'
				rNode.codeWord = '1'
			pNode = HuffmanNode(freq=lNode.freq+rNode.freq)
			pNode.lChild = lNode
			pNode.rChild = rNode
			lNode.parent = pNode
			rNode.parent = pNode
			Squeue.append(pNode)
		return Squeue.pop()

	def huffmanEncoding(self):
		freq = []
		codes = ['']*len(self.queue)
		symbol = []
		all_ = []

		for i in range(len(self.queue)):
			tmp_node = self.queue[i]
			while tmp_node.parent is not None:
				codes[i] = tmp_node.codeWord+codes[i]
				tmp_node = tmp_node.parent

			self.queue[i].codeWord = codes[i]
			symbol.append(self.queue[i].symbol)
			freq.append(self.queue[i].freq)
			all_.append((self.queue[i].codeWord,self.queue[i].symbol,self.queue[i].freq))

		return len(codes[0])#symbol,codes,freq


starttime = time.time()
c = CreateHuffmanTree(getSymbols("huffman.txt"))
#c = CreateHuffmanTree([2,3,1,3,23])
# c.huffmanEncoding(c.huffman())

c.huffman()

print("The depth is:",c.huffmanEncoding())
endtime = time.time()
print("The running time is:",endtime-starttime)
# 0.010932207107543945