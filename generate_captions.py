import numpy as np
import pickle
from keras.applications.resnet50 import ResNet50, preprocess_input
from keras.preprocessing import image
from keras.models import Model
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Input, Dense, Dropout, Embedding, LSTM
from keras.layers.merge import add

model = ResNet50(weights="imagenet", input_shape=(3, 224, 224))
model_new = Model(input=model.input, output=model.layers[-2].output)
model = ResNet50(weights="imagenet",input_shape=(3,224,224))
model_new = Model(input=model.input,output = model.layers[-2].output)
model_new._make_predict_function()


def predict_captions(photo):
    in_text = "<s>"
    for i in range(max_len):
        sequence = [word_to_index[w] for w in in_text.split() if w in word_to_index]
        sequence = pad_sequences([sequence], maxlen=max_len, padding='post')

        ypred = model.predict([photo, sequence])
        ypred = ypred.argmax()
        word = index_to_word[ypred]
        in_text += ' ' + word
        if word == "<e>":
            break
    final_caption = in_text.split()[1:-1]
    final_caption = ' '.join(final_caption)

    return final_caption


def preprocess_img(img):
    img = image.load_img(img, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)

    img = preprocess_input(img)
    return img


def encode_img(img):
    img = preprocess_img(img)
    feature_vector = model_new.predict(img)
    feature_vector = feature_vector.reshape((-1,))
    return feature_vector


max_len = 74
vocab_size = 5121

embedding_matrix = None
with open("embedding_matrix.pkl", 'rb') as f:
    embedding_matrix = pickle.load(f)

word_to_index = None
with open("word_to_index.pkl", 'rb') as f:
    word_to_index = pickle.load(f)

index_to_word = None
with open("index_to_word.pkl", 'rb') as f:
    index_to_word = pickle.load(f)

input_img_features = Input(shape=(2048,))
inp_img1 = Dropout(0.3)(input_img_features)
inp_img2 = Dense(256, activation='relu')(inp_img1)

input_captions = Input(shape=(max_len,))
inp_cap1 = Embedding(input_dim=vocab_size, output_dim=50, mask_zero=True)(input_captions)
inp_cap2 = Dropout(0.3)(inp_cap1)
inp_cap3 = LSTM(256)(inp_cap2)

decoder1 = add([inp_img2, inp_cap3])
decoder2 = Dense(256, activation='relu')(decoder1)
outputs = Dense(vocab_size, activation='softmax')(decoder2)

model = Model(inputs=[input_img_features, input_captions], outputs=outputs)

model.layers[2].set_weights([embedding_matrix])
model.layers[2].trainable = False

model.load_weights("model_37.h5")
model._make_predict_function()

# In[66]:


# img_path = "/Users/paraskaushik/Desktop/FOOD/CODES/DATA_SCIENCE/Image Captioning Bot/8k/flickr8k/Flickr_Data/Flickr_Data/Images/"


# In[67]:


"""for i in range(15):
    id = np.random.randint(0,1000)
    all_image_names = list(os.listdir(img_path))
    img_name = all_image_names[id]
    photo_2048 = encode_img(img_path+img_name).reshape((1,2048))
    #photo_2048 = encoding_train[img_name].reshape((1,2048))

    i = plt.imread(img_path+img_name)
    caption = predict_captions(photo_2048)
    print(caption)

    plt.imshow(i)
    plt.axis("off")
    plt.show()"""


def give_caption(image_path):
    photo_2048 = encode_img(image_path).reshape((1, 2048))
    caption = predict_captions(photo_2048)
    return caption