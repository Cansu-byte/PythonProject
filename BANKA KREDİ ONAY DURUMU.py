import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Model
from keras.layers import Input, Dense
from keras import regularizers
from sklearn.linear_model import LogisticRegression

# Veriyi yükleme
data = pd.read_csv('C:/Users/cansu/OneDrive/Masaüstü/bankloan.csv')  # Kendi dosya yolunuzu buraya ekleyin

# Veriyi hazırlama
X = data.drop(columns=["ID", "ZIP.Code", "Personal.Loan"])  # ID ve ZIP kodunu modelden çıkarıyoruz
y = data["Personal.Loan"]  # Hedef değişken

# Eğitim ve test setlerini oluşturma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Verileri ölçeklendirme
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Denoising Autoencoder modelini oluşturma
input_dim = X_train_scaled.shape[1]
input_layer = Input(shape=(input_dim,))
encoded = Dense(8, activation='relu', activity_regularizer=regularizers.l2(0.01))(input_layer)
encoded = Dense(4, activation='relu')(encoded)
decoded = Dense(8, activation='relu')(encoded)
decoded = Dense(input_dim, activation='sigmoid')(decoded)

# Modeli tanımlama
autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Modeli eğitme
autoencoder.fit(X_train_scaled, X_train_scaled, epochs=50, batch_size=256, shuffle=True, validation_data=(X_test_scaled, X_test_scaled))

# Encoder ile özellikleri elde etme
encoder = Model(inputs=input_layer, outputs=encoded)
encoded_X_train = encoder.predict(X_train_scaled)
encoded_X_test = encoder.predict(X_test_scaled)

# Kredi tahmini için Lojistik Regresyon modeli oluşturma
lr_model = LogisticRegression()
lr_model.fit(encoded_X_train, y_train)

# Tahmin yapma fonksiyonu: müşteri ID'sine göre kredi alıp almadığını tahmin edecek
def predict_loan_status(customer_id):
    # Müşteri verilerini seçme
    customer_data = data[data["ID"] == customer_id].drop(columns=["ID", "ZIP.Code", "Personal.Loan"])
    
    if customer_data.empty:
        return "Müşteri bulunamadı."
    
    # Veriyi ölçeklendirme
    customer_data_scaled = scaler.transform(customer_data)
    
    # Denoising Autoencoder ile kodlama
    encoded_customer_data = encoder.predict(customer_data_scaled)
    
    # Lojistik Regresyon ile tahmin yapma
    prediction = lr_model.predict(encoded_customer_data)
    return "Kredi Onaylandı" if prediction[0] == 1 else "Kredi Onaylanmadı"

# Program döngüsü: Kullanıcı "çık" yazana kadar devam eder
while True:
    user_input = input("Lütfen müşteri ID'sini girin (Çıkmak için 'çik' yazın): ")
    
    if user_input.lower() == 'çik':
        print("Program sonlandırılıyor...")
        break
    
    try:
        customer_id = int(user_input)
        result = predict_loan_status(customer_id)
        print(f"Müşteri ID {customer_id} için tahmin: {result}")
    except ValueError:
        print("Geçersiz giriş! Lütfen geçerli bir müşteri ID'si girin.")
