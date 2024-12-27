def div(num1,num2):
    return(num1,num2)
try:
    num1=int(input("enter num1"))
    num2=int(input("enter num2"))
    result=(num1/num2)
    print(result)
    print(name)
except ZeroDivisionError as zero_error:
    print("division zero error",str(zero_error))
except ValueError as value_error:
    print("value error"),str(value_error)
except Exception as error:
    print("error",str(error))
