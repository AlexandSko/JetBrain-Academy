Credit Calculator



_________________________________________________________________________________________

About


Finance is an important part of the life of any people.

Sometimes you think about getting additional income and want to open a deposit account.

And sometimes you need additional money right now and want to take a credit or mortgage.

Anyway, you may want to calculate different financial indicators to make a decision.

Let’s make such an instrument that can help us.
_________________________________________________________________________________________


Description


Let's compute all the parameters of the credit.

There are at least two kinds of credit loans: those with annuity payment and those with differentiated payment.

The annuity payment is fixed during the whole credit term.

Here is the formula:
--------------------------------------------------------------------------------------------
Annuity payment:



A_{ordinary\_annuity} = P * \dfrac{i * (1+i)^n}{(1+i)^n-1}A 
ordinary_annuity
?	
 =P? 
(1+i) 
n
 ?1
i?(1+i) 
n
 
?	
 

Where:

A = annuity payment;

P = credit principal;

i = nominal (monthly) interest rate. Usually, it’s 1/12 of the annual interest rate, and usually,

it’s a floating value, not a percentage. For example, if your annual interest rate = 12%, then i = 0.01;

n = number of payments. Usually, it’s the number of months.

You are interested in four values: the number of periods to repay the credit loan, the monthly payment, the credit principal, and the credit interest.

Each of these values can be calculated if the others are known:




Credit principal:

P = \dfrac{A}{\left( \dfrac{i * (1+i)^n}{(1+i)^n-1} \right)}P= 
( 
(1+i) 
n
 ?1
i?(1+i) 
n
 
?	
 )
A
?	
 


A number of payments:

n = \log_{1+i} \left( \dfrac{A}{A - i*P} \right)n=log 
1+i
?	
 ( 
A?i?P
A)
?



--------------------------------------------------------------------------------------------
Differentiated payment. 

This is a kind of payment where the part for reducing the credit principal is constant.

Another part of the payment is for interest repayment and it reduces during the credit term.

It means that the payment is different every month. Let’s look at the formula:
--------------------------------------------------------------------------------------------
Differentiated payment:



D_m = \dfrac{P}{n} + i * \left( P - \dfrac{P*(m-1)}{n} \right)D 
m
?	
 = 
n
P
?	
 +i?(P? 
n
P?(m?1)
?	
 )




Where:

D_mD 
m
?	
  = mth differentiated payment;

P = credit principal;

i = nominal interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage. For example, if our annual interest rate = 12%, then i = 0.01;

n = number of payments (months);

m = current period.



______________________________________________________________________________________________
Suppose you used to run your credit calculator via a command line like this:

______________________________________________________________________________________________

python credit_calc.py
______________________________________________________________________________________________

Using command-line arguments, you can run your program this way:

______________________________________________________________________________________________

python credit_calc.py --type=diff --principal=1000000 --periods=10 --interest=10

______________________________________________________________________________________________

In that case, your program can get different values without asking the user to input them.

It can be useful when you are developing your program and trying to find a mistake, so you run the program again and again with the same parameters.

Also, it's convenient if you made a mistake in a single parameter. You don't have to input all other values again.








































