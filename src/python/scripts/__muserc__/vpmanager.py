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
            fp, pathname, description = imp.find_module('_vpmanager', [dirname(__file__)])
        except ImportError:
            import _vpmanager
            return _vpmanager
        if fp is not None:
            try:
                _mod = imp.load_module('_vpmanager', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _vpmanager = swig_import_helper()
    del swig_import_helper
else:
    import _vpmanager
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


class vpmanager(_object):
    """Proxy of C++ casac::vpmanager class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vpmanager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vpmanager, name)
    __repr__ = _swig_repr
    def __init__(self): 
        """__init__(self) -> vpmanager"""
        this = _vpmanager.new_vpmanager()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _vpmanager.delete_vpmanager
    __del__ = lambda self : None;
    def saveastable(self, *args, **kwargs):
        """
        saveastable(self, tablename=string("")) -> bool

        Summary
        	Save the vp or pb descriptions as a table

        Description
        	
        Save the vp or pb descriptions as a table.  Each description is in a different
        row of the table.


        Input Parameters:
        	tablename	 Name of table to save vp descriptions in 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_saveastable(self, *args, **kwargs)

    def loadfromtable(self, *args, **kwargs):
        """
        loadfromtable(self, tablename=string("")) -> bool

        Summary
        	Load the vp or pb descriptions from a table (deleting all previous definitions)

        Description
        	
        Load the vp or pb descriptions from a table created, e.g., with saveastable().


        Input Parameters:
        	tablename	 Name of table to load vp descriptions from 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_loadfromtable(self, *args, **kwargs)

    def summarizevps(self, verbose=False):
        """
        summarizevps(self, verbose=False) -> bool

        Summary
        	Summarize the currently accumulated VP descriptions

        Description
        	
        Summarize the currently accumulated VP descriptions to the logger.


        Input Parameters:
        	verbose		 Print out full record? Otherwise, print summary. false 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_summarizevps(self, verbose)

    def setcannedpb(self, *args, **kwargs):
        """
        setcannedpb(self, telescope=string("VLA"), othertelescope=string(""), dopb=True, commonpb=string("DEFAULT"), 
            dosquint=False, paincrement=initialize_variant("720deg"), usesymmetricbeam=False) -> record *

        Summary
        	Select a vp/pb from our library of common pb models

        Description
        	
        We have many vp/pb models ready to go for a variety of telescopes.  If 'DEFAULT' isselected, the system default for that telescope and frequency is used.


        Input Parameters:
        	telescope	 Which telescope in the MS will use this vp/pb? VLA 
        	othertelescope	 If telescope=='OTHER', specify name here 
        	dopb		 Should we apply the vp/pb to this telescope's data? true 
        	commonpb	 List of common vp/pb models: DEFAULT code figures it out DEFAULT 
        	dosquint	 Enable the natural beam squint found in the common vp model false 
        	paincrement	 Increment in Parallactic Angle for asymmetric (ie, squinted) vp application 720deg 
        	usesymmetricbeam	 Not currently used false 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_setcannedpb(self, *args, **kwargs)

    def setpbairy(self, *args, **kwargs):
        """
        setpbairy(self, telescope=string("VLA"), othertelescope=string(""), dopb=True, dishdiam=initialize_variant("25.0m"), 
            blockagediam=initialize_variant("2.5m"), maxrad=initialize_variant("0.8deg"), 
            reffreq=initialize_variant("1.0GHz"), squintdir=initialize_variant(""), 
            squintreffreq=initialize_variant("1.0GHz"), dosquint=False, 
            paincrement=initialize_variant("720deg"), usesymmetricbeam=False) -> record *

        Summary
        	Make an airy disk vp

        Description
        	
        Information sufficient to create a portion of the Airy disk voltage pattern.
        The Airy disk pattern is formed by Fourier transforming a uniformly illuminated
        aperture and is given by
        egin{equation}
        vp_p(i) = ( areaRatio * 2.0 * j_{1}(x)/x 
                          - 2.0 * j_{1}(x*lengthRatio)/(x*lengthRatio) )/ areaNorm,
        nd{equation}
        where areaRatio is the dish area divided by the blockage area, lengthRatio
        is the dish diameter divided by the blockage diameter, and 
        egin{equation}
        x = rac{i * maxrad * 7.016 * dishdiam/24.5m}{N_{samples} * 1.566 * 60}.
        nd{equation}


        Input Parameters:
        	telescope	 Which telescope in the MS will use this vp/pb? VLA 
        	othertelescope	 If telescope=='OTHER', specify name here 
        	dopb		 Should we apply the vp/pb to this telescope's data? true 
        	dishdiam	 Effective diameter of dish 25.0m 
        	blockagediam	 Effective diameter of subreflector blockage 2.5m 
        	maxrad		 Maximum radial extent of the vp/pb (scales with 1/freq) 0.8deg 
        	reffreq		 Frequency at which maxrad is specified 1.0GHz 
        	squintdir	 Offset (Measure) of RR beam from pointing center, azel frame (scales with 1/freq) 
        	squintreffreq	 Frequency at which the squint is specified 1.0GHz 
        	dosquint	 Enable the natural beam squint found in the common vp model false 
        	paincrement	 Increment in Parallactic Angle for asymmetric (ie, squinted) vp application 720deg 
        	usesymmetricbeam	 Not currently used false 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_setpbairy(self, *args, **kwargs)

    def setpbcospoly(self, *args, **kwargs):
        """
        setpbcospoly(self, telescope=string("VLA"), othertelescope=string(""), dopb=True, coeff=initialize_vector(1, (double)-1), 
            scale=initialize_vector(1, (double)-1), maxrad=initialize_variant("0.8deg"), 
            reffreq=initialize_variant("1.0GHz"), isthispb=string("PB"), 
            squintdir=initialize_variant(""), squintreffreq=initialize_variant("1.0GHz"), 
            dosquint=False, paincrement=initialize_variant("720deg"), usesymmetricbeam=False) -> record *

        Summary
        	Make a vp/pb from a polynomial of scaled cosines

        Description
        	
        A voltage pattern or primary beam of the form
        egin{equation}
        VP(x) = \sum_{i} ( coeff_{i} \cos^{2i}( scale_{i} x).
        nd{equation}
        This is a generalization of the WSRT primary beam model.


        Input Parameters:
        	telescope	 Which telescope in the MS will use this vp/pb? VLA 
        	othertelescope	 If telescope=='OTHER', specify name here 
        	dopb		 Should we apply the vp/pb to this telescope's data? true 
        	coeff		 Vector of coefficients of cosines -1 
        	scale		 Vector of scale factors of cosines -1 
        	maxrad		 Maximum radial extent of the vp/pb (scales with 1/freq) 0.8deg 
        	reffreq		 Frequency at which maxrad is specified 1.0GHz 
        	isthispb	 Do these parameters describe a PB or a VP? PB 
        	squintdir	 Offset (Measure) of RR beam from pointing center, azel frame (scales with 1/freq) 
        	squintreffreq	 Frequency at which the squint is specified 1.0GHz 
        	dosquint	 Enable the natural beam squint found in the common vp model false 
        	paincrement	 Increment in Parallactic Angle for asymmetric (ie, squinted) vp application 720deg 
        	usesymmetricbeam	 Not currently used false 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_setpbcospoly(self, *args, **kwargs)

    def setpbgauss(self, *args, **kwargs):
        """
        setpbgauss(self, telescope=string("VLA"), othertelescope=string(""), dopb=True, halfwidth=initialize_variant("0.5deg"), 
            maxrad=initialize_variant("1.0deg"), reffreq=initialize_variant("1.0GHz"), 
            isthispb=string("PB"), squintdir=initialize_variant(""), 
            squintreffreq=initialize_variant("1.0GHz"), dosquint=False, paincrement=initialize_variant("720deg"), 
            usesymmetricbeam=False) -> record *

        Summary
        	Make a Gaussian vp/pb

        Description
        	
        Make a Gaussian primary beam given by
        egin{equation}
        PB(x) =  e^{- (x/(halfwidth*\sqrt{1/\log(2)})) }.
        nd{equation}


        Input Parameters:
        	telescope	 Which telescope in the MS will use this vp/pb? VLA 
        	othertelescope	 If telescope=='OTHER', specify name here 
        	dopb		 Should we apply the vp/pb to this telescope's data? true 
        	halfwidth	 Half power half width of the Gaussian at the reffreq 0.5deg 
        	maxrad		 Maximum radial extent of the vp/pb (scales with 1/freq) 1.0deg 
        	reffreq		 Frequency at which maxrad is specified 1.0GHz 
        	isthispb	 Do these parameters describe a PB or a VP? PB 
        	squintdir	 Offset (Measure) of RR beam from pointing center, azel frame (scales with 1/freq) 
        	squintreffreq	 Frequency at which the squint is specified 1.0GHz 
        	dosquint	 Enable the natural beam squint found in the common vp model false 
        	paincrement	 Increment in Parallactic Angle for asymmetric (ie, squinted) vp application 720deg 
        	usesymmetricbeam	 Not currently used false 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_setpbgauss(self, *args, **kwargs)

    def setpbinvpoly(self, *args, **kwargs):
        """
        setpbinvpoly(self, telescope=string("VLA"), othertelescope=string(""), dopb=True, coeff=initialize_vector(1, (double)-1), 
            maxrad=initialize_variant("0.8deg"), reffreq=initialize_variant("1.0GHz"), 
            isthispb=string("PB"), squintdir=initialize_variant(""), 
            squintreffreq=initialize_variant("1.0"), dosquint=False, paincrement=initialize_variant("720deg"), 
            usesymmetricbeam=False) -> record *

        Summary
        	Make a vp/pb as an inverse polynomial

        Description
        	
        The inverse polynomial describes the inverse of the VP or PB
        as a polynomial of even powers:
        egin{equation}
        1/VP(x) = \sum_{i} coeff_{i} * x^{2i}.
        nd{equation}


        Input Parameters:
        	telescope	 Which telescope in the MS will use this vp/pb? VLA 
        	othertelescope	 If telescope=='OTHER', specify name here 
        	dopb		 Should we apply the vp/pb to this telescope's data? true 
        	coeff		 Coefficients of even powered terms -1 
        	maxrad		 Maximum radial extent of the vp/pb (scales with 1/freq) 0.8deg 
        	reffreq		 Frequency at which maxrad is specified 1.0GHz 
        	isthispb	 Do these parameters describe a PB or a VP? PB 
        	squintdir	 Offset (Measure) of RR beam from pointing center, azel frame (scales with 1/freq) 
        	squintreffreq	 Frequency at which the squint is specified 1.0 
        	dosquint	 Enable the natural beam squint found in the common vp model false 
        	paincrement	 Increment in Parallactic Angle for asymmetric (ie, squinted) vp application 720deg 
        	usesymmetricbeam	 Not currently used false 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_setpbinvpoly(self, *args, **kwargs)

    def setpbnumeric(self, *args, **kwargs):
        """
        setpbnumeric(self, telescope=string("VLA"), othertelescope=string(""), dopb=True, vect=initialize_vector(1, (double)-1), 
            maxrad=initialize_variant("0.8deg"), reffreq=initialize_variant("1.0GHz"), 
            isthispb=string("PB"), squintdir=initialize_variant(""), 
            squintreffreq=initialize_variant("1.0GHz"), dosquint=False, paincrement=initialize_variant("720deg"), 
            usesymmetricbeam=False) -> record *

        Summary
        	Make a vp/pb from a user-supplied vector

        Description
        	
        Supply a vector of vp/pb sample values taken on a regular grid between x=0 and
        x=maxrad.  We perform sinc interpolation to fill in the lookup table.


        Input Parameters:
        	telescope	 Which telescope in the MS will use this vp/pb? VLA 
        	othertelescope	 If telescope=='OTHER', specify name here 
        	dopb		 Should we apply the vp/pb to this telescope's data? true 
        	vect		 Vector of vp/pb samples uniformly spaced from 0 to maxrad -1 
        	maxrad		 Maximum radial extent of the vp/pb (scales with 1/freq) 0.8deg 
        	reffreq		 Frequency at which maxrad is specified 1.0GHz 
        	isthispb	 Do these parameters describe a PB or a VP? PB 
        	squintdir	 Offset (Measure) of RR beam from pointing center, azel frame (scales with 1/freq) 
        	squintreffreq	 Frequency at which the squint is specified 1.0GHz 
        	dosquint	 Enable the natural beam squint found in the common vp model false 
        	paincrement	 Increment in Parallactic Angle for asymmetric (ie, squinted) vp application 720deg 
        	usesymmetricbeam	 Not currently used false 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_setpbnumeric(self, *args, **kwargs)

    def setpbimage(self, *args, **kwargs):
        """
        setpbimage(self, telescope=string("VLA"), othertelescope=string(""), dopb=True, realimage=string(""), 
            imagimage=string(""), compleximage=string(""), antnames=std::vector< string >(1, "")) -> record *

        Summary
        	Make a vp/pb from a user-supplied image

        Description
        	
        Experimental: Supply an image of the E Jones elements. The format of the 
        image is:
        egin{description}
        \item[Shape] nx by ny by 4 complex polarizations (RR, RL, LR, LL or
        XX, XY, YX, YY) by 1 channel.
        \item[Direction coordinate] Az, El
        \item[Stokes coordinate] All four ``stokes'' parameters must be present
        in the sequence RR, RL, LR, LL or XX, XY, YX, YY.
        \item[Frequency] Only one channel is currently needed - frequency 
        dependence beyond that is ignored. 
        nd{description}

        If a compleximage is specified the real and imaginary images is to be left empty.

        The other option is to provide the real and imaginary part of the E-Jones as seperale {	t float} images
        On that case
        one or two images may be specified - the real (must be present) and
        imaginary parts (optional). 

        Note that beamsquint must be intrinsic to the images themselves.
        This will be accounted for correctly by regridding of the images
        from Az-El to Ra-Dec according to the parallactic angle.

        antnames is the Vector of names  for which this response pattern apply '*' is for all 
        The name has to match exactly the name of the Antennas in the ANTENNA table of the MS with which
        you want to use this VPManager table or object.



        Input Parameters:
        	telescope	 Which telescope in the MS will use this vp/pb? VLA 
        	othertelescope	 If telescope=='OTHER', specify name here 
        	dopb		 Should we apply the vp/pb to this telescope's data? true 
        	realimage	 Real part of vp as an image 
        	imagimage	 Imaginary part of vp as an image 
        	compleximage	 complex vp as an image of complex numbers; if specified realimage and imagimage are ignored 
        	antnames	 antenna names for which this pattern is valid; default is all antennas * 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_setpbimage(self, *args, **kwargs)

    def setpbpoly(self, *args, **kwargs):
        """
        setpbpoly(self, telescope=string("VLA"), othertelescope=string(""), dopb=True, coeff=initialize_vector(1, (double)-1), 
            maxrad=initialize_variant("0.8deg"), reffreq=initialize_variant("1.0GHz"), 
            isthispb=string("PB"), squintdir=initialize_variant(""), 
            squintreffreq=initialize_variant("1.0GHz"), dosquint=False, paincrement=initialize_variant("720"), 
            usesymmetricbeam=False) -> record *

        Summary
        	Make a vp/pb from a polynomial

        Description
        	
        The VP or PB is described as a polynomial of even powers:
        egin{equation}
        VP(x) = \sum_{i} coeff_{i} * x^{2i}.
        nd{equation}


        Input Parameters:
        	telescope	 Which telescope in the MS will use this vp/pb? VLA 
        	othertelescope	 If telescope=='OTHER', specify name here 
        	dopb		 Should we apply the vp/pb to this telescope's data? true 
        	coeff		 Coefficients of even powered terms -1 
        	maxrad		 Maximum radial extent of the vp/pb (scales with 1/freq) 0.8deg 
        	reffreq		 Frequency at which maxrad is specified 1.0GHz 
        	isthispb	 Do these parameters describe a PB or a VP? PB 
        	squintdir	 Offset (Measure) of RR beam from pointing center, azel frame (scales with 1/freq) 
        	squintreffreq	 Frequency at which the squint is specified 1.0GHz 
        	dosquint	 Enable the natural beam squint found in the common vp model false 
        	paincrement	 Increment in Parallactic Angle for asymmetric (ie, squinted) vp application 720 
        	usesymmetricbeam	 Not currently used false 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_setpbpoly(self, *args, **kwargs)

    def setpbantresptable(self, *args, **kwargs):
        """
        setpbantresptable(self, telescope=string(""), othertelescope=string(""), dopb=True, antresppath=string("")) -> bool

        Summary
        	Declare a reference to an antenna responses table

        Description
        	
        Declare a reference to an antenna responses table containing a set of VP/PB definitions.


        Input Parameters:
        	telescope	 Which telescope in the MS will use this vp/pb? 
        	othertelescope	 If telescope=='OTHER', specify name here 
        	dopb		 Should we apply the vp/pb to this telescope's data? true 
        	antresppath	 The path to the antenna responses table (absolute or relative to CASA data dir.) 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_setpbantresptable(self, *args, **kwargs)

    def reset(self):
        """
        reset(self) -> bool

        Summary
        	Reinitialize the VPManager (will erase all VPs and defaults defined on the command line)

        Description
        	
        Reinitialize the VPManager database.
        Erase all VPs and defaults defined on the command line.

        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_reset(self)

    def setuserdefault(self, *args, **kwargs):
        """
        setuserdefault(self, vplistnum=-1, telescope=string(""), anttype=string("")) -> bool

        Summary
        	Select the VP which is to be used by the imager for the given telescope and antenna type

        Description
        	
        Selects the VP which is to be used by the imager for the given telescope and antenna type.
        Overwrites a previous default. Returns True if successful.


        Input Parameters:
        	vplistnum	 The number of the vp as displayed by summarizevps(), or -1 for internal default, or -2 for unset -1 
        	telescope	 Which telescope in the MS will use this vp/pb? 
        	anttype		 Which antennatype will use this vp/pb? Default: '' = all 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_setuserdefault(self, *args, **kwargs)

    def getuserdefault(self, *args, **kwargs):
        """
        getuserdefault(self, telescope=string(""), anttype=string("")) -> int

        Summary
        	Get the vp list number of the present default VP/PB for the given parameters (-1 = internal PB, -2 = none)

        Description
        	
        Get the vp list number of the present default VP/PB for the given parameters.


        Input Parameters:
        	telescope	 Which telescope in the MS will use this vp/pb? 
        	anttype		 Which antennatype will use this vp/pb? Default: '' = all 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_getuserdefault(self, *args, **kwargs)

    def getanttypes(self, *args, **kwargs):
        """
        getanttypes(self, telescope=string(""), obstime=initialize_variant(""), freq=initialize_variant(""), 
            obsdirection=initialize_variant("AZEL 0deg 90deg")) -> std::vector< std::string >

        Summary
        	Return the list of available antenna types for the given parameters

        Description
        	
        Get a list of the available antenna types.


        Input Parameters:
        	telescope	 Telescope name 
        	obstime		 Time of the observation (for versioning and reference frame calculations) 
        	freq		 Frequency of the observation (may include reference frame, default: LSRK) 
        	obsdirection	 Direction of the observation (may include reference frame, default: J2000). default: Zenith AZEL 0deg 90deg 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_getanttypes(self, *args, **kwargs)

    def numvps(self, *args, **kwargs):
        """
        numvps(self, telescope=string(""), obstime=initialize_variant(""), freq=initialize_variant(""), 
            obsdirection=initialize_variant("AZEL 0deg 90deg")) -> int

        Summary
        	Return the number of vps/pbs available for the given parameters

        Description
        	
        Can be used to, e.g., determine the number of antenna types.
        Note: if a global response is defined for the telescope, this will increase the count of
        available vps/pbs by 1.


        Input Parameters:
        	telescope	 Telescope name 
        	obstime		 Time of the observation (for versioning and reference frame calculations) 
        	freq		 Frequency of the observation (may include reference frame, default: LSRK) 
        	obsdirection	 Direction of the observation (may include reference frame, default: J2000). default: Zenith AZEL 0deg 90deg 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_numvps(self, *args, **kwargs)

    def getvp(self, *args, **kwargs):
        """
        getvp(self, telescope=string(""), antennatype=string(""), obstime=initialize_variant(""), freq=initialize_variant(""), 
            obsdirection=initialize_variant("AZEL 0deg 90deg")) -> record *

        Summary
        	Return the default vps/pbs record for the given parameters

        Description
        	
        Record is empty if no matching vp/pb could be found.


        Input Parameters:
        	telescope	 Telescope name 
        	antennatype	 The antenna type as a string, e.g. 'DV' 
        	obstime		 Time of the observation (for versioning and reference frame calculations), e.g. 2011/12/12T00:00:00 
        	freq		 Frequency of the observation (may include reference frame, default: LSRK) 
        	obsdirection	 Direction of the observation (may include reference frame, default: J2000), default: AZEL 0deg 90deg 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_getvp(self, *args, **kwargs)

    def createantresp(self, *args, **kwargs):
        """
        createantresp(self, imdir=string(""), starttime=string(""), bandnames=std::vector< string >(1, ""), bandminfreq=std::vector< string >(1, ""), 
            bandmaxfreq=std::vector< string >(1, "")) -> bool

        Summary
        	Create a standard-format AntennaResponses table

        Description
        	
        The AntennaResponses table serves CASA to look up the location of images describing the
        response of observatory antennas. Three types of images are supported: 'VP' - real voltage patterns,
        'AIF' - complex aperture illumination patterns, 'EFP' - complex electric field patterns.
        For each image, a validity range can be defined in Azimuth, Elevation, and Frequency.
        Furthermore, an antenna type (for heterogeneous arrays), a receiver type (for the case of
        several receivers on the same antenna having overlapping frequency bands), and a beam number
        (for the case of multiple beams per antenna) are associated with each response image.

        The images need to be stored in a single directory DIR of arbitrary name and need to
        have file names following the pattern
        egin{verbatim}
        obsname_beamnum_anttype_rectype_azmin_aznom_azmax_elmin_elnom_elmax_freqmin_freqnom_freqmax_frequnit_comment_functype.im
        nd{verbatim}
        where the individual name elements mean the following (none of the elements may contain 
        the space character, but they may be empty strings if they are not numerical values):
        egin{description}
        \item[obsname] - name of the observatory as in the Observatories table, e.g. 'ALMA'
        \item[beamnum] - the numerical beam number (integer) for the case of multiple beams, e.g. 0
        \item[anttype] - name of the antenna type, e.g. 'DV'
        \item[rectype] - name of the receiver type, e.g. ''
        \item[azmin, aznom, azmax] - numerical value (degrees) of the minimal, the nominal, and 
          the maximal Azimuth where this response is valid, e.g. '-10.5\_0.\_10.5'
        \item[elmin, elnom, elmax] - numerical value (degrees) of the minimal, the nominal, and 
          the maximal Elevation where this response is valid, e.g. '10.\_45.\_80.'
        \item[freqmin, freqnom, freqmax] - numerical value (degrees) of the minimal, the nominal, and 
          the maximal Frequency (in units of frequnit) where this response is valid, e.g. '84.\_100.\_116.'
        \item[frequnit] - the unit of the previous three frequencies, e.g. 'GHz'
        \item[comment] - any string containing only characters permitted in file names and not empty space
        \item[functype] - the type of the image as defined above ('VP', 'AIF', or 'EFP')
         nd{description}

        The createantresp method will then extract the parameters from all the images in DIR
        and create the lookup table in the same directory.


        Input Parameters:
        	imdir		 Path to the directory containing the response images 
        	starttime	 Time from which onwards the response is valid, format YYYY/MM/DD/hh:mm:ss 
        	bandnames	 List containing the names of the observatory's frequency bands 
        	bandminfreq	 List containing the lower edges of the observatory's frequency bands, e.g. ['80GHz','120GHz'] 
        	bandmaxfreq	 List containing the upper edges of the observatory's frequency bands, e.g. ['120GHz','180GHz'] 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_createantresp(self, *args, **kwargs)

    def getrespimagename(self, *args, **kwargs):
        """
        getrespimagename(self, telescope=string(""), starttime=string(""), frequency=string(""), functype=string("ANY"), 
            anttype=string(""), azimuth=string("0deg"), elevation=string("45deg"), 
            rectype=string(""), beamnumber=0) -> string

        Summary
        	Get the image name for the given parameters from the given responses table

        Description
        	
        Given the observatory name, the antenna type, the receiver type, the observing frequency, the
        observing direction, and the beam number, find the applicable response image and return its name.


        Input Parameters:
        	telescope	 Which telescope is described by this response? 
        	starttime	 Time at which the response has to be valid, format YYYY/MM/DD/hh:mm:ss 
        	frequency	 The frequency at which the response has to be valid, e.g. '100GHz' 
        	functype	 Type of the responsefunction requested, e.g. 'EFP' ANY 
        	anttype		 Antenna type (observatory-dependent) 
        	azimuth		 Azimuth of the observation (at the location of the observatory, 0 is North), e.g. '5deg' 0deg 
        	elevation	 Elevation of the observation (at the location of the observatory, 0 is North), e.g. '60deg' 45deg 
        	rectype		 Receiver type (observatory-dependent) 
        	beamnumber	 Beam number (for the case of multiple beams per receiver) 0 
        	
        --------------------------------------------------------------------------------
        	      
        """
        return _vpmanager.vpmanager_getrespimagename(self, *args, **kwargs)

vpmanager_swigregister = _vpmanager.vpmanager_swigregister
vpmanager_swigregister(vpmanager)

# This file is compatible with both classic and new-style classes.


