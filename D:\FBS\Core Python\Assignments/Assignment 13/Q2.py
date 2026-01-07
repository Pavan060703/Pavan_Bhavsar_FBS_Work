# Python Program to concatenate two dictionaries into one
def concatenate_dictionary(dict1,dict2):
    result={}
    for key in dict1:
        result[key]=dict1[key]

    for key in dict2:
        result[key]=dict2[key]

    return result

dict1={1:"Python",2:"Java",3:"C++",4:"C"}
dict2={5:"MySQL",6:"DotNet"}
concatenate_dict=concatenate_dictionary(dict1,dict2)
print("Concatenate Dictionary is ",concatenate_dict)