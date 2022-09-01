from housing.logger import logging

logging.info("Enter any number integers as argument")
input_lst = [20,30,40,10]

for i in input_lst:
    logging.info("The user input is: "+str(i))

logging.info("Number of inputs: "+str(len(input_lst)))
result = sum(input_lst)
logging.info("The sum is: "+str(result))   
print (result) 