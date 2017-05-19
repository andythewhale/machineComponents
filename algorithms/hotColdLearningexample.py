#Hot/Cold learning example.
#This is just a code example for showing how learning works.
#It is insanely inefficient.


import numpy as np

#These are our variables
#Only our weight will change, our input will not... for this example.
weight = 0.5
input = 0.5
goal_prediction = 0.8

#This is our learning rate basically.
step_amount = 0.001

for iteration in range(1101):
	prediction = input * weight
	error = (prediction - goal_prediction) ** 2

	print('Error: ' + str(error) + ' ' + 'Prediction: ' + str(prediction))

	up_prediction = input * (weight + step_amount)
	up_error = (goal_prediction - up_prediction) ** 2

	down_prediction = input * (weight + step_amount)
	down_error = (goal_prediction - down_prediction) ** 2

	#If our weight is too high we decrease it.
	if(down_error < up_error):
		weight = weight - step_amount

	#If our weight is too low we increase it.
	if(down error > up_error):
		weight = weight + step amount

#Keep in mind this is drastically oversimplified.
#It doesn't generalize.
#The inputs don't change.
#There's literally only one type of thing being optimized.
#But, the concept is there and its a good foundation to expand on.

