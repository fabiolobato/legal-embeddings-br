### Embeddings Jurídico: Representações Orientadas à Linguagem Jurídica Brasileira
***
  O processamento automático de textos jurídicos dispostos em linguagem natural proporciona o desenvolvimento de diversas aplicações para o setor, como a classificação de processos por assunto, sumarização de documentos, tradução para linguagem cidadã etc. Nesse sentido, o judiciário brasileiro lançou o programa Justiça 4.0, buscando soluções que ofereçam celeridade nas atividades processuais. Convém pontuar que a linguagem técnica predomina nesse domínio de aplicação, o que adiciona desafios para modelagem dos dados, exigindo modelos especializados para o segmento. Frente ao exposto, esse trabalho tem como objetivo a construção de modelos embeddings orientados ao âmbito jurídico visando alimentar aplicações na área. Para isso, foram extraídos aproximadamente 500.000 documentos de instituições de justiça do Brasil das mais variadas esferas (civil, criminal, trabalhista etc). Os modelos foram avaliados por meio da classificação de petições iniciais e os resultados mostraram-se competitivos quando comparados a modelos generalistas da língua portuguesa. Tais  resultados mostram que modelos treinados com documentos jurídicos compreendem melhor as especificidades da linguagem do segmento e têm o potencial de fomentar novas aplicações para o setor.

### Instruções de uso
***
1. Carregando os modelos `word2vec` e `fastText` treinados. Consulte as dependências (listadas abaixo) para a execução do arquivo `load_models.py`.

```
python3 load_models.py 
```

2. Dependências: 

* `gensim`
* `numpy`
* `pandas`
* `logging`
* `collection`
* `more-itertools`

3. Cite este trabalho
```
@INPROCEEDINGS{230786,
    AUTHOR="Fabrício do Carmo and Ferdinando Serejo and Antonio Fernando Lavareda Jacob Junior and Ewaldo Santana and Fabio Lobato",
    TITLE="Embeddings Jurídico: Representações Orientadas à Linguagem Jurídica Brasileira",
    BOOKTITLE="CSBC 2023 - WCGE 2023 ()",
    ADDRESS="",
    DAYS="23-28",
    MONTH="jul",
    YEAR="2023",
    URL="http://XXXXX/230786-23.pdf"
}
```
