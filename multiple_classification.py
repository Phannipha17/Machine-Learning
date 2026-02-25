# ---------------------- STRESS ----------------------
if selected == 'Stress':

    st.title('Stress Prediction')

    # ใช้ number_input แทน text_input
    Age = st.number_input('Age', min_value=0.0)
    Gender = st.number_input('Gender (encoded)', min_value=0.0)
    Occupation = st.number_input('Occupation (encoded)', min_value=0.0)
    Device_Type = st.number_input('Device_Type (encoded)', min_value=0.0)
    Daily_Phone_Hours = st.number_input('Daily_Phone_Hours', min_value=0.0)
    Social_Media_Hours = st.number_input('Social_Media_Hours', min_value=0.0)
    Work_Productivity_Score = st.number_input('Work_Productivity_Score', min_value=0.0)
    Sleep_Hours = st.number_input('Sleep_Hours', min_value=0.0)
    App_Usage_Count = st.number_input('App_Usage_Count', min_value=0.0)
    Caffeine_Intake_Cups = st.number_input('Caffeine_Intake_Cups', min_value=0.0)
    Weekend_Screen_Time_Hours = st.number_input('Weekend_Screen_Time_Hours', min_value=0.0)

    if st.button('Predict'):

        input_data = [[
            Age,
            Gender,
            Occupation,
            Device_Type,
            Daily_Phone_Hours,
            Social_Media_Hours,
            Work_Productivity_Score,
            Sleep_Hours,
            App_Usage_Count,
            Caffeine_Intake_Cups,
            Weekend_Screen_Time_Hours
        ]]

        # เช็คจำนวน feature ก่อน predict
        if len(input_data[0]) == stress_model.n_features_in_:

            stress_predict = stress_model.predict(input_data)

            if stress_predict[0] == 0:
                result = "Low Stress"
            else:
                result = "High Stress"

            st.success(result)

        else:
            st.error(f"Model expects {stress_model.n_features_in_} features "
                     f"but got {len(input_data[0])}")