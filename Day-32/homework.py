input_string = "goa is the best"


result_string = ""


for i in range(len(input_string)):
    
    if input_string[i] != " ":
      
        result_string += input_string[i]


print(result_string)