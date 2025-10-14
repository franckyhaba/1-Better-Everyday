# colors = ['red','blue','green', 'black']
# for color in colors:
#        print(color.title())
# colors.append('orange')
# print()
# print( colors[3:6])


# colors = ['red','blue','green', 'black']

# print('Here are my favorite colors')
# for color in colors[:2]: 
#     print(color.title())


colors = ['red','blue','green', 'black']
secColors = colors[:]
#this would be considered as slicing 
colors.append('purple')
secColors.append('orange')

print('Here are my favorite colors')
print (colors)

print ()
print('Here are my second favorite colors')
print (secColors)
