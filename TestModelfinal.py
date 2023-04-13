from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#Loading the model
def isClickbait(str):
    
        model = keras.models.load_model('model.h5')

        maxlen=500
        vocab_size = 5000
        tokenizer = Tokenizer(num_words=vocab_size)

        #Input list for testing
        test = [str]

        #Input string from user
        '''print("Enter the headline to check whether clickbait or not: \n")
        inp = input("Enter the headline : ")
        test.append(inp)'''

        token_text = pad_sequences(tokenizer.texts_to_sequences(test), maxlen=maxlen)
        preds = [round(i[0]) for i in model.predict(token_text)]
        for (text, pred) in zip(test, preds):
                if(pred == 1.0):
                        return 1
                else:
                        return 0
                #label = 'Clickbait' if pred == 1.0 else 'Not Clickbait'
                #print("{} - {}".format(text, label))
        

result = isClickbait("18 Easy And Delicious One-Pan Breakfasts")
print("Result = ", result)