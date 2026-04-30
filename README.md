# Music-Genre-Classification

This repository consists of the data and Python code for the multi-class classification problem to predict music genre based on song features. The project explores various modeling techniques, ranging from traditional statistical classifiers to deep learning architectures, to predict musical genres based on audio features.

The goal of this project is to evaluate the performance of different classification algorithms on the GTZAN "Music Genre Classification" dataset. We implemented and compared several models, including:

- Naive Baseline model

- Ensemble Methods: Random Forest, XGBoost

- Instance-based: K-Nearest Neighbors (KNN)

- Deep Learning: Convolutional Neural Networks (CNN)

## About the Data

The [GTZAN dataset](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification/data) is a widely-used public dataset for music genre classification. It consists of 1000 audio files and their audio files and waveform visualizations, along with about 50 numerical features. 

## Repository Organization

i. `data/`: From the Kaggle dataset, sources `images_original` (consists of mel spectrogram images) and `features_3_sec.csv` and `features_30_sec.csv` (numerical features of the data). `remap.py` re-organizes the image data into three folders for each of the music genres we would like to use for the classfication problem.

ii. `EDA_and_PCA.ipynb`: Conducts exploratory data analysis and sdimensionality reduction to understand feature importance and variance. Outputs `data\final_df.csv` with remapped data points into three genres.

iii. `Naive_Baseline_model.ipynb`: Builds the initial benchmark model using assumptions based on inferences made from EDA and PCA.

iv. `KNN_model.ipynb` `RandomForest.ipynb`, `xgboost.ipynb`: Implements traditional machine learning models with hyperparameter tuning.

v. `CNN.ipynb`: Deep learning approach touched on briefly, which uses audio spectrograms for classification.

`best_cnn_weights.keras` saved weights for the CNN model to ensure reproducibility without retraining.

## Reproducibility

To run the notebooks in this repository, follow these steps to ensure all dependencies are met.

- Python 3.8+

- The following libraries are required and the folloing text may be put into the terminal to install them

`pip install pandas numpy matplotlib seaborn scikit-learn xgboost tensorflow librosa`

## AI Citation

Some code and material in this repository has been inspired by prompts given to AI models like Claude and Gemini.