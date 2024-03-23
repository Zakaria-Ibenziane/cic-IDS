import pandas as pd 
import pickle

with open('modele.pkl','rb') as fichier:
	modele = pickle.load(fichier)
	
df_test = pd.read_csv(ens33.csv)

df_test = df_test.drop_duplicates(keep="first")
df_test = df_test.dropna(axis=0)

colonnes_selected = [	
						'dst_port','flow_duration','tot_fwd_pkts','tot_bwd_pkts',
						'totlen_fwd_pkts','totlen_bwd_pkts','fwd_pkt_len_max',
						'fwd_pkt_len_min','fwd_pkt_len_mean','fwd_pkt_len_std',
						'bwd_pkt_len_max','bwd_pkt_len_min','bwd_pkt_len_mean',
						'bwd_pkt_len_std','flow_byts_s','flow_pkts_s','flow_iat_mean',
						'flow_iat_std','flow_iat_max','flow_iat_min','fwd_iat_tot',
						'fwd_iat_mean','fwd_iat_std','fwd_iat_max','fwd_iat_min',
						'bwd_iat_tot','bwd_iat_mean','bwd_iat_std','bwd_iat_max',
						'bwd_iat_min','fwd_psh_flags','bwd_psh_flags','fwd_urg_flags',
						'fwd_header_len','bwd_header_len','fwd_pkts_s','bwd_pkts_s',
						'pkt_len_min','pkt_len_max','pkt_len_mean','pkt_len_std',
						'pkt_len_var','fin_flag_cnt','syn_flag_cnt','rst_flag_cnt',
						'psh_flag_cnt','ack_flag_cnt','urg_flag_cnt',
						'ece_flag_cnt','down_up_ratio','pkt_size_avg',
						'fwd_header_len','init_fwd_win_byts','init_bwd_win_byts',
						'active_mean','active_std','active_max','active_min',
						'idle_mean','idle_std','idle_max','idle_min',

							]



df_test = df_test[colonnes_selected]

prediction = modele.predict(df_test)

print(prediction)


# Colonnes qui manquent : 

# 'Avg Fwd Segment Size', 'Avg Bwd Segment Size',

# 'Fwd Avg Bytes/Bulk', 'Fwd Avg Packets/Bulk', 'Fwd Avg Bulk Rate', 'Bwd Avg Bytes/Bulk', 'Bwd Avg Packets/Bulk', 'Bwd Avg Bulk Rate',

# 'Subflow Fwd Packets', 'Subflow Fwd Bytes', 'Subflow Bwd Packets', 'Subflow Bwd Bytes',

# 'act_data_pkt_fwd','min_seg_size_forward', 