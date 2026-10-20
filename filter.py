def check_even_number(number):
	if number % 2 == 0:
	    return True
	else:
	    return False
	    
	    
even_number_list = list(filter(check_even_number,range(1,21)))

print (even_number_list)

def words_longer_than_5(word):
    return len(word) > 5
        
list_of_words_with_more_than_5_characters = list( filter(words_longer_than_5,['cat','elephant','tiger','lion']))

print(list_of_words_with_more_than_5_characters)


def tuple_in_list(collection):
    return collection[0] > 2
           
            
tuple_with_first_value_greater_than_2 = list(filter(tuple_in_list,[(1,'A'),(4,'B'),(2,'C')]))
print(tuple_with_first_value_greater_than_2)


def check_number_divisible_by_3_and_5(number):
    return number% 3 == 0 and number% 5 == 0
    
number_divisible_by_3_and_5 = list(filter(number_divisible_by_3_and_5_checker,range(1,51)))
print(number_divisible_by_3_and_5)



def palindrome(word):
    return word == word[::-1]
    
result = list(filter(palindrome,['level','world','madam','python']))
print(result)
    
