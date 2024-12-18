# Giyim Ürünleri için Öneri Sistemi

Bu proje, H&M giyim ürünleri için bir öneri sistemi sunmaktadır. Kullanıcıların seçtikleri bir ürüne benzer ürünleri bulmalarına yardımcı olur. Öneriler, ürünlerin tanımlayıcı özelliklerine (ürün tipi, renk, departman, vb.) dayalı olarak hesaplanmaktadır.

## Gereksinimler

*   Python 3.7+
*   [Streamlit](https://streamlit.io/)
*   [Pandas](https://pandas.pydata.org/)
*   [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)
*   [NumPy](https://numpy.org/)
*   [ast](https://docs.python.org/3/library/ast.html)

Gerekli kütüphaneleri yüklemek için:

```bash
pip install -r requirements.txt

Kullanılan dosyalar:

articles.csv: Ürünlerle ilgili detaylı bilgileri ( article_id, product_type_name, product_group_name, graphical_appearance_name, colour_group_name, perceived_colour_value_name, perceived_colour_master_name, department_name, index_name, index_group_name, section_name, garment_group_name, detail_desc ) içeren veri dosyası.

results/articles_rcmnds.csv: Her bir ürün için, tanımlayıcı özelliklerine göre hesaplanmış benzer ürünlerin listesini ve benzerlik skorlarını içeren dosya. Bu dosyanın, feature_rcmnds ve feature_scores sütunlarını içerdiğinden emin olun.

results/images/: Ürün görsellerini içeren klasör. Görsellerin dosya adları, article_id ile aynı olmalıdır (örneğin, 0108775015.jpg).
