#dimensions and shapes
#shape = structure of array e.g.(3,2,2)
#dimensions = num of different sets/groups e.g. (12,5,20,20) has 4 dimensions
import numpy
numpy_array = numpy.array(0) # ()
print(numpy_array,'=', numpy_array.shape) 

numpy_array = numpy.array([0]) #(1,)
print(numpy_array,'=', numpy_array.shape)

numpy_array = numpy.array([['hello'],[1],[2.77]]) #(3,1)
print(numpy_array,'=', numpy_array.shape)

numpy_array = numpy.array([[[0],[0]],[[1],[1]],[[2],[2]]]) #(3,2,1)
print(numpy_array,'=', numpy_array.shape)

numpy_array = numpy.array([[[0,0],[0,0]],[[1,0],[1,0]],[[2,0],[2,0]]]) #(3,2,2)
print(numpy_array,'=', numpy_array.shape)

numpy_array = numpy.array([[[0],[0],[0],[0]],[[1],[0],[1],[0]],[[2],[0],[2],[0]]]) #(3,4,1)
print(numpy_array,'=', numpy_array.shape)

