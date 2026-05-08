# main_app.py
import streamlit as st

# إعدادات الصفحة العامة (ستطبق على جميع الصفحات)
st.set_page_config(
    page_title="الباحث الاقتصادي",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# دمج الهوية البصرية عبر CSS (لتطبيقها على جميع الصفحات)
# ملاحظة: سأقوم بدمج هذا الجزء في كل ملف لضمان تطبيقه
style_css = """
<style>
/* CSS مخصص لتطبيق الألوان والخطوط */
@import url('https://fonts.googleapis.com/css2?family=Almarai:wght@400;700;800&display=swap');

body {
    background-color: #f4f4f4; /* خلفية رمادية فاتحة للمحتوى */
    font-family: 'Almarai', sans-serif;
}

[data-testid="stHeader"] {
    background-color: transparent;
}

[data-testid="stSidebar"] {
    background-color: #1a233a; /* كحلي داكن - مستوحى من سترة الشخص */
    color: white;
}

[data-testid="stSidebarNav"] li a {
    color: white;
    font-family: 'Almarai', sans-serif;
}

/* تخصيص محتوى الصفحة الرئيسي */
.stMarkdown h1, h2, h3 {
    color: #ffd700; /* ذهبي - مستوحى من النص الذهبي */
    font-family: 'Almarai', sans-serif;
}

.stMarkdown p, .stMarkdown li, .stMarkdown label, .stMetricValue, .stMetricLabel {
    color: white; /* أبيض - للنصوص العامة لتبرز على الخلفية */
    font-family: 'Almarai', sans-serif;
}

.stSlider label, .stNumberInput label {
    color: white; /* أبيض */
}

/* تخصيص مؤشر الألوان لمظهر أكثر احترافية */
.element-container [data-testid="stMetricValue"] {
    color: #ffd700; /* ذهبي لقيم المؤشرات */
}
</style>
"""

st.markdown(style_css, unsafe_allow_html=True)

st.write("## مرحبًا بكم في منصتنا التعليمية التفاعلية")
st.write("لقد بدأت رحلة بناء موقعك! استخدم الشريط الجانبي للتنقل بين الأقسام المختلفة.")
st.write("سأقوم الآن بإنشاء كود كل صفحة، وسأقوم بدمج كود CSS المخصص داخل كل ملف لضمان تطبيقه.")