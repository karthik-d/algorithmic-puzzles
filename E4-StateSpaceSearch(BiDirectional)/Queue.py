class Queue:
	# [HEAD, ....... , TAIL]
	def __init__(self, data_list=None):
		self.data = list()
		self.size = 0
		if data_list is not None:
			self.data.extend(data_list)
			self.size = len(data_list)
    
	def enqueue(self, data_list):
		self.data.extend(data_list)
		self.size += len(data_list)

	def dequeue(self):
		if self.size == 0:
			return None
		self.size -= 1
		return self.data.pop(0)

	def get_contents(self):
		return self.data

	def is_empty(self):
		return self.size==0