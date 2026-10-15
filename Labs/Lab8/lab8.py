import math

def driver():
    '''Running a function to evaluate a line given a two points and a point.'''
    x_0,x_1 = 0,1
    y_0,y_1 = math.exp(x_0),math.exp(x_1) #Just test points
    alpha = 0.5
    y_alpha = eval_line(x_0,x_1,y_0,y_1,alpha)
    print('y_alpha = ',y_alpha)

def eval_line(x_0,x_1,y_0,y_1,alpha):
    '''evaluate the line at the point alpha given the two points (x_0,y_0) and (x_1,y_1)'''
    m = (y_1-y_0)/(x_1-x_0)
    b = y_0 - m*x_0
    y_alpha = m*alpha + b
    return y_alpha

if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()          