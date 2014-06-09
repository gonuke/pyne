###################
###  WARNING!!! ###
###################
# This file has been autogenerated

# Cython imports
from cython.operator cimport dereference as deref
from cython.operator cimport preincrement as inc
from libcpp.string cimport string as std_string
from libcpp.utility cimport pair
from libcpp.map cimport map as cpp_map
from libcpp.set cimport set as cpp_set
from libcpp.vector cimport vector as cpp_vector
from libcpp cimport bool as cpp_bool
from libc cimport stdio
from cpython.version cimport PY_MAJOR_VERSION
from cpython.ref cimport PyTypeObject, Py_INCREF, Py_XDECREF

# Python Imports
cimport numpy as np

# Local imports
cimport extra_types

cimport numpy as np


# Cython Imports For Types
cimport extra_types
from libcpp.vector cimport vector as cpp_vector
from libcpp.string cimport string as std_string

# SetStr
cdef class _SetIterStr(object):
    cdef cpp_set[std_string].iterator * iter_now
    cdef cpp_set[std_string].iterator * iter_end
    cdef void init(_SetIterStr, cpp_set[std_string] *)

cdef class _SetStr:
    cdef cpp_set[std_string] * set_ptr
    cdef public bint _free_set




# SetInt
cdef class _SetIterInt(object):
    cdef cpp_set[int].iterator * iter_now
    cdef cpp_set[int].iterator * iter_end
    cdef void init(_SetIterInt, cpp_set[int] *)

cdef class _SetInt:
    cdef cpp_set[int] * set_ptr
    cdef public bint _free_set




# MapStrStr
cdef class _MapIterStrStr(object):
    cdef cpp_map[std_string, std_string].iterator * iter_now
    cdef cpp_map[std_string, std_string].iterator * iter_end
    cdef void init(_MapIterStrStr, cpp_map[std_string, std_string] *)

cdef class _MapStrStr:
    cdef cpp_map[std_string, std_string] * map_ptr
    cdef public bint _free_map




# MapStrInt
cdef class _MapIterStrInt(object):
    cdef cpp_map[std_string, int].iterator * iter_now
    cdef cpp_map[std_string, int].iterator * iter_end
    cdef void init(_MapIterStrInt, cpp_map[std_string, int] *)

cdef class _MapStrInt:
    cdef cpp_map[std_string, int] * map_ptr
    cdef public bint _free_map




# MapIntStr
cdef class _MapIterIntStr(object):
    cdef cpp_map[int, std_string].iterator * iter_now
    cdef cpp_map[int, std_string].iterator * iter_end
    cdef void init(_MapIterIntStr, cpp_map[int, std_string] *)

cdef class _MapIntStr:
    cdef cpp_map[int, std_string] * map_ptr
    cdef public bint _free_map




# MapStrUInt
cdef class _MapIterStrUInt(object):
    cdef cpp_map[std_string, extra_types.uint32].iterator * iter_now
    cdef cpp_map[std_string, extra_types.uint32].iterator * iter_end
    cdef void init(_MapIterStrUInt, cpp_map[std_string, extra_types.uint32] *)

cdef class _MapStrUInt:
    cdef cpp_map[std_string, extra_types.uint32] * map_ptr
    cdef public bint _free_map




# MapUIntStr
cdef class _MapIterUIntStr(object):
    cdef cpp_map[extra_types.uint32, std_string].iterator * iter_now
    cdef cpp_map[extra_types.uint32, std_string].iterator * iter_end
    cdef void init(_MapIterUIntStr, cpp_map[extra_types.uint32, std_string] *)

cdef class _MapUIntStr:
    cdef cpp_map[extra_types.uint32, std_string] * map_ptr
    cdef public bint _free_map




# MapStrDouble
cdef class _MapIterStrDouble(object):
    cdef cpp_map[std_string, double].iterator * iter_now
    cdef cpp_map[std_string, double].iterator * iter_end
    cdef void init(_MapIterStrDouble, cpp_map[std_string, double] *)

cdef class _MapStrDouble:
    cdef cpp_map[std_string, double] * map_ptr
    cdef public bint _free_map




# MapUIntUInt
cdef class _MapIterUIntUInt(object):
    cdef cpp_map[extra_types.uint32, extra_types.uint32].iterator * iter_now
    cdef cpp_map[extra_types.uint32, extra_types.uint32].iterator * iter_end
    cdef void init(_MapIterUIntUInt, cpp_map[extra_types.uint32, extra_types.uint32] *)

cdef class _MapUIntUInt:
    cdef cpp_map[extra_types.uint32, extra_types.uint32] * map_ptr
    cdef public bint _free_map




# MapIntInt
cdef class _MapIterIntInt(object):
    cdef cpp_map[int, int].iterator * iter_now
    cdef cpp_map[int, int].iterator * iter_end
    cdef void init(_MapIterIntInt, cpp_map[int, int] *)

cdef class _MapIntInt:
    cdef cpp_map[int, int] * map_ptr
    cdef public bint _free_map




# MapIntDouble
cdef class _MapIterIntDouble(object):
    cdef cpp_map[int, double].iterator * iter_now
    cdef cpp_map[int, double].iterator * iter_end
    cdef void init(_MapIterIntDouble, cpp_map[int, double] *)

cdef class _MapIntDouble:
    cdef cpp_map[int, double] * map_ptr
    cdef public bint _free_map




# MapIntComplex
cdef class _MapIterIntComplex(object):
    cdef cpp_map[int, extra_types.complex_t].iterator * iter_now
    cdef cpp_map[int, extra_types.complex_t].iterator * iter_end
    cdef void init(_MapIterIntComplex, cpp_map[int, extra_types.complex_t] *)

cdef class _MapIntComplex:
    cdef cpp_map[int, extra_types.complex_t] * map_ptr
    cdef public bint _free_map




# MapUIntDouble
cdef class _MapIterUIntDouble(object):
    cdef cpp_map[extra_types.uint32, double].iterator * iter_now
    cdef cpp_map[extra_types.uint32, double].iterator * iter_end
    cdef void init(_MapIterUIntDouble, cpp_map[extra_types.uint32, double] *)

cdef class _MapUIntDouble:
    cdef cpp_map[extra_types.uint32, double] * map_ptr
    cdef public bint _free_map




# MapStrVectorDouble
cdef class _MapIterStrVectorDouble(object):
    cdef cpp_map[std_string, cpp_vector[double]].iterator * iter_now
    cdef cpp_map[std_string, cpp_vector[double]].iterator * iter_end
    cdef void init(_MapIterStrVectorDouble, cpp_map[std_string, cpp_vector[double]] *)

cdef class _MapStrVectorDouble:
    cdef cpp_map[std_string, cpp_vector[double]] * map_ptr
    cdef public bint _free_map




# MapIntVectorDouble
cdef class _MapIterIntVectorDouble(object):
    cdef cpp_map[int, cpp_vector[double]].iterator * iter_now
    cdef cpp_map[int, cpp_vector[double]].iterator * iter_end
    cdef void init(_MapIterIntVectorDouble, cpp_map[int, cpp_vector[double]] *)

cdef class _MapIntVectorDouble:
    cdef cpp_map[int, cpp_vector[double]] * map_ptr
    cdef public bint _free_map



