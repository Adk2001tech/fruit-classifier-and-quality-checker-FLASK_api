# Healthy Fruit Lead App 
## Table of Content
* [Demo](#demo)
* [Overview](#overview)
* [Motivation/Purpose](#Motivation/Purpose)
* [Technical Aspect](#technical-aspect)
* [Data collection](#data-collection)
* [Installation](#installation) 
* [Run](#run)
* [Deployement on Heroku](#deployement-on-heroku)
* [Directory Tree](#directory-tree)
* [Technologies Used](#technologies-used)
* [Team](#team)
* [License](#license)

## Demo
Link:<br> https://fruit-classifier-quality-check.herokuapp.com
<br>
<br>
 <img target="_blank" src="https://user-images.githubusercontent.com/64481847/88918432-0dabc400-d287-11ea-9be6-8188eca807f0.gif" width="800px">


![](https://forthebadge.com/images/badges/made-with-python.svg) [![forthebadge](https://forthebadge.com/images/badges/validated-html5.svg)](https://forthebadge.com)


## Overview
* **Simple Flask app fitted with Deep Conv. neural network model which is able to distinguish between real world images of Apples, Bananas, Oranges with predicting weather the fruit in image is Fresh or Rotten with respective probabilities.**<br>
* **Data to train this DNN is collected in (`/data`) folder, which is done with the help of google search and downloading each image from it. This section is more explored in  'Data collection' topic below**

## Motivation/Purpose
After completing the 4th course(CNN) of deep learning specialization. I was super excited to implement the knowledge I gained in practical and productional way by doing an **end to end project** with following purposes.
1. This application/technique can be applied to **material selection procedure** in productional sector of companies making... 
<ul>
	<li>Fruit juices</li>
	<li>Pickles</li>
	<li>Tomato sauces</li>
	<li>etc. in commercial scale.</li>
</ul>
2.  Want to give enlightenment to beginners in learning flask as well as to train DNN and hypertune it to get better performance !<br>
3. Want to make more advancement in this project to serve the dealers who work in food checking & transportation, So they can monitor/check the condition of their stock at any time they want.

## Technical Aspect
#### This project is divided into Four major parts:
1. Train deep CNN model from **kaggle** on basic and clear images of our targets which I want to classify.
**Purpose behind this approach is to let our model figure out the basic lines, curves, edges, etc first and then retrain it
for classifying my target on real world images!!**

2. Retraining model on real world data/images and hypertune it for better performance.
3. Setting up Frontend for website.
4. Building and hosting a Flask web app on Heroku(Platform as a service)

## Data collection
As we know *data* is building block of Data science!<br>
I had collected around 400+ unique images of fruits and 400+ images of for quality detection. You can download it for your project from 
(`/data`) folder.<br>
<div class="row">
  <div class="col">
     <img target="_blank" src="https://user-images.githubusercontent.com/64481847/89262299-0ac91e80-d64d-11ea-9138-6dd297806f96.jpg" width=400>
  </div>
  <div class="col">
        <img target="_blank" src="https://user-images.githubusercontent.com/64481847/89262116-cf2e5480-d64c-11ea-8157-eef2aea3b817.jpg" width=400>
  </div>
</div>




## Installation
The Code is written in Python 3.7 in an anaconda environment. For anaconda instalation click <a href="https://www.anaconda.com/products/individual">here</a>.To make new environment in anaconda run following commands in your **Anaconda Prompt**.
```
conda create -n your_env_name python=3.7.x
```
## Run
After successfully creating anaconda environment, install the required packages and libraries by running this command in the project directory after cloning the repository:
```
pip install -r requirements.txt
```
then by running the following command, it will host this page in your local port and will also give you local link, which you can put in any web browser.
```
python app.py
``` 

## Deployement on Heroku
Vist <a href="Deployement on Heroku">here</a> for details.

## Directory tree
------


## Technologies Used
<img target="_blank" src="https://blog.keras.io/img/keras-tensorflow-logo.jpg" width=400>
<br><img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=270><img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280><img target="_blank" src="https://kazoo.jp/wpkazoo2019/wp-content/uploads/2018/05/bootstrap4.png" width=270>

