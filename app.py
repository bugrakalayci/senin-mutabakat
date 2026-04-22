import streamlit as st
import pandas as pd
import plotly.express as px

# Sayfa ayarları
st.set_page_config(page_title="Cari Mutabakat Dashboard", layout="wide")

st.title("📊 Cari Hesap Mutabakat ve Karşılaştırma")

# Dosya Yükleme Alanı
st.sidebar.header("Dosyaları Yükle")
file1 = st.sidebar.file_uploader("Birinci Cari PDF (Senin Kayıtların)", type=['pdf'])
file2 = st.sidebar.file_uploader("İkinci Cari PDF (Karşı Taraf)", type=['pdf'])

# Analiz Özeti (Örnek Verilerle)
st.subheader("📌 Genel Durum Özeti")
c1, c2, c3 = st.columns(3)

# Buraya senin PDF verilerini manuel bir tablo olarak ekleyelim (Şimdilik Demo)
data = {
    'Ay': ['Ocak', 'Şubat', 'Mart', 'Nisan'],
    'Senin Borç': [53854, 41470, 14619, 39947],
    'Karşı Borç': [53854, 41470, 14619, 39947],
    'Durum': ['✅ Tamam', '⚠️ Tarih Hatası', '⚠️ Tarih Hatası', '⚠️ Tarih Hatası']
}
df = pd.DataFrame(data)

with c1:
    st.metric("Toplam Borç", "149.890,80 TL")
with c2:
    st.metric("Toplam Alacak", "138.300,00 TL")
with c3:
    st.metric("Net Bakiye", "52.447,96 TL")

st.divider()

# Grafik ve Tablo
col_left, col_right = st.columns([2, 1])

with col_left:
    st.write("### Aylık Hareket Karşılaştırması")
    fig = px.bar(df, x='Ay', y=['Senin Borç', 'Karşı Borç'], barmode='group')
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.write("### Hata Bildirimleri")
    st.table(df[['Ay', 'Durum']])

st.warning("💡 **Öneri:** Şubat, Mart ve Nisan aylarındaki KDV kayıt tarihlerini ana fatura tarihleriyle aynı güne çekmeniz mutabakatı kolaylaştıracaktır.")