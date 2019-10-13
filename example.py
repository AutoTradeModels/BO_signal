import datetime
import pickle
from BO import BinaryOption 
from info import get_info

No, ID, PW, token, price, driver, confidence = get_info()
instrument = "USD_JPY"
BO = BinaryOption(ID, token, instrument)

now = datetime.datetime.now()
end = now.replace(second=0, microsecond=0)
start = end - datetime.timedelta(minutes=100)
X = BO.history_data(start, end)

model = "model_" + instrument + "_BO_2019.pickle"
with open(model, mode='rb') as fp:
    G3P_High = pickle.load(fp)
    G3P_Low = pickle.load(fp)
myu_High, sigma_High = G3P_High.predict(X, ID)
myu_Low, sigma_Low = G3P_Low.predict(X, ID)

print('myu_High', myu_High[0], 'sigma_High', sigma_High[0], 
      'myu_Low', myu_Low[0], 'sigma_Low', sigma_Low[0])