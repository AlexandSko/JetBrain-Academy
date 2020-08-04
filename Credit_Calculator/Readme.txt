Credit Calculator



__________________________________________________________________________________________________________

About


Finance is an important part of the life of any people.

Sometimes you think about getting additional income and want to open a deposit account.

And sometimes you need additional money right now and want to take a credit or mortgage.

Anyway, you may want to calculate different financial indicators to make a decision.

Let’s make such an instrument that can help us.

__________________________________________________________________________________________________________


Description


Let's compute all the parameters of the credit.

There are at least two kinds of credit loans: 

	1) those with annuity payment 

		      and 

	2) those with differentiated payment.

-----------------------------------------------------------------------------------------------------------
1) The annuity payment is fixed during the whole credit term.

   Here is the formula:
-----------------------------------------------------------------------------------------------------------
Annuity payment:

                            
                                     n
                        i  *  (1 + i) 
A                = P * ---------------
 ordinary_annuity              n
                        (1 + i)  -  1
	
 

Where:

A = annuity payment;

P = credit principal;

i = nominal (monthly) interest rate.

    Usually, it’s 1/12 of the annual interest rate, and usually,
    
    it’s a floating value, not a percentage.
    
    For example, if your annual interest rate = 12%, then i = 0.01;

n = number of payments. Usually, it’s the number of months.

You are interested in four values: 

	- the number of periods to repay the credit loan,
 
	- the monthly payment,

	- the credit principal,

	- the credit interest.

Each of these values can be calculated if the others are known:




Credit principal:


           A
P = ------------------	
    (              n )
    ( i  *  (1 + i)  )
    (--------------- )
    (        n       ) 
    ( (1 + i)  -  1  )



A number of payments:


             (    A      )
n = log      (-----------)
       (1+i) ( A - i * P )



--------------------------------------------------------------------------------------------------------------
2) Differentiated payment. 

      This is a kind of payment where the part for reducing the credit principal is constant.

   Another part of the payment is for interest repayment and it reduces during the credit term.

   It means that the payment is different every month. Let’s look at the formula:
---------------------------------------------------------------------------------------------------------------
Differentiated payment:



       P              P * (m - 1)    
D =   --- + i * (P -  ------------ )
 m     n                   n



Where:

D = mth differentiated payment;
 m

P = credit principal;

i = nominal interest rate. Usually, it’s 1/12 of the annual interest rate, and usually,

    it’s a floating value, not a percentage.
    
    For example, if our annual interest rate = 12%, then i = 0.01;

n = number of payments (months);

m = current period.



_______________________________________________________________________________________________________________

Suppose you used to run your credit calculator via a command line like this:

_______________________________________________________________________________________________________________


>>>  python credit_calc.py

_______________________________________________________________________________________________________________


Using command-line arguments, you can run your program this way:

_______________________________________________________________________________________________________________


>>>  python credit_calc.py --type=diff --principal=1000000 --periods=10 --interest=10

_______________________________________________________________________________________________________________

In that case, your program can get different values without asking the user to input them.

It can be useful when you are developing your program and trying to find a mistake,

so you run the program again and again with the same parameters.

Also, it's convenient if you made a mistake in a single parameter.

You don't have to input all other values again.

################################################################################################################



The program is supposed to work from the command line and parse the following parameters:


	--type, which indicates the type of payment: "annuity" or "diff" (differentiated).
		If --type is specified neither as "annuity" nor as "diff",
		or not specified at all, show the error message.

_______________________________________________________________________________________________________________


>>> python credit_calc.py --principal=1000000 --periods=60 --interest=10

Incorrect parameters

_______________________________________________________________________________________________________________

	--payment, which refers to the monthly payment.
		   
                   For --type=diff, the payment is different each month,
		   so we cannot calculate a number of periods or the principal,
		   therefore, its combination with --payment is invalid, too:

_______________________________________________________________________________________________________________


>>> python credit_calc.py --type=diff --principal=1000000 --interest=10 --payment=100000

Incorrect parameters

_______________________________________________________________________________________________________________

	--principal is used for calculating both types of payment.
		    You can get its value knowing the interest,
		    the annuity payment, and the number of periods.

	--periods   parameter denotes the number of months and/or years needed to repay the credit.
		    It's calculated based on the interest, annuity payment, and the principal.

	--interest  is specified without the percentage sign.
   		    Note that it may accept a floating-point value.
		    Our credit calculator can't calculate the interest,
		    so these parameters are incorrect:

_______________________________________________________________________________________________________________

>>> python credit_calc.py --type=annuity --principal=100000 --payment=10400 --periods=8

Incorrect parameters

_______________________________________________________________________________________________________________

You might have noticed that for differentiated payments you need 4 out of 5 parameters (excluding payment),

and the same is true for annuity payments (missing either a number of periods, the payment, or the principal).

Thus, when less than four parameters are given, the program will display the error message:

_______________________________________________________________________________________________________________


>>> python credit_calc.py --type=annuity --principal=1000000 --payment=104000

Incorrect parameters

_______________________________________________________________________________________________________________

Another case when the program will output this message is with negative values. We can't work with these!

_______________________________________________________________________________________________________________


>>> python credit_calc.py --type=diff --principal=30000 --periods=-14 --interest=10

Incorrect parameters

_______________________________________________________________________________________________________________

Finally, the program computes the value of overpayment, and we have our real functional credit calculator!



































