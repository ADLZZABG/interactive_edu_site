# pages/5_Social_Media.py
import streamlit as st

# تطبيق الهوية البصرية
style_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Almarai:wght@400;700;800&display=swap');
body { background-color: #f4f4f4; font-family: 'Almarai', sans-serif; }
[data-testid="stHeader"] { background-color: transparent; }
[data-testid="stSidebar"] { background-color: #1a233a; color: white; }
[data-testid="stSidebarNav"] li a { color: white; font-family: 'Almarai', sans-serif; }
.stMarkdown h1, h2, h3, h4 { color: #ffd700; font-family: 'Almarai', sans-serif; }
.stMarkdown p, .stMarkdown li, .stMarkdown label { color: white; font-family: 'Almarai', sans-serif; }
</style>
"""
st.markdown(style_css, unsafe_allow_html=True)

st.title("التواجد الرقمي ووسائل التواصل")
st.write("---")

st.write("يسعدني تواصلكم ومتابعتكم لمحتواي الأكاديمي والمهني عبر المنصات التالية:")
st.write("") # مسافة فارغة لترتيب العناصر

# استخدام الأعمدة لعرض الأزرار بشكل متجاور وأنيق
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📺 يوتيوب (YouTube)")
    st.write("أشارك عبر قناتي محتوى مرئي متعلق بالاقتصاد، ريادة الأعمال، والتحليلات المتنوعة.")
    
    # تصميم زر ذهبي ليوتيوب
    youtube_button = """
    <a href="https://www.youtube.com/@thelens49" target="_blank" style="text-decoration: none;">
        <div style="background-color: #ffd700; color: #1a233a; padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; font-family: 'Almarai', sans-serif; transition: 0.3s; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-top: 10px;">
            زيارة قناة The Lens 49 ▶️
        </div>
    </a>
    """
    st.markdown(youtube_button, unsafe_allow_html=True)

with col2:
    st.markdown("### 💼 لينكد إن (LinkedIn)")
    st.write("للتواصل المهني، الاستشارات، ومتابعة أحدث النشاطات والمقالات.")
    
    # تصميم زر كحلي بإطار ذهبي للينكد إن
    linkedin_button = """
    <a href="https://linkedin.com/in/abdulaziz-sabbagh-990854104" target="_blank" style="text-decoration: none;">
        <div style="background-color: #1a233a; color: #ffd700; padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; border: 2px solid #ffd700; font-family: 'Almarai', sans-serif; transition: 0.3s; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-top: 10px;">
            التواصل عبر LinkedIn 🔗
        </div>
    </a>
    """
    st.markdown(linkedin_button, unsafe_allow_html=True)