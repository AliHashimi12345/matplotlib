from matplotlib import pyplot as plt
  
#Plotting to our canvas
  
plt.plot([1,2,3],[4,5,1])
  
 #Showing what we plotted
  
plt.show()

import matplotlib.pyplot as plt
  
  
a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]
  
 
# want ans to be displayed
fig = plt.figure(figsize =(10, 10))
  
# creating multiple plots in a 
# single plot
sub1 = plt.subplot(2, 2, 1)
sub2 = plt.subplot(2, 2, 2)
sub3 = plt.subplot(2, 2, 3)
sub4 = plt.subplot(2, 2, 4)
  
sub1.plot(a, 'sb')
  
 
# x axis values advances by 1

sub1.set_xticks(list(range(0, 10, 1)))
sub1.set_title('1st Rep')
  
sub2.plot(b, 'or')
  
# sets how the display subplot x axis
# values advances by 2 within the
sub2.set_xticks(list(range(0, 10, 2)))
sub2.set_title('2nd Rep')
  
# can directly pass a list in the plot

sub3.plot(list(range(0, 22, 3)), 'vg')
sub3.set_xticks(list(range(0, 10, 1)))
sub3.set_title('3rd Rep')
  
sub4.plot(c, 'Dm')
  
sub4.set_yticks(list(range(0, 24, 2)))
sub4.set_title('4th Rep')
  
plt.show()