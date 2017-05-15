'''This is a skeleton for PCA
Andy Miller
5/14/2017'''
import numpy as np

mu_vec1 = np.array([0,0,0])
cov_mat1 = np.array([[1,0,0],[0,1,0],[0,0,1]])

class1_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, 20).T

print(class1_sample)


mu_vec1 = np.array([0,0,0])
cov_mat1 = np.array([[1,0,0],[0,1,0],[0,0,1]])

class2_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, 20).T

print(class2_sample)

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline
%pylab inline

#This is the width and height of the plot
fig = plt.figure(figsize =(8,8))

#3d subplot, these are are grid parameters, the add_subplot function turns it into a single integer.
ax = fig.add_subplot(111, projection = '3d')

#Fontsize
plt.rcParams['legend.fontsize'] = 10

#plot samples
ax.plot(class1_sample[0,:], class1_sample[1,:], class1_sample[2,:], 'o', markersize = 8, color = 'green', alpha = 0.666, label = 'class1')
ax.plot(class2_sample[0,:], class2_sample[1,:], class2_sample[2,:], '^', markersize = 8, color = 'red', alpha = 0.666, label = 'class2')

all_samples = np.concatenate((class1_sample, class2_sample), axis = 1)
all_samples

mean_x = np.mean(all_samples[0,:])
mean_y = np.mean(all_samples[1,:])
mean_z = np.mean(all_samples[2,:])

mean_vector = np. array([[mean_x], [mean_y], [mean_z]])
print(mean_vector)

cov_mat = np.cov([all_samples[0,:],all_samples[1,:],all_samples[2,:]])
print('Covariance Matrix:\n', cov_mat)

#Eigan Vectors and Eigan Values:
eig_val, eig_vec = np.linalg.eig(cov_mat)
print('eigan value: \n', eig_val)
print('-----------------------------------------')
print('eigan vector: \n', eig_vec)

#So now we just need to collect and sort these into eigain pairs...
#They need to be in tuple form. Not sure why, I forget.

eig_pairs = [(np.abs(eig_val[i]), eig_vec[:,i]) for i in range(len(eig_val))]

#Sorting
eig_pairs.sort()
eig_pairs.reverse()

#Confirming
for i in eig_pairs:
    print(i[0])

    #Now we pick out the k eigan pair values of the eigan vectors. 


matrix_w = np.hstack((eig_pairs[0][1].reshape(3,1), eig_pairs[1][1].reshape(3,1)))

print(matrix_w)

#Now we need to transform our data using this information
transformed_data = matrix_w.T.dot(all_samples)
print(transformed_data)
#Nonsense.

plt.plot(transformed_data[0,0:20], transformed_data[1,0:20],
         'o', markersize=7, color='green', alpha=0.5, label='class1')
plt.plot(transformed_data[0,20:40], transformed_data[1,20:40],
         '^', markersize=7, color='red', alpha=0.5, label='class2')
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.xlabel('x_values')
plt.ylabel('y_values')
plt.legend()
plt.title('Transformed samples with class labels')

plt.show()

#This should reduce a random 3d data set to a random 2d data set.
