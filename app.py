import streamlit as st
from modelbit import get_inference

# Fungsi untuk prediksi menggunakan Modelbit
def predict_lung_cancer(data):
    processed_data = preprocess_input(data)
    response = get_inference(
        region="us-east-2.aws",
        workspace="22131tofanadinugroho",
        deployment="predict_lung_cancer",
        data=processed_data
    )
    return response

# Fungsi untuk preprocessing data
def preprocess_input(data):
    mapping = {"Yes": 2, "No": 1, "Male": 1, "Female": 2}
    return [
        mapping[data['gender']],
        data['age'],
        mapping[data['smoking']],
        mapping[data['yellow_fingers']],
        mapping[data['anxiety']],
        mapping[data['peer_pressure']],
        mapping[data['chronic_disease']],
        mapping[data['fatigue']],
        mapping[data['allergy']],
        mapping[data['wheezing']],
        mapping[data['alcohol_consuming']],
        mapping[data['coughing']],
        mapping[data['shortness_of_breath']],
        mapping[data['swallowing_difficulty']],
        mapping[data['chest_pain']],
    ]

# Sidebar dengan deskripsi dan ikon
st.sidebar.title("Navigasi")
st.sidebar.image("templates/lungCancer.jpg", width=90)
st.sidebar.header("Model Prediksi Kanker Paru")
st.sidebar.write(
    """
    Pilih halaman berikut untuk melihat penjelasan atau melakukan prediksi.
    """
)

# Menu navigasi
menu = st.sidebar.radio("Pilih Halaman", ["📄 Penjelasan : Melihat penjelasan analisis.", "🔍 Prediksi : Melakukan prediksi kanker paru."])

# Halaman Penjelasan
if menu == "📄 Penjelasan : Melihat penjelasan analisis.":
    st.title("Penjelasan Analisis")
    with open("templates/Kelompok6_PSD.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=800, scrolling=True)

# Halaman Prediksi
elif menu == "🔍 Prediksi : Melakukan prediksi kanker paru.":
    st.title("Prediksi Lung Cancer")
    st.write("Masukkan data di bawah ini:")

    # Layout input dalam 2 kolom
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col2:
        age = st.number_input("Age", min_value=1, max_value=87, step=1)
        st.markdown(
            """
            <span style="font-size: 16px; color: #888;">
                <i class="fa fa-info-circle" title="Masukkan usia Anda (antara 1 hingga 87 tahun)"></i>
            </span>
            """, 
            unsafe_allow_html=True
        )

    with col1:
        smoking = st.selectbox("Smoking", ["No", "Yes"])
    with col2:
        yellow_fingers = st.selectbox("Yellow Fingers", ["No", "Yes"])

    with col1:
        anxiety = st.selectbox("Anxiety", ["No", "Yes"])
    with col2:
        peer_pressure = st.selectbox("Peer Pressure", ["No", "Yes"])

    with col1:
        chronic_disease = st.selectbox("Chronic Disease", ["No", "Yes"])
    with col2:
        fatigue = st.selectbox("Fatigue", ["No", "Yes"])

    with col1:
        allergy = st.selectbox("Allergy", ["No", "Yes"])
    with col2:
        wheezing = st.selectbox("Wheezing", ["No", "Yes"])

    with col1:
        alcohol_consuming = st.selectbox("Alcohol Consuming", ["No", "Yes"])
    with col2:
        coughing = st.selectbox("Coughing", ["No", "Yes"])

    with col1:
        shortness_of_breath = st.selectbox("Shortness of Breath", ["No", "Yes"])
    with col2:
        swallowing_difficulty = st.selectbox("Swallowing Difficulty", ["No", "Yes"])

    with col1:
        chest_pain = st.selectbox("Chest Pain", ["No", "Yes"])

    # Data dikumpulkan ke dalam dictionary
    data = {
        "gender": gender,
        "age": age,
        "smoking": smoking,
        "yellow_fingers": yellow_fingers,
        "anxiety": anxiety,
        "peer_pressure": peer_pressure,
        "chronic_disease": chronic_disease,
        "fatigue": fatigue,
        "allergy": allergy,
        "wheezing": wheezing,
        "alcohol_consuming": alcohol_consuming,
        "coughing": coughing,
        "shortness_of_breath": shortness_of_breath,
        "swallowing_difficulty": swallowing_difficulty,
        "chest_pain": chest_pain,
    }

    # Tombol prediksi
if st.button("Predict"):
    try:
        result = predict_lung_cancer(data)
        prediction = result.get('data', 'Tidak ada hasil')
        
        if prediction.lower() == 'yes':
            st.success("Hasil Prediksi : Terdiagnosis Terkena Kanker Paru-paru")
        elif prediction.lower() == 'no':
            st.success("Hasil Prediksi : Terdiagnosis Tidak Terkena Kanker Paru-paru")
        else:
            st.warning("Hasil Prediksi tidak dapat dipastikan")
    except Exception as e:
        st.error(f"Error: {e}")