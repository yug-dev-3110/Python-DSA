**DSA (Data Structure & Alogorithms)**

# data => information
# structure => data ko store karne ka tarika
    - data ko ham multiple ways me store kar sakte hai like array, linked list, queue - (ex of non-linear structure) & tree, graph - (ex of linear structure)

# algorithm => set of instructions
    - suppose there are two softwares
        - dono ko banane ka tarika alag ho sskta hai, steps alag ho sakte hai
 
------------------------------------------------------------------------------------------------------------------

=> agar apko dono me se koi ek software ko choose karna ho to , jo sabse jaldi kam karke de usko hi choose karoge
# hame dono ko compare kar sakte hai through time complexity
    - time complexity is not depended on no. of lines of code
    - by looking at your watch and compare

------------------------------------------------------------------------------------------------------------------

**Time Complexity**

=> basic knowledge :
    - suppose, app ne do cheeze purchase kari, 1. car & 2. cycle
    - agar aapka dost ka call aya ki kya kharidne aye ho to aapka reply kya hoga, of course car !

    - suppose, apne kisi ko 1 lakh 10 ruppes /- udhar diye , which will be better to speak :
        1. mene 1 lakh 10 ruppes udhar diye ❌ or
        2. mene 1 lakh ruppes udhar diye ✅

--------------------------------------------------------------------------------------------------------------------

*Comparison*

- time complexity nikalne ke liye , jab ham comparison kar rahe hote hai to hame kuch chizzo ka pata hona chahiye
=> ex.
    👉 1 < loglog n < log n < n < n^2 < n^3 < ....... < 2^n
            - (if n is very very large)
- jiski time coplexity jyada kam hogi wo achha hoga and jiski jyada hogi usko ignore kar denge

----------------------------------------------------------------------------------------------------------------------

// time complexity nikalenge kese ?
- for that , jo bhi aapne program banaya hai uski ek methematical equation bana lenge

# EX.
    1. constant eq. : y = 5 
    2. linear func. : y = 2x + 5
    3. quedratic func.: y = 2x² + 3x - 5
    4. logarithmic eq. : y = log x + 2
    5. exponential func: y = 3ⁿ + 3

- agar aapne kisi ko 1 lakh 10 ruppes diye to usme 1 lakh is more dominating term

== constant func ko ham **1** se denote karte hai
== 2x + 5 me agar x ki value ko increase karu to usme 5 koi bahut bada role play nahi kar raha
    - agar eq. me koi bhi contant hai jiska multiply , devide ... ho raha hai usko ignore kar sakte ho
    - to 2x + 5 me most dominating factor x hoga
    👆 - is tarah ki eq. ko linear growth kehte hai

== 2x² + 3x - 5 me most dominating factor x² hoga
== log x + 2 me log x
== 3ⁿ + 3 me 3ⁿ

---------------------------------------------------------------------------------------------------------------------

**Types Of Analysis**

- suppose, muje ghar banwana hai, to jisko bhi me tender dunga usko puchunga ki ghar ko banane me kitna time lagega
 - he can ans in t 3 ways :
    -> min 3 months
    -> max 1 year
    -> avg. 6 months

- same goes to software, agar aapne usko chhota input diya to jaldi kam karega and bada input diya to jyada time lele

---------------------------------------------------------------------------------------------------------------------

*Three Types Of Analysis*
1. best case - min kitna time lagega - Ω (omega notaion)
2. avg case - θ (theta notaion)
3. worst case - O (big o notaion) ⭐ - most of the time iska hi use hoga

----------------------------------------------------------------------------------------------------------------------

**Ex.**
- agar mene kisi software ki time complexity nikali , suppose it's n
    - agar uski best complexity n hai to me kahunga Ω(n)
    - agar uski avg complexity n logn hai to me kahunga θ(n logn)
    - agar uski worst complexity n² hai to me kahunga O(n²)

---------------------------------------------------------------------------------------------------------------------

**Let's Start**

# 1. Constant Time Complxity: 
    - sabse pehle kisi bhi program ki constant time complexity kab hoti hai
    - denote by O(1) (we are mostly intersted in worst case)

-> x = 5     = isko excute hone me 1 units of time lag raha hai
-> print(x)  = isko 1 units ==> total 2 units of time 

- agar program me koi loop nahi hai to wo constant unit lega , us case me es program ki time complexity O(1) kahenge

# 2. Linear Time Complexity:
    - agar aapke program ki time complexity y = 2n + 10 ati hai to us case me , time complexity "order of n O(n)" hogi
    - EX.
        x = 5          -|
        ----------     -| - iski time complexity O(1) hogi 
        ----------     -|

        for i in range(0,n): -|
            print(i)         -| - its depend on size of n (agar n ki value 5 hogi to 5 times chalega)
        
        - 👆 first line ko chalne me 1 unit lagega, then suppose baki ke code ko 1 unit, so 1+1+n+n = 2n + 2 = O(n)

# short : 
    x = 5                   -> starting ke code ko constant time lagega
    ---------
    for i in range(0,n):    -> loop n times chalega  -> overall compexity O(n) hogi cause n is the most dominating term
        print(i) 

# 3. Quadratic Time Complexity :
    - Ex. 
        n = 5                           -> 1 unit
        m = 10                          -> 1 unit

        for i in range(0,n):            -> n times = 5 times
            for j in range(0,m):        -> m times = 10 times
                print("hello world")    -> 50 times (n*m)
                                        => ≈ n² + 2 => O(n²)

# 4. Logarithm Time Complexity :
    - Ex.
        n = 10
        while (n >= 1):    # suppose loop k times chala so = O(k) = O(logn)
            print("hello") 
            n = n//2
    - 👆 - loop n/2¹, n/2², n/2³.....n/2^k
    - jab n/2^k ki value 1 hogi tab loop end hoga
    - so n/2^k = 1  ==> n = 2^k ==> logn = k log2 ==> k = log₂n

-----------------------------------------------------------------------------------------

**Que.**

n = 10
print(n)

for i in range(0,n):
    print("hello")
for j in range(0,n):
    for k in range(0,n):
        print("world")
while (n >= 1):
    print("while loop")
    n = n//2

-> first two lines = (1)
-> first loop = O(n)        over all time complexity :
-> nested loop = O(n²)       O(1) < O(logn) < O(n) < O(n²)
-> while loop = O(logn)      - it will be O(n²)