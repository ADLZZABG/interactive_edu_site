# pages/0_Homepage.py
import streamlit as st

# تطبيق الهوية البصرية (يجب إضافته لكل صفحة)
style_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Almarai:wght@400;700;800&display=swap');
body { background-color: #f4f4f4; font-family: 'Almarai', sans-serif; }
[data-testid="stHeader"] { background-color: transparent; }
[data-testid="stSidebar"] { background-color: #1a233a; color: white; }
[data-testid="stSidebarNav"] li a { color: white; font-family: 'Almarai', sans-serif; }
.stMarkdown h1, h2, h3 { color: #ffd700; font-family: 'Almarai', sans-serif; }
.stMarkdown p, .stMarkdown li, .stMarkdown label, .stMetricValue, .stMetricLabel { color: white; font-family: 'Almarai', sans-serif; }
.stSlider label, .stNumberInput label { color: white; }
.element-container [data-testid="stMetricValue"] { color: #ffd700; }
</style>
"""
st.markdown(style_css, unsafe_allow_html=True)

st.title("الخبير التقني ورائد الأعمال: [اسمك هنا]")
st.write("---")

st.markdown("## مرحباً بكم في منصتنا التعليمية التفاعلية")
st.write("نحن ملتزمون بتقديم المعرفة من خلال المحاكاة المبتكرة والتدريب العملي، مستلهمين الابتكار من عمالقة التكنولوجيا مثل يوتيوب، أمازون، تيسلا، وغيرهم.")
st.write("استكشف أقسامنا المختلفة لتطوير مهاراتك في ريادة الأعمال والتكنولوجيا.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### نماذج المحاكاة التعليمية")
    st.write("جرب المحاكاة التفاعلية وطبق النظريات اقتصادية.")
    st.button("اذهب للمحاكاة") # لنقم بإنشاء رابط لاحقاً

with col2:
    st.markdown("### الدورات التدريبية")
    st.write("تعلم من خبرائنا وطور مهاراتك.")
    st.button("اذهب للدورات") # لنقم بإنشاء رابط لاحقاً

with col3:
    st.markdown("### الأبحاث والمقالات")
    st.write("اقرأ أحدث الأبحاث والمقالات.")
    st.button("اذهب للأبحاث") # لنقم بإنشاء رابط لاحقاً