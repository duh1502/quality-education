{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11018f36",
   "metadata": {},
   "outputs": [],
   "source": [
    "targets\n",
    "Selecionar as colunas que serão utilizadas no treinamento do modelo.\n",
    "\n",
    "Após vários testes, a seleção é pelos melhores resultados obtidos.\n",
    "\n",
    "# ==============================================================================\n",
    "colunas_adicionais = [  \"NO_IDADE_GROUP\",  \"VR_IDHM\", \"VR_IFDM\", 'CO_REGIAO_RESIDENCIA',\n",
    "                      \"IN_ATEND_ESPECIAL\", \"IN_ATEND_ESPECIFICO\",  \"IN_RECURSO_ESPECIAL\",\n",
    "                      ]\n",
    "\n",
    "#\"SG_UF_RESIDENCIA\"\n",
    "#colunas_dados_participante_train = ['TP_COR_RACA','TP_ST_CONCLUSAO','TP_ANO_CONCLUIU','TP_SEXO','TP_ESCOLA','TP_ESTADO_CIVIL','IN_TREINEIRO','CO_MUNICIPIO_RESIDENCIA','NU_IDADE']\n",
    "colunas_dados_participante_train = [\"TP_ESCOLA\",\t\"TP_ANO_CONCLUIU\",\t\"TP_ST_CONCLUSAO\",\t\"IN_TREINEIRO\",\t\"TP_SEXO\", \"TP_COR_RACA\" ]\n",
    "\n",
    "colunas_prova_objetiva_train = [\"TP_LINGUA\"]\n",
    "\n",
    "colunas_socio_economico = ['Q001','Q002','Q003','Q004',\t'Q006', 'Q008',\t'Q024',\t'Q025']\n",
    "#colunas_socio_economico = ['Q001','Q002','Q003','Q004','Q005','Q006','Q007','Q008','Q009','Q010','Q011','Q012','Q013',\n",
    "#                           'Q014','Q015','Q016','Q017','Q018','Q019','Q020','Q021','Q022','Q023','Q024','Q025']\n",
    "#Separar dados de treino e teste, além de features para treinamento e objetivo/target\n",
    "X = df_train[colunas_dados_participante_train + colunas_prova_objetiva_train + colunas_adicionais + colunas_socio_economico]\n",
    "y = df_train[targets]\n",
    "\n",
    "# Separation of data into a training set and a test set\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.10, test_size=0.01, random_state=18, stratify=X['CO_REGIAO_RESIDENCIA'])\n",
    "X_train.shape\n",
    "X.head()\n",
    "# Definir colunas categóricas, as quais serão convertidas para OneHotEncoding no pipeline do modelo\n",
    "# ==============================================================================\n",
    "colunas_categoricas = ['TP_ESCOLA',\t'TP_ANO_CONCLUIU',\t'TP_ST_CONCLUSAO',  'TP_COR_RACA', 'NO_IDADE_GROUP','CO_REGIAO_RESIDENCIA']\n",
    "colunas_categoricas = colunas_categoricas + colunas_socio_economico"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
