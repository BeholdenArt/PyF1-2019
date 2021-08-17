<!-- INTRODUCTION -->
<br />
<pre>
<strong>EXPECTATIONS</strong>                                                  <strong>REALITY</strong>
</pre>
<p align="left">
  <a href="https://github.com/BeholdenArt/pyF1-2019">
    <img src=https://media.giphy.com/media/9F2VWRiJypeBq/source.gif alt="Logo" width="480" height="300">
  </a>
  <a href="https://github.com/BeholdenArt/pyF1-2019">
    <img src="https://media.giphy.com/media/Y1ggBG6wpBdwA/source.gif" alt="Logo" width="480" height="300">
  </a>


  <h2 align="center">AI Plays F1-2019(PC) Game</h2>

  <p align="center">
    An AI that drives the car in the F1-2019(PC) game on the Bahrain map.
    <br />
    <br />
    <a href="https://github.com/BeholdenArt/pyF1-2019">View Demo</a>
    ·
    <a href="https://github.com/BeholdenArt/pyF1-2019/issues">Report Bug</a>
    ·
    <a href="https://github.com/BeholdenArt/pyF1-2019/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<br />
<details open="open">
  <summary><h2 style="display: inline-block">TABLE OF CONTENTS</h2></summary>
  <ol>
    <li>
      <a href="#ABOUT-THE-PROJECT">ABOUT THE PROJECT</a>
      <ul>
        <li><a href="#Built-with">Built With</a></li>
      </ul>
    </li>
      <a href="#GETTING-STARTED">GETTING STARTED</a>
      <ul>
        <li><a href="#Prerequisite">Prerequisite</a></li>
        <li><a href="#Installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#USAGE">USAGE</a></li>
    <li><a href="#CONTRIBUTION">CONTRIBUTION</a></li>
    <li><a href="#CONTACT-ME">CONTACT ME</a></li>
  </ol>
</details>



<br><br><br>
<!-- ABOUT THE PROJECT -->
## ABOUT THE PROJECT

<p align="center">
  <a href="https://github.com/BeholdenArt/pyF1-2019">
    <img src="videos/demo1.gif" alt="demo1" width="960" height="540">
  </a>
  GIF of AI playing F1-2019 game on it's own. 
</p>
<br />

 This project uses the <a href="https://en.wikipedia.org/wiki/AlexNet">AlexNet model</a> as the brain of the operation and uses [image of road, key pressed] as input and predicts the input car should make to stay on the track and makes that move in-game. 

<!--
 ### To see more clip of AI driving the car, Kindly visit the youtube video provided below.
<p align="center">
  <a href="https://www.youtube.com/channel/UCipSxT7a3rn81vGLw9lqRkg?sub_confirmation=1"><img alt="Youtube" title="Youtube" src="https://img.shields.io/badge/-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white"/></a>
</p>
 -->


<br>
<!-- BUILT WITH -->
## Built With
<ol>
  <li> <a href="https://docs.opencv.org/4.5.2/" target="_blank">OpenCV</a> - To capture the Game screen. </li> 
  <li> <a href="http://timgolden.me.uk/pywin32-docs/" target="_blank">win32api</a> - To identify keys pressed. </li> 
  <li> <a href="https://www.tensorflow.org/guide" target="_blank">Tensorflow-GPU</a>, <a href="http://tflearn.org/" target="_blank">Tflearn</a> - To use the AlexNet model. </li>
  <li> <a href="https://numpy.org/doc/" target="_blank">NumPy</a> - To convert keypress into a list. </li>
</ol>
  <br>


<br><br><br>
<!-- GETTING STARTED -->
## GETTING STARTED

<!-- PREREQUISITE -->
## Prerequisite 
<p align="left" > 
    &emsp;
   <a href="https://www.python.org" target="_blank">
    <img alt="Python" src="https://img.shields.io/badge/Python%20-%2314354C.svg?logo=python&logoColor=white">
  </a>
  &emsp; 
    <a href="https://jupyter.org/install"><img alt="Jupyter" src="https://img.shields.io/badge/Jupyter%20-%23F37626.svg?logo=Jupyter&logoColor=white"></a>
  &emsp;
  </a>
</p>

<br>
<!--INSTALLATION -->
## Installation
<ol>
  <li> Clone the repo </li>
  
   ```sh
   git clone https://github.com/BeholdenArt/pyF1-2019.git
   ```
  
  <li> Install requirements </li>
  <p>Install (the latest) <a href="https://developer.nvidia.com/cuda-downloads" alt="nvidia cuda toolkit">CUDA Toolkit</a> and <a href="https://developer.nvidia.com/cudnn" alt="nvidia cuDNN">cuDNN</a> if you want to train the model using GPU (Recommended).</p> 
   
  ```sh
   pip3 install -r requirements.txt
   pip3 install tensorflow-gpu tensorflow_addons
   ```
  
</ol>



<br><br><br>
<!-- USAGE EXAMPLES -->
## USAGE

To use this project.
*  Complete the getting started part. </li>
*  Open the game in the lowest resolution and place it on the top left side of the monitor. </li>

*  To test the model </li>
    ```
    python Test-Model.py
    ```

*  To collect more data </li>
    ```
    python Collect-Data.py
    ```

*  To train the model </li>
    ```
    python Train-Model.py
    ```



<br><br><br>
<!-- CONTRIBUTING -->
## CONTRIBUTION
Please refer to each project's style and contribution guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!



<br><br><br>
## CONTACT ME

<p align="center">
	<a href="mailto:priyanshub5645@gmail.com"><img src="https://img.icons8.com/bubbles/50/000000/gmail.png" alt="Gmail"/></a>
	<a href="https://github.com/BeholdenArt"><img src="https://img.icons8.com/bubbles/50/000000/github.png" alt="GitHub"/></a>
	<a href="https://linkedin.com/in/priyanshu-bairwa-827432190"><img src="https://img.icons8.com/bubbles/50/000000/linkedin.png" alt="LinkedIn"/></a>
	<a href="https://www.facebook.com/priyanshu.bairwa.129794"><img src="https://img.icons8.com/bubbles/50/000000/facebook-new.png" alt="Facebook"/></a>
	<a href="https://instagram.com/theblockedguy"><img src="https://img.icons8.com/bubbles/50/000000/instagram.png" alt="Instagram"/></a>
	
</p>
