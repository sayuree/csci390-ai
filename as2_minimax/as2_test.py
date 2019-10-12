#Test file
from as2_mnx import MNX
def main():
	data_list=['A', ['B', ('E', 3), ('F', 12),('G', 2)], ['C', ('H', 6), ('I', 8),('J', 9)],['D', ('K', 4), ('L', 5),('M', 3)]]

	mnm=MNX(data_list);

	res=mnm.minimax();
	
    #Test the result
	print (res.value)#should be 3
	print (res.solution);#should be ['A', 'B', 'E']

	
if __name__ == "__main__":
	main()
	 
