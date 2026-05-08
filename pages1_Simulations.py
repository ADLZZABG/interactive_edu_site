# pages/1_Simulations.py
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

st.title("نماذج المحاكاة التعليمية 📊")
st.write("---")

st.markdown("## محاكاة توازن سوق السلعة")
st.write("في هذا النموذج، يمكنك محاكاة توازن سوق لسلعة معينة عن طريق ضبط معلمات الطلب والعرض. ستلاحظ كيف يؤثر التغير في السعر على الكميات المطلوبة والموردة، وكيف يتم تحديد سعر التوازن.")

# قسم المدخلات (الشريط الجانبي)
st.sidebar.header("إعدادات المحاكاة")

st.sidebar.markdown("### معلمات الطلب (Demand)")
initial_demand = st.sidebar.slider("الطلب الأولي (عند سعر 10)", 50, 500, 100)
price_elasticity_demand = st.sidebar.slider("مرونة الطلب السعرية", 0.5, 2.0, 1.0)

st.sidebar.markdown("### معلمات العرض (Supply)")
initial_supply = st.sidebar.slider("العرض الأولي (عند سعر 10)", 50, 500, 100)
price_elasticity_supply = st.sidebar.slider("مرونة العرض السعرية", 0.1, 1.0, 0.5)

st.sidebar.markdown("### التحكم في المحاكاة")
time_periods = st.sidebar.slider("عدد الفترات الزمنية", 10, 200, 100)
# عامل تعديل السعر (مدى سرعة تعديل السعر بناءً على فائض الطلب)
price_adjustment_factor = 0.1 

# منطق المحاكاة الاقتصادية
# T = 100 periods
T = time_periods
# أسعار التوازن المتوقعة (بناءً على التوازن الرياضي)
# D = InitialDemand - (Price - 10) * ElasticityDemand
# S = InitialSupply + (Price - 10) * ElasticitySupply
# Equate D = S, and solve for P
# InitialDemand - P*ElasticityDemand + 10*ElasticityDemand = InitialSupply + P*ElasticitySupply - 10*ElasticitySupply
# P*(ElasticitySupply + ElasticityDemand) = InitialDemand - InitialSupply + 10*(ElasticitySupply + ElasticityDemand)
equilibrium_price = (initial_demand - initial_supply) / (price_elasticity_supply + price_elasticity_demand) + 10
# equilibrium_quantity can be derived from P_eq
# equilibrium_quantity = initial_demand - (equilibrium_price - 10) * price_elasticity_demand

# Simulation steps: start with an initial price (e.g., 10) and update based on excess demand
current_price = 10.0
simulation_data = []

for t in range(T):
    # Calculate demand and supply at current price
    demand = max(0, initial_demand - (current_price - 10) * price_elasticity_demand)
    supply = max(0, initial_supply + (current_price - 10) * price_elasticity_supply)
    
    # Calculate excess demand
    excess_demand = demand - supply
    
    # Update price based on excess demand (more excess demand = higher price)
    new_price = current_price + price_adjustment_factor * excess_demand
    
    simulation_data.append({
        'تاريخ/فترة': t + 1,
        'السعر الحالي ($)': round(current_price, 2),
        'الكمية المطلوبة': round(demand, 1),
        'الكمية الموردة': round(supply, 1),
        'فائض الطلب': round(excess_demand, 1)
    })
    
    current_price = new_price

# Convert results to DataFrame
df_simulation = pd.DataFrame(simulation_data)

# قسم عرض النتائج
col1, col2 = st.columns(2)

with col1:
    st.markdown("### المؤشرات الرئيسية للحظة الحالية (T=100)")
    # استخدام القيم من آخر فترة في المحاكاة
    last_data = simulation_data[-1]
    # metric functions can display changes, e.g., current price vs prev price
    price_change = last_data['السعر الحالي ($)'] - equilibrium_price
    price_diff_percentage = (price_change / equilibrium_price) * 100 if equilibrium_price > 0 else 0
    
    # Calculate if market is in balance, excess demand, or excess supply
    market_state = "في توازن" if abs(last_data['فائض الطلب']) < 0.1 else ("فائض عرض" if last_data['فائض الطلب'] < 0 else "فائض طلب")
    market_state_delta_color = "green" if market_state == "في توازن" else ("inverse" if market_state == "فائض عرض" else "normal") # normal = red
    
    st.metric(
        label="سعر السوق الحالي ($)",
        value=f"{last_data['السعر الحالي ($)']}$",
        delta=f"{round(price_change, 2)}$ ({round(price_diff_percentage, 1)}%)",
        delta_color="off" # لا تستخدم ألوان تيسلا/ديبسيك للحفاظ على الهوية البصرية الكحلية والذهبية
    )
    
    st.metric(
        label="الكمية المتداولة حالياً",
        value=f"{last_data['الكمية المطلوبة']} وحدة",
        delta=f"الطلب: {last_data['الكمية المطلوبة']} | العرض: {last_data['الكمية الموردة']}",
        delta_color="off"
    )
    
    st.metric(
        label="حالة السوق (T=100)",
        value=f"{market_state}",
        delta=f"فائض الطلب: {last_data['فائض الطلب']}",
        delta_color=market_state_delta_color # تلوين حالة السوق للحفاظ على الانتباه، دون استخدام الرموز الأخرى
    )

