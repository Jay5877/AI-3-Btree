-> Name : Jay Shah

-> UTA ID : 1002070971

-> Programming language used : Python 3.10.7

-> Structure of my code: 
   	My entire code is in a single File named bnet.py
	Intially I have wrote code to read the data file and store it in a variable.
	Then I have divided my code in 3 different sections according to the specific tasks in the assignment. 
	
	1st section is for intialization of counters and forwarding that is the calculations for binary tree values.
	 Once values are determined for the tree, it then prints off all the values in a particular manner and print 
	 functions are the end of section 1.
	
	2nd section contains a function to find any probability in the JPD of the given data. Underneath the function to 
	 calculate the values is the code to take input and pass in the right format to the function we wrote earlier. 
	 At the end of this section it will print the probability of the sceanario in the input.
	 
	3rd section is of similar structure as the 2nd, there is a function at first which is used to find the probability
	 that we will be using in the inference by enumeration process. Ater the function to calculate enumeration, there is 
	 a code to intialize the query and evidence variables lists. Following is the code to read the inputs and apply the 
	 inference function on the inputs to calculate the conditional probability.

-> How to run my code:
	My (.py) file is in zip folder so You need to extract it. Now wherever you extract it
	make sure, that while running the file in CMD pr any terminal the path is set to the location
	where the .py file is.  
	You can call my function using the filename :- bnet.py
	followed by the name of the file containing the data.
	My code is designed to take inputs of events with only 4 parameters(BGCF) in a binary class manner.

	For task 1:
	So in order to just get the values of JPD you only need to pass 2 arguements which would be name of the 
	Python file followed by the name of file containing testing data.

	Command line arguement for testing task 1 - 
	bnet.py <training_data>
		Where <training_data> should be a text file with training data.
	

	For task 2:
	Running my code for getting the probability of any given condition you need to follow the below given format.
	 Please make sure that when passing in the values for the condition, the first character should be capital and should 
	 be out of {B,G,C,F} and also it takes input in the same pattern.

	Command line arguement for testing task 2 - 
	bnet.py <training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>
		Where <training_data> should be a text file with training data.
		Bt if B is true, Bf if B is false
		Gt if G is true, Gf if G is false
		Ct if C is true, Cf if C is false
		Ft if F is true, Ff if F is false
	
	For task 3:
	Running my code for getting the probability of any given condition you need to follow the below given format.
	 Please make sure that when passing in the values for the condition, the first one should be capital and should
	 out of {B,G,C,F} and also it takes input in the same pattern. Please use "given" in front of evidence variables
	 and make sure to pass an space in between of "given" and query variable.
	 NOTE - For query variables and evidence variables you need to pass values which are seperated by the ",".
	 Also make sure that there is no space in between of variables for either of the lists.

	Command line arguement for testing task 3 - 
	bnet.py <training_data> <query variable values> given <evidence variable values>
		where <training_data> text file with training data.
		Values of Query Variable seperated by "," but without any space in between [Format is same as in Task 2]
		Values of Evidence Variable seperated by "," but without any space in between (if any) [Format is same as in Task 2]

Thank you!