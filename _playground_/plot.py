import matplotlib.pyplot as plt
year = [1950,1970,1990,2010]
pop = [2.519, 3.692, 5.263, 6.972]

# add data
year = [1800,1850,1900] + year
pop = [1.0,1.262,1.650] + pop
plt.plot(year,pop)
plt.scatter(year,pop)

xlab = 'Year'
plt.xlabel(xlab)
# plt.xticks([_y for _y in range(min(year), max(year), (max(year) - min(year))//len(year))])
ylab = 'Poulation (billion)'
plt.ylabel(ylab)
plt.yticks(
    [_x for _x in pop],
    [str(_x) for _x in pop])

title = 'Word Polulation Projections'
plt.title(title)

plt.show()
