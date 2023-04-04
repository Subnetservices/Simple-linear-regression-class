# A module that calculates Linear regression, using Y = MX + C
#Module uses standard algorithm, might be modified for efficiency on a later date, IDK.
#21-Jan-2023, A Boredom project

#Regression object

class regr:
    def __init__(self):
#First we create the lists we need
# 'a' represents mean of X, while 'b' represents mean of Y.
# 's' = sum(x - a), 'u' = sum(x-a)^2, 'p' = sum(y-b)
        self.x = []
        self.y = []
        

#attribute to add values to list X
#We need attribute to be able to read a custom list
#from user input, to make it a more general adaptable solution
    
    def avg_x(self):
        
 #Find the average of X
 #Declare 'a' global so it can be used outside of its home function
        global a
        global w
        w = self.x
        a = sum(w)/len(w)
        print('Average of col X=' , a)
        return a

    def avg_y(self):
# Find the average of Y
#Declare 'b' global so it can be used outside of its home function
       global e
       e = self.y
       global b
       b = sum(e)/len(e)
       print('Average of Col Y=' ,b)
       return b

#Next we create an attribute that populates list s = (x-a),
#as our first step in solving for our slope M.
    def sum_x(self):

        global s
        global u

             
        n = len(w)
        s=0
        u = 0
        for i in range(n):
            s +=  (w[i] - a)
            u += (w[i] - a)**2
            i = i + 1
             
            print ('sum(x-mean(x)=' , s)
            print ( 'Sum (x-mean(x))^2 =' , u)
            return s, u
        
#Next we create an attribute that populates list p = (y-b),
#as our first step in solving for our slope M.
    def sum_y(self):
        
        global p
        
        l = len(self.y)
        p=0
       
        for i in range( l):
            p += (self.y[i] - b)
            i = i + 1
           
            print ('sum(y-mean(y)=' , p)
            
            return p
        

    def slope(self):
        # We find the slope M: formular = s*p/u

        global m

        m = (s*p)/u
        print('Slope m =', m)
        return m

    def intercept_(self):

        # We find the intercept, c.
        # to find the intercept, we multiply our slope 'm' by the average of x 'a'
        #We then subtract this result from the average of y 'b'
        global c
        c = b - (a * m)
        print ('Intercept c:', c)
        return c

    def pred(self):

        #We're so close to the end, but first, we want to make some predictions ourselves.
        #We'll take our list X, and using Y=MX + C, we'll make some predictions of our own for Y.
        # We'll then display the list for Y provided, so the user can see the difference.

        global z

        z = []

        n = len(self.x)
        

        for i in range(n):

            y1 = ((m * self.x[i]) + c)

            z.append (y1)

            i = i + 1

            print('X:', self.x)
            print ('Y_pred:', z)
            print('Y:', self.y)
            
            return z

        

        
        

    
        

    



    
