import matplotlib.pyplot as plt
import numpy as np

# we define row to be genes, column to be samples

number_of_genes = 6
number_of_samples = 3

#########################
## draw grid here
print float(1/(number_of_genes))

xgrid = np.arange(0, 1, (1.0/(number_of_samples)) )
ygrid = np.arange(0, 1, (1.0/(number_of_genes)) )

for i in range(len(xgrid)):

	# plot grid here

	#print  xgrid[i], yspace, ":",xgrid[i],1-yspace

	plt.axvline(xgrid[i],0,1, color = "lightgrey")

for i in range(len(ygrid)):
	plt.axhline(ygrid[i],0,1, color = "lightgrey")


# add last vertical and horizential lines here
plt.axvline(1,0,1, color = "lightgrey")
plt.axhline(1,0,1, color = "lightgrey")


##########################
## add labels here

# set labels here
y_labs = ['a', 'b', 'c', 'd',"e","f"]
x_labs = ["1",'2','3']

plt.yticks(ygrid+(1.0/(number_of_genes)/2), y_labs)
plt.xticks(xgrid+(1.0/(number_of_samples)/2), x_labs)


##### 

plt.show()