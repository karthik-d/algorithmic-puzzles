import time

import BFS as BFS 
import Bidirectional_BFS as BiBFS

time_ = time.time()
#print(BFS())
print(time.time()-time_)
time_ = time.time()
conn_state, f_parents, r_parents = BiBFS.search()
for state in BiBFS.deduce_path(conn_state, f_parents, r_parents):
	for row in state:
		print(row)
	print()
print(time.time()-time_)
			
