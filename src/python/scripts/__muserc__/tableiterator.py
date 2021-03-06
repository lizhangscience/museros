# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_tableiterator', [dirname(__file__)])
        except ImportError:
            import _tableiterator
            return _tableiterator
        if fp is not None:
            try:
                _mod = imp.load_module('_tableiterator', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _tableiterator = swig_import_helper()
    del swig_import_helper
else:
    import _tableiterator
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class tableiterator(_object):
    """Proxy of C++ casac::tableiterator class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, tableiterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, tableiterator, name)
    __repr__ = _swig_repr
    def __init__(self): 
        """__init__(self) -> tableiterator"""
        this = _tableiterator.new_tableiterator()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tableiterator.delete_tableiterator
    __del__ = lambda self : None;
    def table(self):
        """
        table(self) -> record *

        Summary
        	Return the current table subset

        Description
        	
        Return a 	exttt{table} tool for the current subset.
        \Note that 	exttt{next} has to be called to form the first subset.

        --------------------------------------------------------------------------------
        	      
        """
        return _tableiterator.tableiterator_table(self)

    def reset(self):
        """
        reset(self) -> bool

        Summary
        	Reset iteration to the beginning

        Description
        	
        It resets the iteration to the beginning of the table.
        Note that 	exttt{next} has to be called to get the first subset.

        --------------------------------------------------------------------------------
        	      
        """
        return _tableiterator.tableiterator_reset(self)

    def next(self):
        """
        next(self) -> bool

        Summary
        	Advance to the next table subset

        Description
        	
        Form the next subset of the table.
        It returns a false status if no more subsets are available
        The subset can be accessed using the 	exttt{table} function.
        \Note that 	exttt{next} has to be called to form the first subset.

        --------------------------------------------------------------------------------
        	      
        """
        return _tableiterator.tableiterator_next(self)

    def terminate(self):
        """
        terminate(self) -> bool

        Summary
        	Terminate the iteration and clean up memory

        Description
        	
        This function has to be called if the iteration is ended prematurely.
        Otherwise tables are left open.
        If the iteration is done until the end, 	exttt{terminate} does not
        need to be called, but it does not harm to call it.
        \Hereafter it is still possible to restart the iteration using the
        	exttt{reset} function.

        --------------------------------------------------------------------------------
        	      
        """
        return _tableiterator.tableiterator_terminate(self)

    def done(self):
        """
        done(self) -> bool

        Summary
        	End the tableiterator tool

        Description
        	
        Terminate the iteration and free up all memory.

        --------------------------------------------------------------------------------
        	      
        """
        return _tableiterator.tableiterator_done(self)

tableiterator_swigregister = _tableiterator.tableiterator_swigregister
tableiterator_swigregister(tableiterator)

# This file is compatible with both classic and new-style classes.


