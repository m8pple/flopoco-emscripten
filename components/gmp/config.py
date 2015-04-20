NAME = 'gmp'
VERSION = '6.0.0'
DOWNLOADS = ['ftp://ftp.gmplib.org/pub/gmp/gmp-%sa.tar.bz2' % VERSION]
SOURCE_DIR = 'gmp-%s' % VERSION
CONFIGURE_CMD = 'CCFLAGS="-Wno-error -Wno-implicit-function-declaration" ./configure --disable-assembly'
MAKE_CMD = 'emmake make -j4'
CONFIG_PATCHES = [
    {
        'file': 'config.h',
        'patch': 'config.h.patch'
    }
]
ARTIFACTS =  {
    'includes': [{
                     'source':'gmp-%s' % VERSION,
                     'name':'gmp'
                 }],
    'libs': [{
                     'source': 'gmp-%s/.libs/libgmp.so' % VERSION,
                     'name':'libgmp.so'
                 }]
}

