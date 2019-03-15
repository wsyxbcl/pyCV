# PyCV
Used to process Cyclic Voltammetry data from CHI660E Electrochemical Workstation  
It's a user-unfriendly script for it's mainly used by few guys in our lab.    

The program will walk through aimed dir and get all files that match given re(defalut:'cv(.*?)txt') as CV data files to form CV objects.  
A CV object can be seperated by cycle and plotted(based on matplotlib) using this program.  
Overlap of different CV curves is also supported, the overlap.py is an example.  
Input file is generated from CHI660E Electrochemical Workstation(cv_sample.txt is an example).

## Demo
Cycles seperated and plotted  
![image](https://github.com/wsyxbcl/pyCV/blob/master/demo/cv_sample.png)  

Different CV curves overlapped  
![image](https://github.com/wsyxbcl/pyCV/blob/master/demo/overlap/metal_weird_cv.png)