with col2:
    st.markdown("### نتائج توازن السوق الرياضية")
    if equilibrium_price > 0:
        eq_quantity = initial_demand - (equilibrium_price - 10) * price_elasticity_demand
        st.write(f"سعر التوازن الرياضي: **{round(equilibrium_price, 2)}$**")
        st.write(f"الكمية المتوازنة الرياضية: **{round(eq_quantity, 1)} وحدة**")
        st.write("هذه هي القيم التي سيتجه إليها السوق بمرور الوقت إذا لم يتغير شيء.")
    else:
        st.write("لا يوجد سعر توازن إيجابي في هذه الظروف.")

st.markdown("---")
st.markdown("### الرسوم البيانية التفاعلية")

# الرسم البياني الأول: السعر والكمية بمرور الوقت
st.markdown("#### تغير السعر والكمية عبر الزمن")
col_graph1, col_graph2 = st.columns(2)

with col_graph1:
    fig_price, ax_price = plt.subplots(figsize=(8, 4))
    ax_price.plot(df_simulation['تاريخ/فترة'], df_simulation['السعر الحالي ($)'], label='السعر السوقي', color='#ffd700', linewidth=2.5) # ذهبي
    ax_price.axhline(equilibrium_price, color='#ffd700', linestyle='--', label='سعر التوازن', alpha=0.5)
    ax_price.set_title('تغير سعر السلعة بمرور الوقت', color='#ffd700')
    ax_price.set_xlabel('الفترة الزمنية', color='white')
    ax_price.set_ylabel('السعر ($)', color='white')
    # تخصيص ألوان المحاور للحفاظ على الهوية الكحلية والذهبية
    ax_price.tick_params(axis='x', colors='white')
    ax_price.tick_params(axis='y', colors='white')
    ax_price.grid(axis='y', linestyle='--', alpha=0.3)
    ax_price.legend()
    # fig_price.patch.set_facecolor('#1a233a') # خلفية كحلية للشكل بالكامل
    # ax_price.set_facecolor('#1a233a') # خلفية كحلية للمحور
    st.pyplot(fig_price)

with col_graph2:
    fig_quantity, ax_quantity = plt.subplots(figsize=(8, 4))
    ax_quantity.plot(df_simulation['تاريخ/فترة'], df_simulation['الكمية المطلوبة'], label='الكمية المطلوبة', color='#80c0ff', linewidth=2.5) # أزرق فاتح للحفاظ على الهوية
    ax_quantity.plot(df_simulation['تاريخ/فترة'], df_simulation['الكمية الموردة'], label='الكمية الموردة', color='#a0ffa0', linewidth=2.5) # أخضر فاتح للحفاظ على الهوية
    ax_quantity.set_title('تغير الكميات المطلوبة والموردة عبر الزمن', color='#ffd700')
    ax_quantity.set_xlabel('الفترة الزمنية', color='white')
    ax_quantity.set_ylabel('الكمية', color='white')
    # تخصيص ألوان المحاور
    ax_quantity.tick_params(axis='x', colors='white')
    ax_quantity.tick_params(axis='y', colors='white')
    ax_quantity.grid(axis='y', linestyle='--', alpha=0.3)
    ax_quantity.legend()
    # fig_quantity.patch.set_facecolor('#1a233a')
    # ax_quantity.set_facecolor('#1a233a')
    st.pyplot(fig_quantity)

st.markdown("#### استكشف السوق (جدول البيانات)")
# استعراض جدول البيانات الكامل
st.dataframe(df_simulation.style.format({'السعر الحالي ($)': '{:.2f}$'}))