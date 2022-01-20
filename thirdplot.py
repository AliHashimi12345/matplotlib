from matplotlib import pyplot as plt
 
x = [5,2,7]
y = [2,16,4]
plt.plot(x,y)
plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

import matplotlib.pyplot as plt
  
  
a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
plt.plot(a)
  
# o is for circles and r is 
# for red
plt.plot(b, "or")
  
plt.plot(list(range(0, 22, 3)))
  
# naming the x-axis
plt.xlabel('Day ->')
  
# naming the y-axis
plt.ylabel('Temp ->')
  
c = [4, 2, 6, 8, 3, 20, 13, 15]
plt.plot(c, label = '4th Rep')
  
# get current axes command
ax = plt.gca()
  
# get command over the individual
# boundary line of the graph body
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
  

# the left boundary line to fixed range
ax.spines['left'].set_bounds(-3, 40)
  
 
# the x-axis set the marks
plt.xticks(list(range(-3, 10)))
  

plt.yticks(list(range(-3, 20, 3)))
  
# legend denotes that what color 

ax.legend(['1st Rep', '2nd Rep', '3rd Rep', '4th Rep'])
  
plt.annotate('Temperature V / s Days', xy = (1.01, -2.15))
  
# gives a title to the Graph
plt.title('All Features Discussed')
  
plt.show()
