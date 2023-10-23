# Build Face-mask-detector-using-RetinaNet-model

We are grappling with a pandemic that’s operating at a never-before-seen scale. Researchers all over the globe are frantically trying to develop a vaccine or a cure for COVID-19 while doctors are just about keeping the pandemic from overwhelming the entire world. On the other hand, many countries have found social distancing, using masks & gloves a way to curb the situation a little.

![Face Mask Detector ](https://github.com/Praveen76/Face-mask-detector-using-RetinaNet-model/blob/master/Data/FaceMaskDetector.png)

I recently had an idea to apply my deep learning knowledge to help the current situation a little. In this article, I’ll introduce you to the implementation of RetinaNet with little background & working on it.

# Directory Structure
* **Data :** This directory has input files that you'll need to important orginal Data. You can create your own dataset too. You can follow my [this article](https://towardsmachinelearning.org/web-scraping-using-selenium-with-python/) to create your own dataset for your deep learning tasks.
  *maskDetectorJPEGImages: This directory contains original data.
  * maskDetectorXMLfiles: This directory contained the xml files produced after annotation of images. Each xml file contains the coordinates of the bounding box.

* **keras-retinanet:** This directory is produced after installing keras-retinanet. You can check retinaNet-maskDetector.ipynb notebook to get more details on installation.
    * **snapshots:**  This directory under keras-retinanet directory will be used to save model's weights at different checkpoints.
* **maskDetectorClasses:** This file has been exporrted from the experiment . It contains the coordinates of the bounding boxes along with their classes. Please check notebook for more details.
* **maskDetectorClasses:**  This file contains the information about the classes involved, mask and noMask in our case study.
* **retinaNet-maskDetector.ipynb**: This is the python notebook that you can run to implement face mask detector on your own.

**Note**: Kindly note that I've tested it on a very small Dataset with very minimal epochs. You'll need much larger dataset and epochs to get better results and accuracy.

# Instructions for Installation
Download Dataset from the above Link and store the files in the data folder. Run any of the Python notebook according to the task desired

**Dependencies:**
* numpy: 1.18.1
* pandas: 1.0.1
* matplotlib: 3.1.3
* requests: 2.22.0
* PIL: 7.0.0
* keras_retinanet
* labelImg
* shutil
* urllib
* glob
* xml

The code has been tested on Windows system. It should work well on other distributions but has not yet been tested.

In case of any issue with installation or otherwise, please contact me on [Linkedin](https://www.linkedin.com/in/praveen-kumar-anwla-49169266/)

# **Article published on Analytics Vidhya:** 
* I've published a comprehensive case study on implementation of Face Mask Detector using RetinaNet Model. You can refer this [link](https://www.analyticsvidhya.com/blog/2020/08/how-to-build-a-face-mask-detector-using-retinanet-model/) to get more details.

# **Important learnings from implementation of Face mask detector using RetinaNet model**
* How to clone & install the keras-retinanet repository
* How to gather a large amount of Data for Deep learning tasks
* Create Dataset for your model training.
* Model Training
* Model Testing
* Final Notes
  
# **Important learnings from the article:**
* What is RetinaNet Model
* Need for RetinaNet Model
* The Architecture of RetinaNet
   * Backbone Network
   * Subnetwork for object Classification
   * Subnetwork for object Regression
* What is Focal Loss, and why it's important in object detection algorithms?



