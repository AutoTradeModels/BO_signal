import datetime
import pickle
from BO import BinaryOption 

ID = "**********"
token = "*************************"
instrument = "USD_JPY"

model = "model_" + instrument + "_BO_2019.pickle"
with open(model, mode='rb') as fp:
    G3P_High = pickle.load(fp)
    G3P_Low = pickle.load(fp)
T = G3P_High.T

now = datetime.datetime.now()
end = now.replace(second=0, microsecond=0)
start = end - datetime.timedelta(minutes=T)

BO = BinaryOption(ID, token, instrument, T=T)
X = BO.history_data(start, end)

myu_High, sigma_High = G3P_High.predict(X, ID)
myu_Low, sigma_Low = G3P_Low.predict(X, ID)

print('myu_High', myu_High[0], 'sigma_High', sigma_High[0], 
      'myu_Low', myu_Low[0], 'sigma_Low', sigma_Low[0])