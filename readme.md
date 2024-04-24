# Pyrevision

# Build
run
`pyinstaller pyrevision.py`

# Run
use
add `.\dist\pyrevision\` to path
`pyrevision` or `pyrevision.exe` in a terminal

# Usage
Run program to recieve a random topic to revise, based on
`topics.csv` in `%APPDATA%\pyrevision\`, edit this to contain
topics following the format:

**module name,topic name,score**

*i.e.*
**Database Systems,SQL,0** 
(Best to initalise score to 0 as this is metadata used by the program)

