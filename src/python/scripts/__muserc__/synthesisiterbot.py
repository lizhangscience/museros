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
            fp, pathname, description = imp.find_module('_synthesisiterbot', [dirname(__file__)])
        except ImportError:
            import _synthesisiterbot
            return _synthesisiterbot
        if fp is not None:
            try:
                _mod = imp.load_module('_synthesisiterbot', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _synthesisiterbot = swig_import_helper()
    del swig_import_helper
else:
    import _synthesisiterbot
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


class synthesisiterbot(_object):
    """Proxy of C++ casac::synthesisiterbot class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, synthesisiterbot, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, synthesisiterbot, name)
    __repr__ = _swig_repr
    def __init__(self): 
        """__init__(self) -> synthesisiterbot"""
        this = _synthesisiterbot.new_synthesisiterbot()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _synthesisiterbot.delete_synthesisiterbot
    __del__ = lambda self : None;
    def setupiteration(self, *args, **kwargs):
        """
        setupiteration(self, iterpars=initialize_record("")) -> record *

        Summary
        	Set parameters to control iteration mechanisms

        Description
        	


        Input Parameters:
        	iterpars	 All parameters that control iterations 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _synthesisiterbot.synthesisiterbot_setupiteration(self, *args, **kwargs)

    def cleanComplete(self):
        """
        cleanComplete(self) -> int

        Summary
        	Return true when we have completed this clean

        Description
        	

        --------------------------------------------------------------------------------
        	      
        """
        return _synthesisiterbot.synthesisiterbot_cleanComplete(self)

    def endmajorcycle(self):
        """
        endmajorcycle(self) -> bool

        Summary
        	Record the end of a major cycle

        Description
        	

        --------------------------------------------------------------------------------
        	      
        """
        return _synthesisiterbot.synthesisiterbot_endmajorcycle(self)

    def getminorcyclecontrols(self):
        """
        getminorcyclecontrols(self) -> record *

        Summary
        	Get the controller for a minor cycle

        Description
        	

        --------------------------------------------------------------------------------
        	      
        """
        return _synthesisiterbot.synthesisiterbot_getminorcyclecontrols(self)

    def mergeexecrecord(self, *args, **kwargs):
        """
        mergeexecrecord(self, execrecord=initialize_record("")) -> bool

        Summary
        	Update the iterbot with iteration stats from the deconvolver

        Description
        	


        Input Parameters:
        	execrecord	 Pass in the output of synthesisdeconvolver.executeminorcycle() 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _synthesisiterbot.synthesisiterbot_mergeexecrecord(self, *args, **kwargs)

    def changestopflag(self, stopflag=False):
        """
        changestopflag(self, stopflag=False) -> bool

        Summary
        	Change the stop flag (for interactive clean)

        Description
        	


        Input Parameters:
        	stopflag	 Set to False for the next cleanComplete() check to stop the run false 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _synthesisiterbot.synthesisiterbot_changestopflag(self, stopflag)

    def mergeinitrecord(self, *args, **kwargs):
        """
        mergeinitrecord(self, initrecord=initialize_record("")) -> bool

        Summary
        	Initialize the iterbot with starting peak residuals

        Description
        	


        Input Parameters:
        	initrecord	 Pass in the output of synthesisdeconvolver.initminorcycle() 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _synthesisiterbot.synthesisiterbot_mergeinitrecord(self, *args, **kwargs)

    def getiterationdetails(self):
        """
        getiterationdetails(self) -> record *

        Summary
        	Return a record with the details of the iteration

        Description
        	

        --------------------------------------------------------------------------------
        	      
        """
        return _synthesisiterbot.synthesisiterbot_getiterationdetails(self)

    def pauseforinteraction(self):
        """
        pauseforinteraction(self) -> record *

        Summary
        	Pause for interaction

        Description
        	

        --------------------------------------------------------------------------------
        	      
        """
        return _synthesisiterbot.synthesisiterbot_pauseforinteraction(self)

    def getiterationsummary(self):
        """
        getiterationsummary(self) -> record *

        Summary
        	Return a record with a summary of the iteration

        Description
        	

        --------------------------------------------------------------------------------
        	      
        """
        return _synthesisiterbot.synthesisiterbot_getiterationsummary(self)

    def done(self):
        """
        done(self) -> bool

        Summary
        	Close the tool

        Description
        	

        --------------------------------------------------------------------------------
        	      
        """
        return _synthesisiterbot.synthesisiterbot_done(self)

synthesisiterbot_swigregister = _synthesisiterbot.synthesisiterbot_swigregister
synthesisiterbot_swigregister(synthesisiterbot)

# This file is compatible with both classic and new-style classes.


