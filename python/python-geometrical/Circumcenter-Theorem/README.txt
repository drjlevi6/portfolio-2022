These Python scripts produce an animated illustration of a classical theorem of Euclidean geometry, regarding the perpendicular bisectors of a triangle and the inscribed circle they generate. The theorem may be stated as follows:

For any triangle ABC, the perpendicular bisectors of segments AB, BC, CA intersect at a common point O; the point O is the center of a circle c containing the triangle's vertices A, B, C.

(The circle c above is now known as the circumscribing circle of triangle ABC, and the point O is known as ABC's circumcenter; the theorem stated above is usually referred to as the circumcenter theorem.)

The folder contains two scripts, perpBisectors.py and perpView.py. They depend upon the Python graphics module turtle, which in turn depends on the module tkinter. (There is also a Macintosh QuickTime movie, perpBisectors.mov, which shows the running of the scripts.)

The scripts may be downloaded and run using the following shell (bash) commands:

CONTAINER=$HOME/Desktop		# or choose another CONTAINER
mkdir -p $CONTAINER
cd $CONTAINER
git clone https://github.com/drjlevi6/portfolio-2022
cd $CONTAINER/portfolio-2022/python/python-geometrical/perpBisectors_theorem/
python -m perpBisectors

where "python" is a version of Python 3 configured to support the Python modules turtle and tkinter.

Reference: https://en.wikipedia.org/wiki/Triangle_center
