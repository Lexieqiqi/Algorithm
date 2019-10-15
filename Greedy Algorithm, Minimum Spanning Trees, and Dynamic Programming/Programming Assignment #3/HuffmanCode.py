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
	def __init__(self,symbol=None,freq=None,code=''):
		self.symbol = symbol
		self.freq = freq
		self.codeWord = code
		self.parent = None
		self.lChild = None
		self.rChild = None



class CreateHuffmanTree:
	def __init__(self,queue):
		self.queue = queue

	def huffman(self):
		newqueue = []
		while len(self.queue)>1:
			self.queue.sort(key=lambda item:item.freq)
			lNode = self.queue.pop(0)
			rNode = self.queue.pop(0)
			if lNode.symbol is not None:
				newqueue.append(lNode)
			if rNode.symbol is not None:
				newqueue.append(rNode)
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
			self.queue.append(pNode)

		self.queue[0].parent = None
		return newqueue,self.queue[0]

	def huffmanEncoding(self):
		queue, root = self.huffman()
		freq = []
		codes = ['']*len(queue)
		symbol = []
		all_ = []

		for i in range(len(queue)):
			tmp_node = queue[i]
			while tmp_node.parent is not None:
				codes[i] = tmp_node.codeWord+codes[i]
				tmp_node = tmp_node.parent

			queue[i].codeWord = codes[i]
			symbol.append(queue[i].symbol)
			freq.append(queue[i].freq)
			all_.append((queue[i].codeWord,queue[i].symbol,queue[i].freq))

		return len(codes[0])#symbol,codes,freq


start = time.time()
c = CreateHuffmanTree(getSymbols("huffman.txt"))
#c = CreateHuffmanTree([2,3,1,3,23])
print("The depth is:",c.huffmanEncoding())
# c.huffman()
# print(c.huffmanEncoding())
end = time.time()
print("The running time is:",end-start)
# 0.08276891808374023