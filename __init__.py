from distutils.log import debug


def Error(Type, Message, Debug, Code):
    if Debug == True:
        print("Remember to set the debug variable to False when you're done debugging! Also, check out the documentation for more information.")
        print("Type: " + Type)
        print("Message: " + Message)
        print("Code: " + Code)
    try:
        if Code == 0:
            print("Error: " + Message)
        elif Code > 0:
            print("Error Code: " + str(Code) + "" + str(Type) + " " + str(Message))
    except:
        if debug == True:
            print("An error occurred while trying to print the error message. Please check the documentation at https://patric-k-k.github.io/DOC/Error_handle.html for more information.")
        elif debug == False:
            print("Error: " + "Faled to print error message. Please contact the developer(s).")