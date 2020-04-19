# gSorter	
Reality Shift team project for HACKUNIVERSITY hackathon  
  
## Track: Logistics
#### Smart conveyor for garbage sorting powered by neural networks

## Task
You need to develop a software, which can detect individual objects in garbage flow at conveyor, as well as their size, position and speed (and visualize that information). You can use arbitrary video from the Internet or you can imitate the flow and record it.
___
### Our solution
Our first approach was to use Microsoft Kinect v2 to retrieve D channel in addition to RGB.
Unfortunately, we were very limited in time so we decided to use only RGB for training and inference.

### Data
We decided to simulate the garbage flow using a lot of RedBull cans that we were given out on the hackaton.
We took about 1000 photos of RedBull cans from different angles, under different lighting conditions and different states.
<p align="center"><img src="https://github.com/wndenis/gSorter/raw/master/ReadmeMedia/DataVideo.gif" width="430"></p>

As far as I know, there is a problem of overfitting when network could recognize object only if it is on the same background as it was when training. To avoid this, we used TV as background😄 Even if it was a wrong approach, it was kinda funny.
<p align="center"><img src="https://github.com/wndenis/gSorter/raw/master/ReadmeMedia/Moment.jpg" width="430"></p>

To label dataset we used labelbox.com service and 24-hour work of three unfortunate teammates.

![Data](https://github.com/wndenis/gSorter/raw/master/ReadmeMedia/Data2.jpg)


Neural network model is YOLO3 in python as efficient, fast, and affordable solution.

### Code
We wrote small module which takes camera frames, crops and scales them, and then forwards them to the neural network. Using dimensions provided by YOLO3, this module visualize bounding box, middle point, name and confidence value.

### Demo
<p align="center">
  <img src="https://github.com/wndenis/gSorter/raw/master/ReadmeMedia/RecognitionVideo.gif"><br>
  Realtime detection
  <br><br>
  <img src="https://github.com/wndenis/gSorter/raw/master/ReadmeMedia/Recognition2.jpg">
  <img src="https://github.com/wndenis/gSorter/raw/master/ReadmeMedia/Recognition4.jpg">
  There are some false positive results  
</p>

### Results
Unfortunately, we couldnt take prize due to unexpected change of task. In fact, they wanted not a neural network object recognition - any CV method was acceptable. They wanted us to program some kind of manipulator we were not told about.

### Conclusion
We collected and labeled the dataset of 1000 images of Redbull cans.  
If anyone needs it, feel free to use it, it is right here. <nobr>¯\\_(ツ)_/¯</nobr>  
We have learned to train neural networks on our custom data and also to get results from them. Sadly, we were somewhat disappointed in this competition, but we had a great time and gained valuable experience, for which we want to say thank you.
