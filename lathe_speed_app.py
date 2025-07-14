
import streamlit as st
import math

st.set_page_config(page_title="محاسبه سرعت برش و دوران اسپیندل", layout="centered")

st.title("🧮 محاسبه سرعت برش و دوران اسپیندل دستگاه تراش")
st.markdown("---")

# لیست متریال‌ها
materials = {
    "فولاد ساده": 25,
    "فولاد آلیاژی": 20,
    "آلومینیوم": 180,
    "برنج": 100,
    "چدن": 30,
    "استنلس استیل": 15,
    "پلاستیک سخت": 200,
}

material_name = st.selectbox("📦 انتخاب متریال", list(materials.keys()))
default_V = materials[material_name]

st.markdown(f"🔹 سرعت برش پیشنهادی: **{default_V} m/min** برای {material_name}")

D = st.number_input("📐 قطر قطعه (میلی‌متر)", min_value=1.0, step=0.1)

mode = st.radio("🔄 انتخاب نوع محاسبه:", ["محاسبه تعداد دور (n)", "محاسبه سرعت برش (V)"])

if mode == "محاسبه تعداد دور (n)":
    use_default = st.checkbox(f"استفاده از سرعت برش پیش‌فرض {default_V} m/min", value=True)
    if use_default:
        V = default_V
    else:
        V = st.number_input("🔸 وارد کردن سرعت برش (m/min)", min_value=1.0, step=1.0)

    if D > 0:
        n = (1000 * V) / (math.pi * D)
        st.success(f"✅ تعداد دور اسپیندل: **{n:.1f} دور بر دقیقه (rpm)**")

elif mode == "محاسبه سرعت برش (V)":
    n = st.number_input("🔸 وارد کردن تعداد دور اسپیندل (rpm)", min_value=1.0, step=1.0)

    if D > 0:
        V = (math.pi * D * n) / 1000
        st.success(f"✅ سرعت برش: **{V:.1f} متر بر دقیقه (m/min)**")

st.markdown("---")
st.caption("طراحی شده برای محاسبات تراشکاری دقیق 🎯")
