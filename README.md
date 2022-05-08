# FarmAI
One stop solution to help farmers to make better decisions

Agriculture is one of important sector in many countries. Major challenge in agriculture is to
increase the production in the farm and deliver it to the end customers with best possible
price and good quality. After doing some research on the internet, we came to know these are
three major problems faced by farmers these days.

  1. Low crop yield – because most of unaware of the fact
  that soil condition and weather conditions may change
  with time.
  2. Less profit gained- Unaware of current market price
  3. Loss due to lack of awareness of which pesticides to use.
 
In order to solve these problems, We developed a machine learning model using EXTRA
Trees algorithm which predicts crop that should be grown based given conditions such as
Nitrogen, Phosphorus, Pottasium, rainfall, temperature, moisture, PH and humidity as
input. We have analysed over 2200 rows dataset of around 25 crops and classified into
groups, trained a model to predict which crop has best crop yield. Then we developed
android application as a prototype which has three modules which are meant for
predicting crops, suggesting pesticides for a given crop and displaying current market price
of crop. Later we intergrated the ML model with an android app using Firebase realtime databases.

Technical implementation:

Dataset:
  7 attributes-Nitrogen, Phosphorus, Pottasium, rainfall, temperature, humidity and crop type.
  Out of which 6 attributes except crop type is used as input and crop type is used as target
  output.Dataset is divided into 8:2 ratio, 80 percent is used for training and 20% is used
  for testing.

Result:
After training the model, when the model tested upon test data, obtained the
accuracy around 98 percent.

Mobile App:
 Used android studio to develop a mobile app using kotlin and added firebase inorder to intergrate
 it with ML model that predicts crop.

Use cases:
  1. This application can be used by any farmer who has access to a mobile phone.  
  2. For checking the best crop, tips, pesticides we need to connect to the internet.
  3. Not only the farmer, anyone who has a mobile phone and access to the internet 
     can help the farmers across the country by providing information required for them.
 
Advantages :
  Decreases the loss incurred by farmers. 
  Increases the crop production. 
  Decreases the cost of food and other items bringing stability in prices. 

# Instructions
1. Mobile app folder contains the app code which you can import in android studio and run.
2. Farmai.apk is the android app which you can install and run on android phone
3. Crop_recommendation is the dataset we used to train Machine learning model
4. farmai.py contains the code to train ML model and send and receive data from firebase

In order to run the application, install farmai app in the mobile. Enter the details and click on send data. Data gets updated in firebase database then run the farmai.py python program recommended crop is sent back to firebase. Now click on predict in mobile app, you can see the predicted crop. 

