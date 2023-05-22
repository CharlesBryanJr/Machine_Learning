'''file_name'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=W0621
print(" ")

'''

Type of Question:
- math concept

Question:
A test indicating the presence of disease 
in cats 
is 95% accurate
in terms of both sensitivity and specificity. 

The prevalence of the disease is 3% 
which means only 3% of known cats have the disease. 

If your cat tests positive (negative) for the disease, 
what’s the probability that 
your cat has (doesn’t have) the disease?

Input:
- the accuracy of a test
- the percent of a population which has the diseas 

Clarifying Questions / Insights:
- sensitivity == specificity == accuracy
- You shouldn't use any libraries.
- automatically round output values to the 4th decimal.
	
- If I knew / had this....
	-

Output:
- given a positive test result,
what is the probability that an individual 
has the disease
- given a negative test result,
what is the probability that an individual 
does not have the disease
'''


# Time: O() | # Space: O()
def probability_of_disease(accuracy, prevalence):

    disease_test_inaccuracy = 1 - accuracy
    prob_sick = prevalence
    prob_healthy = 1 - prevalence

    prob_positive = (prob_sick * accuracy) + (prob_healthy * disease_test_inaccuracy)
    prob_negative = (prob_sick * disease_test_inaccuracy) + (prob_healthy * accuracy)

    prob_sick_given_postive = (prob_sick * accuracy) / prob_positive
    prob_healthy_given_negative = (prob_healthy * accuracy) / prob_negative

    return [prob_sick_given_postive*100, prob_healthy_given_negative*100]


accuracy = 0.95
prevalence = 0.03
print("accuracy:", accuracy)
print("prevalence:", prevalence)
print("probability_of_disease:", probability_of_disease(accuracy, prevalence))
print(" ")

accuracy = 0.85
prevalence = 0.1
print("accuracy:", accuracy)
print("prevalence:", prevalence)
print("probability_of_disease:", probability_of_disease(accuracy, prevalence))
print(" ")

accuracy = 0.45
prevalence = 0.5
print("accuracy:", accuracy)
print("prevalence:", prevalence)
print("probability_of_disease:", probability_of_disease(accuracy, prevalence))
print(" ")

# _recursion
# _iteration
print(" ")
