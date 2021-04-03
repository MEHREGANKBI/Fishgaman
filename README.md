# Fishgaman

## Table of contents:

- [Introduction](#introduction)

- [Why Fishgaman?](#why-fishgaman)

- [In-Depth methodology, instructions and warnings](#in-depth-methodology-instructions-and-warnings)

- [Dependencies](#dependencies)

- [Acknowledgements](#acknowledgements)


## Introduction

Fishgaman is an web automation based project aimed to solve the problem of having to check non-trivial stuff repeatitively. Using fishgaman, we can automate the boring and error process so that the information you need is always at reach. As of now, it regularly checks my internet credit info and shows them on my desktop. No need to login, wait and then read. It's at the corner of my screen and I check it for a split second whenever I want. 

## Why Fishgaman?

This goes back to the reason I started this project. My ISP, Pishgaman tose-e ertebatat, is not well known for it's high quality service and I as a customer, usually don't have many options to choose. So pretty much, I'm stuck with them and as long as I'm stuck with them, I have to deal with internet data caps. But why automate something as simple as checking your internet plan. To that I'll say, becuase it's no simple task to check your internet plan up to 14 times a day manually and thus, I never did it. As a result, I had no history of my internet usage and no recent detail on my internet plan. How else would I investigate why my monthly internet plan was terminated due to data cap just days after renewing it. So now you have a good idea of why I had to fish for my internet plan info on pishgaman's website, hence the name fishgaman.

## In-Depth methodology, instructions and warnings

**NOTE: Although the folder of the repo is not exactly the same as the one shown in the video, the idea is the same. The only thing that is different is the path to the files in the configuration dictionary**

Don't forget to configure the **fisher.sh** and the **usps.py** files. More info available in the YouTube video. **Click the GIF below to watch the video.** Direct link to the YouTube video in case the GIF does not work: https://youtu.be/-u7Mzx3W_Bs

[<img src="https://drive.google.com/u/0/uc?id=1ZKKfgNYAPjh6zxPlo4B7Mk-7AGwl3OUi&export=download" width="640" height="360">](http://www.youtube.com/watch?v=-u7Mzx3W_Bs "In Depth video")



## Dependencies

python 3.8.5 (including its default re, os, subprocess modules) 

NumPy 1.19.4

Selenium 3.141.0

Pillow(aka PIL) 7.0.0

Alternatively, you could use the "requirements.txt" file in the repo for the "pip{3} install -r requirements.txt" command to set up your environment for the scripts to run properly.


## Acknowledgements

I'd like to thank Mehdi Javidan for his helpful guidance.




This readme.md file will be updated for info on documentation, instruction and proof of concept. 
