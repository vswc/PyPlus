"""
*args can take multiple values.
**kwargs can take multiple values and assigns them a keyword.

You will also learn about unpacking in python.

Below is an example of both being used.
"""

def args_function(*args):
    # Creating a list out of the given arguments.
    mylist = list(args)

    for item in mylist:
        print(item)

           #  argument, argument.
args_function("*args", "are", "quite", "handy")

print("\n")

def kwarg_function(**kwargs):
    # Creating a dictionary out of the given arguments.
    mydict = dict(kwargs)
    
    for item, value in mydict.items():
        print(item, value)
            #  keyword=argument, keyword=argument.
kwarg_function(name="vsw", age=18)

"""
Anything I missed? Let me know.
@vsw on discord.
"""