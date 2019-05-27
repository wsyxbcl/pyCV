# PyCV
Used to process Cyclic Voltammetry data from CHI660E Electrochemical Workstation  
It's a user-unfriendly script for it's mainly used by few guys in our lab.  
So if you feel this is useful, please raise an issue to let me know, maybe I'll make it more user friendly.

The program will walk through aimed dir and get all files that match given re(defalut:'cv(.*?)txt') as CV data files to form CV objects.  
A CV object can be seperated by cycle and plotted(based on matplotlib) using this program.  
Overlap of different CV curves is also supported, the overlap.py is an example.  
Input file is generated from CHI660E Electrochemical Workstation(cv_sample.txt is an example).

## Demo
### Cycles seperated and plotted  
![image](https://github.com/wsyxbcl/pyCV/blob/master/demo/cv_sample.png)  

### Different CV curves overlapped  
![image](https://github.com/wsyxbcl/pyCV/blob/master/demo/overlap/metal_weird_cv.png)

### Four-electrode system
Using ORR on RRDE as a example.  
![image](https://github.com/wsyxbcl/pyCV/blob/master/demo/four_electrode/cv_orr_four_electrode.png)
