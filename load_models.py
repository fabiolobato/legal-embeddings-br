#pip install gensim

## imports
from gensim.models import KeyedVectors
import logging
import numpy as np
import pandas as pd


def load_models(path,model_name, vector_dim = [],epochs = [],nn_types = []):
  models = {}
  for v in vector_dim:
    for nn in nn_types:
      for epoch in epochs:
        if model_name == 'fasttext':
          if nn == 1:
            arch = 'sg'
          else:
            arch = 'cbow'
          name_model_all = 'ft_'+arch+'_dim'+str(v)+'_epochs'+str(epoch)
          print(name_model_all)
          path_local = path+'/'+model_name+'/'+name_model_all+'.txt'
          #print(path_local)
          models[name_model_all] = KeyedVectors.load_word2vec_format(path_local, binary=False)
        elif model_name == 'word2vec':
          if nn == 1:
            arch = 'sg'
          else:
            arch = 'cbow'
          name_model_all = 'w2v_'+arch+'_dim'+str(int(v))+'_epochs'+str(epoch)
          print(name_model_all)
          path_local = path+'/'+model_name+'/'+name_model_all+'.txt'
          #print(path_local)
          models[name_model_all] = KeyedVectors.load_word2vec_format(path_local, binary=False)
        else: 
          pass

  return models
  
  
  #diretório de modelos treinados
path = '/path/to/modelos'

vec_dim = [300,600]
epochs = [10]
nn_types = [0,1]

name_model_w2v = "word2vec"
name_model_ft = "fasttext"

modelos_fasttext_treinados = load_models(path,name_model_ft, vec_dim,epochs,nn_types)
modelos_word2vec_treinados = load_models(path,name_model_w2v, vec_dim,epochs,nn_types)
