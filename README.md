flopoco-emscripten
==================

This is a work in progress to see if [FloPoCo](http://flopoco.gforge.inria.fr/) will compile
in emscripten. It is based on the work to compile  [CGAL](http://www.cgal.org/), and is forked
from (https://github.com/marcosscriven/cgaljs)[https://github.com/marcosscriven/cgaljs].

Status
------

So far I've done nothing beyond working out how to get emscripten to work.

Things that need to be done are:
- libfplll
- sollya
- GSL
- mpfi

Though some of those could be disabled at the expense of losing some operators.

Dependencies
------------

* Emscripten (and all its requirements including Python, Clang, Java, and NodeJS)
* Emscripten tools must be on the path
* Linux build tools
 
To get started
--------------

* Clone the Git repo
* Run the build_all.py script
* You should find the generated libs in the libs dir, and includes for each dependency in the includes dir
* In examples there's a simple test script you can run to demontrate the output running in NodeJS

Issues & Limitations
--------------------
