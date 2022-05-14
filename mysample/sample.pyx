import numpy as np
cimport numpy as np

cdef extern from "sample.h":
    cdef cppclass __Sample:
        __Sample() except +
        void hello()

cdef class Sample:
    cdef __Sample __sample

    def __cinit__(self):
        self.__sample = __Sample()

    def hello(self):
        self.__sample.hello()

    def sum(self, np.ndarray a):
        return a.sum()
