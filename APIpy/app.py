from flask import Flask, request, jsonify
import joblib
import numpy as np
from utils.processing import preprocess
from utils.ekstraksi__fitur import extract_lexical_features, extract_url_features

# Load model dan vectorizer
model = joblib.load('model/v9/hashing_vectorizer.pkl')
vectorizer = joblib.load('model/v9/svm_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Format: {"text": "pesan WhatsApp"}
    text = data.get('message', '')  # Ambil teks dari permintaan

    # 1. Preprocessing teks
    processed = preprocess(text)
    #print("Original:", text)
    #print(preprocess("Processed (VSCode): SLMT!! No Anda men-dpt hadiah dr:pengundian PT.TELKOMSEL No pin b89c7... Untuk melihat Hadiah Anda, silakan klik : www.telkomselpoin2222.webs.com"))

    # 2. TF-IDF vektorisasi
    tfidf_features = vectorizer.transform([processed]).toarray()  # shape: (1, 4889)

    # 3. Ekstraksi fitur leksikal dan URL (masing-masing list, ubah ke array)
    lex_features = np.array(extract_lexical_features(processed)).reshape(1, -1)  # shape: (1, 6)
    url_features = np.array(extract_url_features(processed)).reshape(1, -1)      # shape: (1, 2)

    # 4. Gabungkan seluruh fitur (total: 1 x 4897)
    all_features = np.concatenate([tfidf_features, lex_features, url_features], axis=1).reshape(1, -1)

    # ✅ CETAK UKURAN & ISI FITUR
    print("Processed:", processed)
    print("TF-IDF Nonzero:", np.count_nonzero(tfidf_features))
    print("TF-IDF shape:", tfidf_features.shape)
    print("Lexical:", lex_features)
    print("URL:", url_features)
    print("Final shape:", all_features.shape)
    print("Split processed words:", processed.split())  # tambahan: untuk cek isinya
    #print(preprocess("Selamat!anda m-dptkan Hadiah Cek Tunai Rp. 15jt dari INDOSAT Pin_anda 277fg49 U/info pengambilan Hadiah kunjungi website indosat www.hadiah-indosat.blogspot.com"))


    # 5. Prediksi
    prediction = model.predict(all_features)

    # 6. Label mapping
    label_mapping = {0: 'Normal', 1: 'Penipuan', 2: 'Promosi'}

    # 7. Kembalikan hasil prediksi
    return jsonify({
        'prediction': int(prediction[0]),
        'label': label_mapping[int(prediction[0])]
    })

if __name__ == '__main__':
    app.run(debug=True)


