# Hue-Saturation-Value-Filter

Work in progress, first program trying to learn computer vision.

Graphical user interface using pyqt with the Qt Designer and the openCV library.

Program uses a laptops built-in camera to obtain continuous video stream. On the
left side, the three sliders adjust the minimum hue, saturation, and value levels 
respectively. Similarly on the right side the sliders adjust the maximum hue, 
saturation, and value levels respectively. Adjusting these value allow for 
filtering of colors to display a single color in view of the camera. The User
can name the current state in an entry box and add it to a list of user defined
filters.

TODO:
Upon entering the named filter to the list, the list will store the slider values
associated with the filter. When a filter from the list is selected, the slider 
values will be set to restore the selected filters state.
