NAME = 'fplll'
VERSION = '3.0.12'
DOWNLOADS = ['http://pkgs.fedoraproject.org/repo/pkgs/libfplll/libfplll-%s.tar.gz/3b1cf0f3c4bcbe8b40da3d14c8029c58/libfplll-3.0.12.tar.gz' % VERSION]
SOURCE_DIR = 'libfplll-%s' % VERSION
CONFIGURE_CMD = 'EMCONFIGURE_JS=1 CPPFLAGS="-I{includes}/gmp -I{includes}/mpfr -L{libs}" emconfigure ./configure --with-gmp-include={includes}/gmp --with-gmp-lib={libs}'
MAKE_CMD = 'emmake make -j4'
SOURCE_PATCHES = [
   {
        'file': 'configure',
        'patch': 'configure.patch'
    },
   {
	'file': 'src/nr.h',
	'patch': 'src_nr.h.patch'
   }
]
ARTIFACTS =  {
    'includes': [{
                     'source':'libfplll-%s/src' % VERSION,
                     'name':'fplll'
                 }],
#    'libs': [{
#                 'source': 'mpfr-%s/src/.libs/libmpfr.so' % VERSION,
#                 'name':'libmpfr.so'
#             }]
}





