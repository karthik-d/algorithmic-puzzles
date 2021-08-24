class PriorityQueue:
	# Stores elements (states) along with some payload associated with each of them 

	def __init__(self, priority_func):
		# 'contexts' contains the data required to resolve the priority of elements
		# 'priority' is a function that returns the sort key -> priority(elem, its_context)
		self.data = []
		self.contexts = []
		self.payloads = []
		self.priority = priority_func
		self.size = 0

	def sort_elements(self, elems, contexts, payloads):
		for i in range(1, len(elems)):
			j = i-1
			while j>=0 and self.priority(elems[j],contexts[j])>self.priority(elems[i],contexts[i]):
				elems[j] = elems[j-1]
				contexts[j] = contexts[j-1]
				payloads[j] = payloads[j-1]
				j -= 1
			elems[j+1] = elems[i]
			contexts[j+1] = contexts[i]
			payloads[j+1] = payloads[i]
		return elems, contexts, payloads

	def enqueue(self, elems, contexts, payloads):
		# 'contexts' contains the data required to resolve the priority of elements
		# The resolution is done using the 'priority_func' function
		# Sort the insertion elements 
		elems, contexts,payloads = self.sort_elements(elems, contexts, payloads)
		# Merge with current data
		data_i = 0
		elem_j = 0
		merged_data = []
		merged_contexts = []
		merged_payloads = []
		while data_i<self.size and elem_j<len(elems):
			if self.priority(self.data[data_i], self.contexts[data_i]) <= self.priority(elems[elem_j], contexts[elem_j]):
				merged_data.append(self.data[data_i])
				merged_contexts.append(self.contexts[data_i])
				merged_payloads.append(self.payloads[data_i])
				data_i += 1
			else:
				merged_data.append(elems[elem_j])
				merged_contexts.append(contexts[elem_j])
				merged_payloads.append(payloads[elem_j])
				elem_j += 1
		if data_i<self.size:
			merged_data.extend(self.data[data_i:])
			merged_contexts.extend(self.contexts[data_i:])
			merged_payloads.extend(self.payloads[data_i:])
		else:
			merged_data.extend(elems[elem_j:])
			merged_contexts.extend(contexts[elem_j:])
			merged_payloads.extend(payloads[elem_j:])
		# Update data and contexts
		self.data = merged_data
		self.contexts = merged_contexts
		self.payloads = merged_payloads
		self.size += len(elems)

	def dequeue(self):
		if self.is_empty():
			return None 
		self.size -= 1
		return self.data.pop(0), self.payloads.pop(0)
		
	def is_empty(self):
		return self.size==0
			
