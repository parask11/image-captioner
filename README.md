# Image Captioner

## Getting Started
It will generate captions according to the given images.
For example: 

![result1](/results/1.png)

![result2](/results/3.png)

![result3](/results/4.png)

## File descriptions
1) `app.py` Main code to run to create the server
2) `generate_captions.py` Python module that compiles the AI model and makes predictions.
3) `embedding_matrix.pkl` Matrix for the word embeddings of the vocabulary.
4) `train_descriptions.pkl` Dictionary to map image names to the captions for training data.
5) `word_to_index.pkl` Dictionary to map words in the vocabulary to their index numbers.
6) `index_to_word.pkl` Dictionary to map index number to their words in the vocabulary.
7) `results` Contains samples of results on testing.
8) `static` Stores images input by the user while generating captions.
9) `templates` Contains the `<index.html>` to generate the UI.
10) `preparing_data.ipynb` Jupyter Notebook to prepare the data for training.
11) `training_model.ipynb` Jupyter Notebook to train the model.
12) `generate_captions.ipynb`Jupyter Notebook to import all the essentials and generate the captions.

## External Data
1) `model_weights` Folder that contains all the models generated in 40 epochs during the training.(Link: `https://drive.google.com/open?id=1EzkEjTSQAAlKejyJAwRfKbKqBtDNHwv7`
2) `glove.6B.50d.txt` Text file to contain mapping of words to their corresponding 50-dimensional vector. (Link:
`https://drive.google.com/open?id=1mqHRTOyF87fHoiuRZwOlgcYwcCynQ5Ki`
3) `encoding_train_features.pkl` Dictionary to map training images to their corresponding 2048 dimensional vector. (Link: `https://drive.google.com/open?id=1qO4fgm8qUu0eIslMpg6oqqmcZil5qs9k`
4) `flickr30k_images` Training images and their captions. (Link: `https://www.kaggle.com/hsankesara/flickr-image-dataset`)

## Installation
1) Clone the repository.
`git clone https://www.github.com/parask11/image-captioner`

2) Go in the directory.
`cd image-captioner`

3) Install requirements.
`pip install -r requirements.txt` 

## Running

Run the python script.
`python app.py`

It will start a server.

Open the link from the browser.
`localhost:5000`

The UI will appear. Upload images and generate the captions!
