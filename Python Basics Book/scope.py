x = 5 #globaly set var
y = 2 #globaly set y
#total = 0
def outer_func():
    y = 3 # overwrite in the enclosed scope of the funtion but not to
    # the global scope of the program so it will be used in inner_func as 3 
    # and then go back to y = 2 for the rest of your program

    def inner_func():
        #add global here
        #total = total+x
        z = x + y # getting x from global var it first looks in the local scope 
        # and when i doesnt find x it moves to the global scope and finds x
        return z

    return inner_func() # this is actully a part of the outer_func

print(outer_func())
print(y)
# If you try to use total like it is commented out in the program the you will 
# get a UnboundLocalError: local variable 'total' referenced before assignment.
# To fix this you will have to add 'global total' in the local scope because 
# you are trying to reset total in the funtion and since you dont have a unique 
# assigment like with z python wont associte the global total you set at the 
# begging of the program. Though this is a fix do remeber that using global is
# bad programming form most likely you can fix this with another soluition like 
# j = total+x 