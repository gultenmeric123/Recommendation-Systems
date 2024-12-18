import streamlit as st
import pandas as pd
from PIL import Image
from funcs import *

def main():
    st.set_page_config(layout="wide", initial_sidebar_state='expanded')

    sidebar_header = '''Bu demo, verilen bir giyim ürününe benzer öğeleri bulmak ve öğe önerileri yapmak için bir öneri sistemini göstermektedir:'''
    page_options = ["Benzer öğeleri bul"]

    st.sidebar.info(sidebar_header)
    page_selection = st.sidebar.radio("Dene", page_options)
    articles_df = pd.read_csv('articles.csv')

    # Sadece "Tanımlayıcı özelliklere dayalı benzer öğeler" modeli kullanılıyor.
    models = ['Tanımlayıcı özelliklere dayalı benzer öğeler']
    model_descs = ['Verisetindeki tanımlayıcı özelliklerin one-hot encoding yöntemiyle hesaplanıyor.']

    if page_selection == "Benzer öğeleri bul":
        articles_rcmnds = pd.read_csv('results/articles_rcmnds.csv')
        articles = articles_rcmnds.article_id.unique()
        selected_article = st.sidebar.selectbox('Bir ürün seçin:', articles)

        if selected_article:
            article_data = articles_rcmnds[articles_rcmnds.article_id == selected_article]
            article_desc = articles_df[articles_df.article_id == selected_article].detail_desc.iloc[0]

            # Gerekli değişkenleri get_rcmnds fonksiyonlarından alıyoruz.
            feature_rcmnds = get_rcmnds(article_data)
            scores = get_rcmnds_scores(article_data)
            features = get_rcmnds_features(articles_df, feature_rcmnds)
            images = get_rcmnds_images(feature_rcmnds)
            # detail_descs = get_rcmnds_desc(articles_df, feature_rcmnds) # Artık kullanılmıyor

            st.sidebar.image(get_item_image(str(selected_article), width=200, height=300))
            st.sidebar.write('Ürün açıklaması')
            st.sidebar.caption(article_desc)

            with st.container():
                for i, model, model_desc in zip(range(1), models, model_descs):
                    container = st.expander(model, expanded=True)
                    with container:
                        cols = st.columns(7)
                        cols[0].write('###### Benzerlik Skoru')
                        cols[0].caption(model_desc)

                        # Önerilen ürün sayısı kadar döngü - features.itertuples() kullanıyoruz
                        for j, (img, score, row) in enumerate(zip(images, scores, features.itertuples())): # detail_desc kaldırıldı
                            if j + 1 < len(cols):  # İlk sütun başlık için ayrıldığı için j+1 kullanıyoruz
                                with cols[j + 1]:
                                    st.caption('{}'.format(score))
                                    st.image(img, use_container_width=True)
                                    # Ürün özelliklerini ve açıklamalarını doğru şekilde alıyoruz.
                                    st.caption(f"Ürün Tipi: {row.product_type_name}")
                                    st.caption(f"Renk: {row.colour_group_name}")
                                    st.caption(f"Departman: {row.department_name}")
                                    # st.caption(f"Açıklama: {detail_desc}") # Açıklama kısmı kaldırıldı

if __name__ == '__main__':
    main()