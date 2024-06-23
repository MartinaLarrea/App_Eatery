import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import pickle


# from pyspark.sql.functions import col, explode
# from pyspark import SparkContext
# from pyspark.sql import SparkSession
# from scipy.sparse import csr_matrix
# from implicit.als import AlternatingLeastSquares       
# from pyspark import SparkConf
# implicit==0.7.0
# pyspark>=3.0.0


#1. Import
data = pd.read_csv("data\df_limpio.csv")


#2. Titulo de pagina
st.header("Sistema de recomendación de restaurantes")

