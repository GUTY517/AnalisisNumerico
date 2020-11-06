from sympy import *

class f_x():
    
    def __init__(self, function, g_function):
        self.function = function
        if(g_function):
            self.g_function = g_function


    def get_f_components(self, number):
        init_printing(use_unicode=True)
        x = symbols('x')
        error = 0
        try:
            print(self.function)
            fx = eval(self.function)
            function = fx.evalf(subs={x: number})
            dfx = Derivative(fx, x).doit()
            derivative = dfx.evalf(subs={x: number})
            dfx2 = Derivative(dfx, x).doit()
            second_derivate = dfx2.evalf(subs={x: number})
            return function, error, derivative, second_derivate
        except ValueError:
            error = 1
            print("Input error, please try again")
            return None, error, None, None
        except ZeroDivisionError:
            error = 2
            print("Zero Division Error")
            return None, error, None, None

    def get_g_components(self, number):
        init_printing(use_unicode=True)
        x = symbols('x')
        error = 0
        try:
            gx = eval(self.g_function)
            gfunc = gx.evalf(subs={x:number})
            return gfunc, error
        except ZeroDivisionError:
            error = 2
            print("Zero Division Error")
            return None, error
        except ValueError:
            error = 1
            print("Input error, please try again")
            return None, error



            