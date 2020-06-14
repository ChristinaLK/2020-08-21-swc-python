> ## Exercise: Explore Slicing
> 
> 1.  What does `thing[low:high]` do?
> 2.  What does `thing[low:]` (without a value after the colon) do?
> 3.  What does `thing[:high]` (without a value before the colon) do?
> 4.  What does `thing[:]` (just a colon) do?
> 5.  What does `thing[negative-number]` do? 
> 6.  What does `thing[number:some-negative-number]` do?
> 7.  What happens when you choose a `high` value which is out of range? (i.e., try `atom_name[0:15]`) 
> 8.  What does `thing[low:high:skip]` do?
>
> Once you've explored, load the following bit of code and try to 
> create a slice that prints out every fifth letter, starting from 
> the third letter and going to the end: 
> 
> %load 'code/encoded.py'
