import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from utils.processing import preprocess
import joblib

def train_model_svm_with_extra_features():
    # Baca dataset
    df = pd.read_csv('data/v3/dataset_v2.csv')

    # Cek kolom dan hapus NaN
    print("Kolom dalam dataset:", df.columns)
    df.dropna(subset=['Teks', 'Label'], inplace=True)

    # Preprocessing
    texts = df['Teks'].tolist()
    labels = df['Label'].tolist()
    processed_texts = [preprocess(text) for text in texts]

    # TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000)
    tfidf_features = vectorizer.fit_transform(processed_texts).toarray()
    tfidf_df = pd.DataFrame(tfidf_features, columns=vectorizer.get_feature_names_out())

    # Gabungkan Semua Fitur
    all_features_df = pd.concat([tfidf_df], axis=1)
    X = all_features_df

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

    # Training
    svm_model = SVC(kernel='linear', C=1, random_state=42, decision_function_shape='ovr')
    svm_model.fit(X_train, y_train)

    # Prediksi dan evaluasi
    y_pred = svm_model.predict(X_test)
    print("Akurasi (dengan fitur tambahan):", accuracy_score(y_test, y_pred))
    print("Presisi (dengan fitur tambahan):", precision_score(y_test, y_pred, average='weighted'))
    print("Recall (dengan fitur tambahan):", recall_score(y_test, y_pred, average='weighted'))
    print("F1 Score (dengan fitur tambahan):", f1_score(y_test, y_pred, average='weighted'))
    print("Laporan Klasifikasi (dengan fitur tambahan):\n", classification_report(y_test, y_pred))

    # Buat confusion matrix
    cm = confusion_matrix(y_test, y_pred, labels=svm_model.classes_)

    # Simpan model dan vectorizer (yang sekarang bekerja dengan semua fitur)
    joblib.dump(svm_model, 'svm_model_with_extra_features.pkl')
    # Kita perlu menyimpan vectorizer TF-IDF saja karena fitur lainnya dihitung langsung
    joblib.dump(vectorizer, 'tfidf_vectorizer_with_extra_features.pkl')
    # simpan model ekstrak fitur leksikal
    #joblib.dump(lexical_df, 'lexical_features_df.pkl')
    # simpan model ekstrak fitur URL
    #joblib.dump(url_df, 'url_features_df.pkl')
    print("Model dengan fitur tambahan dan TF-IDF vectorizer disimpan.")

    # Tampilkan confusion matrix
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=svm_model.classes_)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Confusion Matrix (dengan fitur tambahan)")
    plt.show()

    return all_features_df, tfidf_df