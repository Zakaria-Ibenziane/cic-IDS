from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler
from sklearn.preprocessing import RobustScaler
import pandas as pd
import pickle
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt # plotting


df1 = pd.read_csv("2024-04-19-12%3A06%3A56.csv")
df1.shape

# Input depuis cicflowmeter :  Colonnes_selected 59 arguments

colonnes_selected = [ 'dst_port','flow_duration','tot_fwd_pkts','tot_bwd_pkts',
						          'totlen_fwd_pkts','totlen_bwd_pkts','fwd_pkt_len_max',
						          'fwd_pkt_len_min','fwd_pkt_len_mean','fwd_pkt_len_std',
						          'bwd_pkt_len_max','bwd_pkt_len_min','bwd_pkt_len_mean',
						          'bwd_pkt_len_std','flow_byts_s','flow_pkts_s','flow_iat_mean',
						          'flow_iat_std','flow_iat_max','flow_iat_min','fwd_iat_tot',
						          'fwd_iat_mean','fwd_iat_std','fwd_iat_max','fwd_iat_min',
						          'bwd_iat_tot','bwd_iat_mean','bwd_iat_std','bwd_iat_max',
						          'bwd_iat_min','fwd_psh_flags',
						          'fwd_urg_flags','fwd_header_len','bwd_header_len','fwd_pkts_s',
						          'bwd_pkts_s','pkt_len_min','pkt_len_max','pkt_len_mean',
						          'pkt_len_std','pkt_len_var','fin_flag_cnt',
						          'rst_flag_cnt','psh_flag_cnt','ack_flag_cnt','urg_flag_cnt',
						          'ece_flag_cnt','down_up_ratio','pkt_size_avg',
						          'init_fwd_win_byts','init_bwd_win_byts',
						          'active_mean','active_std','active_max','active_min',
						          'idle_mean','idle_std','idle_max','idle_min'
						         ]

df1 = df1[colonnes_selected]

df1.replace([np.inf,-np.inf],np.nan,inplace=True)
print(df1.isna().any(axis=1).sum(),"rows dropped")

df1.dropna(inplace=True)

# scaling the dataset / redimensionnement

ro_scaler = RobustScaler()
x_scaled = ro_scaler.fit_transform(df1)

# échelonnage des données dans une plage donnée, par défaut entre 0 et 1
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_scaled)

# Load the pre-trained model pkl
RF = pickle.load(open('Random_Forest.pkl', 'rb'))
# Load the pre-trained model pkl
LR = pickle.load(open('Logistic_Regression.pkl', 'rb'))
# Load the pre-trained model pkl
NB = pickle.load(open('Naive_Baye.pkl', 'rb'))

models = []
models.append(('RandomForestClassifier', RF))
models.append(('LogisticRegression', LR))
models.append(('Naive Baye Classifier', NB))
# models.append(('Decision Tree Classifier', DTC))
# models.append(('KNeighborsClassifier', KNN))

for i, v in models:
  print()
  print('============================== {} Model Prediction =============================='.format(i))
  # Apply the pre-trained model  to the cleaned test dataset
  prediction = v.predict(x_scaled)
  print(prediction)
  # # Print out the resulting predictions
  # print(prediction)

  # # Apply the pre-trained Random Forest model  to the cleaned test dataset
  # prediction = RF.predict(x_scaled)

  # # Print out the resulting predictions
  # print(prediction)