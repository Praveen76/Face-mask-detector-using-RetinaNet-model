# Build Face-mask-detector-using-RetinaNet-model

We are grappling with a pandemic that’s operating at a never-before-seen scale. Researchers all over the globe are frantically trying to develop a vaccine or a cure for COVID-19 while doctors are just about keeping the pandemic from overwhelming the entire world. On the other hand, many countries have found social distancing, using masks & gloves a way to curb the situation a little.

![Face Mask Detector ](https://github.com/Praveen76/Face-mask-detector-using-RetinaNet-model/blob/master/FaceMaskDetector.png)

I recently had an idea to apply my deep learning knowledge to help the current situation a little. In this article, I’ll introduce you to the implementation of RetinaNet with little background & working on it.

# Directory Structure
* **Data :** This directory has input files that you'll need to important orginal Data. You can import this data from [Kaggle contest](https://www.kaggle.com/datasets/sudalairajkumar/covid19-in-india?select=StatewiseTestingDetails.csv) as well. However, I'll encourage you to explore Ministry of Home Affairs, India [website](https://www.mohfw.gov.in/), considering the data is coming from there only.
* **Processed Data:** This directory has data that has been produced during the experiment. You can run the attached python notebook for better understanding.
* **One Way ANOVA Test.ipynb:** This will demonstrate One-Way ANOVA test on real time COVID-19 Data.
* **Two Way ANOVA Test.ipynb:**  This will demonstrate Two-Way ANOVA test on real time COVID-19 Data.

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

# **Implementation of Face mask detector using RetinaNet model**
* How to clone & install the keras-retinanet repository
* How to gather a large amount of Data for Deep learning tasks
* Create Dataset for your model training.
* Model Training
* Model Testing
* Final Notes
  
# **Important learnings:**
* What is RetinaNet Model
* Need for RetinaNet Model
* The Architecture of RetinaNet
   * Backbone Network
   * Subnetwork for object Classification
   * Subnetwork for object Regression
* What is Focal Loss, and why it's important in object detection algorithms?



