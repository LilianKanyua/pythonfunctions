def my_country(country="Rwanda"):
    print(f"Hello from {country}")


def my_country(country="Rwanda"):
    print(f"Hello from {country}")

def greet(*names):
    for name in names:
        print(f"Hello {name} ")


def student_infor(** kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

# question one
def concatenate_args(*statements):
    added =" "
    for statement in statements:
        added+=statement
    print(added)
    
# question2
def concatenate_kwargs(**kwargs):
    single_string=" "
    for key,value in kwargs.items():
        single_string+= value
    print(single_string)