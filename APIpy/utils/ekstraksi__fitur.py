# fungsi untuk Ekstraksi fitur leksikal sederhana
def extract_lexical_features(text):
    num_words = len(text.split())
    num_chars = len(text)
    ratio_caps = sum(1 for c in text if c.isupper()) / (len(text) + 1e-8)
    num_exclamation = text.count('!')
    num_question = text.count('?')
    num_symbols = sum(1 for c in text if not c.isalnum() and not c.isspace())
    return [num_words, num_chars, ratio_caps, num_exclamation, num_question, num_symbols]

# fungsi untuk eksrtaksi fitur berbais URL
def extract_url_features(text):
    num_urls = text.lower().count('http') + text.lower().count('www') + text.lower().count('bit.ly')
    has_shortened_url = 1 if 'bit.ly' in text.lower() else 0
    return [num_urls, has_shortened_url]
