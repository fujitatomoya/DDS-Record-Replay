# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _StatusWrapper
else:
    import _StatusWrapper

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _StatusWrapper.delete_SwigPyIterator

    def value(self):
        return _StatusWrapper.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _StatusWrapper.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _StatusWrapper.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _StatusWrapper.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _StatusWrapper.SwigPyIterator_equal(self, x)

    def copy(self):
        return _StatusWrapper.SwigPyIterator_copy(self)

    def next(self):
        return _StatusWrapper.SwigPyIterator_next(self)

    def __next__(self):
        return _StatusWrapper.SwigPyIterator___next__(self)

    def previous(self):
        return _StatusWrapper.SwigPyIterator_previous(self)

    def advance(self, n):
        return _StatusWrapper.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _StatusWrapper.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _StatusWrapper.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _StatusWrapper.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _StatusWrapper.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _StatusWrapper.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _StatusWrapper.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _StatusWrapper:
_StatusWrapper.SwigPyIterator_swigregister(SwigPyIterator)

import fastdds
class _StatusSeq(fastdds.LoanableCollection):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _StatusWrapper.delete__StatusSeq

# Register _StatusSeq in _StatusWrapper:
_StatusWrapper._StatusSeq_swigregister(_StatusSeq)

class StatusSeq(_StatusSeq):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _StatusWrapper.delete_StatusSeq

    def __init__(self, *args):
        _StatusWrapper.StatusSeq_swiginit(self, _StatusWrapper.new_StatusSeq(*args))

    def __len__(self):
        return _StatusWrapper.StatusSeq___len__(self)

    def __getitem__(self, i):
        return _StatusWrapper.StatusSeq___getitem__(self, i)

# Register StatusSeq in _StatusWrapper:
_StatusWrapper.StatusSeq_swigregister(StatusSeq)

class Status(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _StatusWrapper.delete_Status

    def __init__(self, *args):
        _StatusWrapper.Status_swiginit(self, _StatusWrapper.new_Status(*args))

    def __eq__(self, x):
        return _StatusWrapper.Status___eq__(self, x)

    def __ne__(self, x):
        return _StatusWrapper.Status___ne__(self, x)

    def previous(self, *args):
        return _StatusWrapper.Status_previous(self, *args)

    def current(self, *args):
        return _StatusWrapper.Status_current(self, *args)

    def info(self, *args):
        return _StatusWrapper.Status_info(self, *args)

    @staticmethod
    def getMaxCdrSerializedSize(current_alignment=0):
        return _StatusWrapper.Status_getMaxCdrSerializedSize(current_alignment)

    @staticmethod
    def getCdrSerializedSize(data, current_alignment=0):
        return _StatusWrapper.Status_getCdrSerializedSize(data, current_alignment)

    def serialize(self, cdr):
        return _StatusWrapper.Status_serialize(self, cdr)

    def deserialize(self, cdr):
        return _StatusWrapper.Status_deserialize(self, cdr)

    @staticmethod
    def getKeyMaxCdrSerializedSize(current_alignment=0):
        return _StatusWrapper.Status_getKeyMaxCdrSerializedSize(current_alignment)

    @staticmethod
    def isKeyDefined():
        return _StatusWrapper.Status_isKeyDefined()

    def serializeKey(self, cdr):
        return _StatusWrapper.Status_serializeKey(self, cdr)

# Register Status in _StatusWrapper:
_StatusWrapper.Status_swigregister(Status)

def Status_getMaxCdrSerializedSize(current_alignment=0):
    return _StatusWrapper.Status_getMaxCdrSerializedSize(current_alignment)

def Status_getCdrSerializedSize(data, current_alignment=0):
    return _StatusWrapper.Status_getCdrSerializedSize(data, current_alignment)

def Status_getKeyMaxCdrSerializedSize(current_alignment=0):
    return _StatusWrapper.Status_getKeyMaxCdrSerializedSize(current_alignment)

def Status_isKeyDefined():
    return _StatusWrapper.Status_isKeyDefined()

GEN_API_VER = _StatusWrapper.GEN_API_VER
class StatusPubSubType(fastdds.TopicDataType):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _StatusWrapper.StatusPubSubType_swiginit(self, _StatusWrapper.new_StatusPubSubType())
    __swig_destroy__ = _StatusWrapper.delete_StatusPubSubType

    def serialize(self, data, payload):
        return _StatusWrapper.StatusPubSubType_serialize(self, data, payload)

    def deserialize(self, payload, data):
        return _StatusWrapper.StatusPubSubType_deserialize(self, payload, data)

    def getSerializedSizeProvider(self, data):
        return _StatusWrapper.StatusPubSubType_getSerializedSizeProvider(self, data)

    def getKey(self, data, ihandle, force_md5=False):
        return _StatusWrapper.StatusPubSubType_getKey(self, data, ihandle, force_md5)

    def createData(self):
        return _StatusWrapper.StatusPubSubType_createData(self)

    def deleteData(self, data):
        return _StatusWrapper.StatusPubSubType_deleteData(self, data)

    def is_bounded(self):
        return _StatusWrapper.StatusPubSubType_is_bounded(self)

    def is_plain(self):
        return _StatusWrapper.StatusPubSubType_is_plain(self)

    def construct_sample(self, memory):
        return _StatusWrapper.StatusPubSubType_construct_sample(self, memory)
    m_md5 = property(_StatusWrapper.StatusPubSubType_m_md5_get, _StatusWrapper.StatusPubSubType_m_md5_set)
    m_keyBuffer = property(_StatusWrapper.StatusPubSubType_m_keyBuffer_get, _StatusWrapper.StatusPubSubType_m_keyBuffer_set)

# Register StatusPubSubType in _StatusWrapper:
_StatusWrapper.StatusPubSubType_swigregister(StatusPubSubType)



