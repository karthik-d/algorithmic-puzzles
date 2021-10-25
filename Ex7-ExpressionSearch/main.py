import BreadthFirstSearch as BFS 

operand_space = list(map(int, input("Enter Operands as space-separated Integers\n").split()))
target_val = int(input("Enter Target Expression Value: "))

result_tree = BFS.search(operand_space, target_val)
# Display result
if result_tree.evaluation==target_val:
	print("Exact expression found")
else:
	print("Nearest expression found. Expression result:", result_tree.evaluation)
result_tree.display()
print()