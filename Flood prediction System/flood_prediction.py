import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load the saved model
model_path = 'C:\\Users\\USER\\Desktop\\Flood prediction System\\ML_model\\linear_regression_model.pkl'
model = joblib.load(model_path)

# Extract feature names from the model if they are available
try:
    expected_columns = model.feature_names_in_
except AttributeError:
    st.error("The model does not contain feature names. Please ensure the model is trained with feature names.")

def main():
    # Set the title of the web app
    st.title('Flood Prediction')

    # Add a description
    st.write('Enter all information to predict flood probability.')

    # Create columns for layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Add input fields for features
        place_name = st.text_input('Place Name')
        MonsoonIntensity = st.slider("Monsoon Intensity", 0, 10, 3)
        TopographyDrainage = st.slider("Topography Drainage", 0, 10, 2)
        RiverManagement = st.slider("River Management", 0, 10, 2)
        Deforestation = st.slider("Deforestation", 0, 10)
        Urbanization = st.slider("Urbanization", 0, 10)
        ClimateChange = st.slider("Climate Change", 0, 10, 2)
        DamsQuality = st.slider("Dams Quality", 0, 10, 2)
        Siltation = st.slider("Siltation", 0, 10)
        AgriculturalPractices = st.slider("Agricultural Practices", 0, 10)
        Encroachments = st.slider("Encroachments", 0, 10)
        IneffectiveDisasterPreparedness = st.slider("Ineffective Disaster Preparedness", 0, 10)
        DrainageSystems = st.slider("Drainage Systems", 0, 10)
        CoastalVulnerability = st.slider("Coastal Vulnerability", 0, 10)
        Landslides = st.slider("Landslides", 0, 10)
        Watersheds = st.slider("Watersheds", 0, 10)
        DeterioratingInfrastructure = st.slider("Deteriorating Infrastructure", 0, 10)
        PopulationScore = st.slider("Population Score", 0, 10)
        WetlandLoss = st.slider("Wetland Loss", 0, 10)
        InadequatePlanning = st.slider("Inadequate Planning", 0, 10)
        PoliticalFactors = st.slider("Political Factors", 0, 10)

    # Prepare input data as a DataFrame
    input_data = pd.DataFrame({
        'MonsoonIntensity': [MonsoonIntensity],
        'TopographyDrainage': [TopographyDrainage], 
        'RiverManagement': [RiverManagement],
        'Deforestation': [Deforestation],
        'Urbanization': [Urbanization],
        'ClimateChange': [ClimateChange],
        'DamsQuality': [DamsQuality],
        'Siltation': [Siltation],
        'AgriculturalPractices': [AgriculturalPractices],
        'Encroachments': [Encroachments],
        'IneffectiveDisasterPreparedness': [IneffectiveDisasterPreparedness],
        'DrainageSystems': [DrainageSystems],
        'CoastalVulnerability': [CoastalVulnerability],
        'Landslides': [Landslides],
        'Watersheds': [Watersheds],
        'DeterioratingInfrastructure': [DeterioratingInfrastructure],
        'PopulationScore': [PopulationScore],
        'WetlandLoss': [WetlandLoss],
        'InadequatePlanning': [InadequatePlanning],
        'PoliticalFactors': [PoliticalFactors],
    })

    input_data = input_data[expected_columns]

    # Prediction and results section
    with col2:
        st.subheader('Prediction')
        if st.button('Predict'):
            prediction = model.predict(input_data)[0]
            
            # Assuming a threshold to classify the linear regression output as flood or no flood
            threshold = 0.5  # Example threshold, adjust as needed
            flood_risk = 'Flood' if prediction >= threshold else 'No Flood'
            probability = prediction  # Treating the regression output as a probability for simplicity

            st.write(f'Prediction for {place_name}: {flood_risk}')
            st.write(f'Predicted Value: {prediction:.2f}')

            # Plotting
            fig, axes = plt.subplots(2, 1, figsize=(8, 16))

            # Plot Flood/No Flood probability
            sns.barplot(x=['No Flood', 'Flood'], y=[1 - probability, probability], ax=axes[0], palette=['blue', 'red'])
            axes[0].set_title('Flood Probability')
            axes[0].set_ylabel('Probability')

            # Plot Flood/No Flood pie chart
            axes[1].pie([1 - probability, probability], labels=['No Flood', 'Flood'], autopct='%1.1f%%', colors=['blue', 'red'])
            axes[1].set_title('Flood Probability Pie Chart')

            # Display the plots
            st.pyplot(fig)

            # Provide recommendations
            if prediction >= threshold:
                st.warning(f"{place_name} is at risk of flooding. Take necessary precautions!")
            else:
                st.success(f"{place_name} is not likely to flood. Stay prepared though!")

if __name__ == '__main__':
    main()