import streamlit as st 
import numpy as np 
import tensorflow as tf 
import pickle 
from tensorflow.keras.models import load_model 
from tensorflow.keras.preprocessing.sequence import pad_sequences 

model = load_model('model_lstm.keras')

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
    
def predict_next_word(model, tokenizer, text, max_sequence_len):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) >= max_sequence_len:
        token_list = token_list[:max_sequence_len-1]
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted = model.predict(token_list, verbose = 0)
    predicted_word_index = np.argmax(predicted)
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return None

st.title('Next Word Prediction ')
input_text = st.text_input("Enter with sequence of words", "To be or not to ")
if st.button("Predict Next Word"):
    max_sequence_len = model.input_shape[1] + 1
    next_word = predict_next_word(model, tokenizer, input_text, max_sequence_len)
    st.write(f'Next Word : {next_word}')