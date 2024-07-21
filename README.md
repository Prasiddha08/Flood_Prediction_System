## Flood_Prediction_System
# Project Overview
This project aims to predict Flood Probability based on different characteristics of places using linear regression model. The project includes a Streamlit web application that allows users to input different tropographical and natural characteristics of the place with the help of a sidebar and get predictions.
# Project Details
The dataset used for this project includes various tropographical and various other properties of a place in a range of 0-10 such as:
 1.   MonsoonIntensity                 
 2.   TopographyDrainage                
 3.   RiverManagement                    
 4.   Deforestation                      
 5.   Urbanization                       
 6.   ClimateChange                      
 7.   DamsQuality                        
 8.   Siltation                         
 9.   AgriculturalPractices             
 10.   Encroachments                      
 11.  IneffectiveDisasterPreparedness    
 12.  DrainageSystems                    
 13.  CoastalVulnerability               
 14.  Landslides                         
 15.  Watersheds                        
 16.  DeterioratingInfrastructure        
 17.  PopulationScore                    
 18.  WetlandLoss                       
 19.  InadequatePlanning                 
 20.  PoliticalFactors                   
 21.  FloodProbability 

# Model
Linear Regression Model was trained on the basis of the features listed above, excluding the 'FloodProbability' column. 

# Streamlit App
The Streamlit app provides an interactive interface to input various properties of a place in a range of 0-10  and visualize the predictions. The app includes:
1. A form to input various properties of a place in a range of 0-10 using slider
2. A "Predict" button to generate prediction

# Installation
# Prerequisites
Ensure you have the following installed:

Python 3.1.2 or higher

Git
# Steps
1. Clone the repository
git clone https://github.com/Nehu2021/Food_Adulteration_Health_Risk_using_ML.git

3. Navigate to the project directory
Change your current working directory to the project directory.

cd Food_Adulteration

5. Install dependencies
Install the required packages using pip.

pip install -r requirements.txt

# Run the predictor

This model is pre-trained so simply run the predictor.

   streamlit run app.py
   
# If you want to train the model on your own:

1. Install Jupyter Notebook: If you haven't already installed Jupyter Notebook, you can do so using pip:

pip install notebook

2. Open the Notebook: Once Jupyter Notebook is installed, navigate to the directory where lung_cancer_analysis.ipynb is located using your command line or terminal.

3. Start Jupyter Notebook: Run the following command to start the Jupyter Notebook server:

jupyter notebook
