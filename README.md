#PyCV
Used to process CV data from CHI660E Electrochemical Workstation  

The program will walk through aimed dir and get all files that match given re(defalut:'cv(.*?)txt') as CV data files to form CV objects.  
A CV object can be seperated by cycle and plotted(based on matplotlib) using this program.  

Overlap of different CV curves is also supported, the overlap.py is an example script.
