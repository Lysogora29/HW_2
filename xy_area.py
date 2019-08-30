axis_x = input('set poin x axis : ')
axis_x = int(axis_x)
axis_y = input ('set poin y axis : ')
axis_y = int(axis_y)
if axis_x > 0 and axis_y > 0:
    print (' Ferst part')
elif axis_x > 0 and axis_y < 0:
    print (' Second part')
elif axis_x < 0 and axis_y < 0:
    print (' Third part')
elif axis_x < 0 and axis_y > 0:
    print (' Fourth part')
elif axis_x == 0 and axis_y == 0:
    print (' Centre of area')
else:
    print ('It is axis line')
