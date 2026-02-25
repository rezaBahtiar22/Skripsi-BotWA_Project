import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Download stopwords jika belum tersedia
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from nltk.corpus import stopwords

# Inisialisasi stemmer
stop_words = set(stopwords.words('indonesian'))
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Membaca kamus normalisasi
kamus_normalisasi = pd.read_csv('data/v3/kamus_normalisasi_v3.csv')

# Mengubah ke dictionary: {'gk': 'tidak', ...}
normalisasi_dict = dict(zip(kamus_normalisasi['kesalahan penulisan(typo)/penyingkatan kata'], kamus_normalisasi['baku']))

print("Kolom CSV:", kamus_normalisasi.columns.tolist())
print("Contoh kamus:", list(normalisasi_dict.items())[:5])


def preprocess(text):
    if isinstance(text, str):

        # Case folding
        text = text.lower()

        # Hapus tanda baca
        text = re.sub(r'[\/\-_]', ' ', text)              # Ganti '/', '-', '_' dengan spasi
        text = re.sub(r'[^\w\s]', ' ', text)               # Hapus karakter selain huruf, angka, dan spasi
        text = re.sub(r'\s+', ' ', text).strip()          # Hapus spasi berlebih


        # Tokenisasi
        words = text.split()

        # Normalisasi
        normalized_words = [normalisasi_dict.get(word, word) for word in words]

        # Stopword removal
        filtered_words = [word for word in normalized_words if word not in stop_words]

        # Stemming
        stemmed_words = [stemmer.stem(word) for word in filtered_words]

        return " ".join(stemmed_words)
    return ""

