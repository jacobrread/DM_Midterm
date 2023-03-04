# Midterm

## Problem 1
To run this set the first parameter of the run function on line 154 to either "50" or "20". This represents the rejection percentage and its affiliated modifications in the code. Then simply run the Problem1.py file. 

### For just 50% chance of accepting the job:
I ran 10000 experiments and got 31% stopping point and 27% stopping point
I ran 100000 experiments and got 34% stopping point

 How does this compare with the simple early-stopping problem?
 - The curve flattens out more

### For 20% and increasing chance of not accepting the job
I ran 10000 experiments and got the following:
- Optimal Search Threshold: 30.0%
- Optimal Answer: 859

I did it again and got the following:
- Optimal Search Threshold: 30.0%
- Optimal Answer: 227

When I ran 100000 experiments I got the following:
- Optimal Search Threshold: 35.0%
- Optimal Answer: 592.757226505516

Optimal Search Threshold: 34.0%
Optimal Answer: 968.1729270627526

Optimal Search Threshold: 35.0%
Optimal Answer: 560.6912085494506


### What is the early stopping rule that maximizes the likelihood of obtaining the optimal answer for 100 total candidates?
- Oddly enough it seems like the early stopping rule is around 34 or 35%. In my head I expected to to be more than the vanilla stopping problem rule, but I guess I was wrong.

### Use a random uniform draw from [1, 1000] for this exercise. How does this compare with the simple early-stopping problem?
- Well the vanilla early stopping problem supposedly is around 37% but it was less with the modifications Dr. Mario suggested. I am curious to talk about this in class after this midterm has been turned in so I can hear what he has to say about why this is. 


## Problem 2
The file runs both of the scenarios (with and without area0) at the bottom of the Problem2.py file. Because of this all you have to do to run my code is run the Problem2.py file. 

### Without Baseline Sensor
How many days will it take for you to make the decision to place the permanent sensor?
- Based on multiple runs of Problem2.py is seems that it takes somewhere between 20 and 30 days 

Also, state the area that you select as the optimum.
- Area1 was the selected optimum area.

### With Baseline Sensor
Does this change the final decision of placement?
- Yes, the algorithm wants to choose area0 which I feel like is not what Dr. Mario is searching for. However, 
I don't know what to do to fix this issue

How long does it take before you choose to place the sensor?
- It is clear that area0 is the primary sensor very quickly. After four or five days it is clear that area0 is 
the only one being chosen. If you look at the results graph it will show that it was rare for another area to be chosen.



## Problem 3
First change the boolean value on line 87 to True of you want to change the volatility at 5 years to 19%. Otherwise set that boolean value to False. Then simply run the Problem3.py file.

### What is the value to us of a lease-to-own contract that lets us immediately sell the leased property at any time as if we owned it (American Option or Mortgage)? 
- Using an american option allows us to sell at any point in time during the 10 years. If the market was good and the price of the option was higher than the desired selling price ($535,000) then we would want to sell right there and then. Technically we still have the option to wait and see if the price keeps climbing, but that is a risk that does not have to be taken. 

### How does this compare to a standard Lease to Own (European Option)? 
- If we were using a european style option then we wouldn't have that ability and instead would have to wait until the end of the 10 years. Whatever the value is at the end of the ten years is what we get regardless of if it is the desired selling price or not.

### Test a situation if the market has a surge in volatility at year 5 and onward of 19%, how do these prices change?
- The volatility increase results in more changes to the cost. As a result the prices seem to get more extreme on either end of the spectrum. In other words, the highest values seem to be higher and the lowest values seem to be lower.


## Problem 4

### As this is the first time I have taught this topic, I could really use help in
understanding how to improve the course. What is making sense, and what doesn’t?
How can I do this better? 

I think this course has a lot of potential. Where it is lacking, in my opinion, is in the early stages 
of learning a new topic. I never felt confident, and honestly still don't, with the monte carlo or epsilon
greedy algorithms. Maybe I am slow to pick up on this, but I felt like we went over it and coded it up once
(which by the way was helpful) and then just assumed it was understood after that. If you payed me to go and 
code up a simple implementation of these algorithms without existing code or google I wouldn't be able to do
it. 

On a different note, a document containing all the various financial terms mentioned would be extremely helpful.
I realize that we can google terms and while that is true I find it very helpful to get the specific teacher's 
definition of a term since they are the ones using it frequently. I would LOVE to understand all of the financial
topics we have talked about better, and I wish I had heard of them before this class, but the reality is that I 
had never heard of most of them. In short, a document that we could refer to for help with would be greatly
appreciated.