
import streamlit as st
import math

st.set_page_config(page_title="Lathe Cutting Speed | سرعت برش تراش", layout="centered")

# انتخاب زبان
lang = st.radio("🌐 Select Language | انتخاب زبان", ["فارسی", "English"])

# ترجمه‌ها
texts = {
    "فارسی": {
        "title": "🧮 محاسبه سرعت برش و دوران اسپیندل (بر اساس HSS و Carbide)",
        "material_select": "📦 انتخاب متریال",
        "tool_select": "🛠 انتخاب نوع ابزار (HSS یا Carbide)",
        "default_speed": "🔹 سرعت برش پیشنهادی",
        "diameter": "📐 قطر قطعه (میلی‌متر)",
        "mode_select": "🔄 انتخاب نوع محاسبه:",
        "mode_n": "محاسبه تعداد دور (n)",
        "mode_v": "محاسبه سرعت برش (V)",
        "use_default": "استفاده از سرعت برش پیشنهادی",
        "input_speed": "🔸 وارد کردن سرعت برش (m/min)",
        "result_n": "✅ تعداد دور اسپیندل",
        "input_rpm": "🔸 وارد کردن تعداد دور اسپیندل (rpm)",
        "result_v": "✅ سرعت برش",
        "footer": "طراحی‌شده برای سرعت‌های اختصاصی برش 🎯"
    },
    "English": {
        "title": "🧮 Lathe Cutting Speed & RPM Calculator (Custom HSS/Carbide Speeds)",
        "material_select": "📦 Select Material",
        "tool_select": "🛠 Select Tool Type (HSS or Carbide)",
        "default_speed": "🔹 Suggested Cutting Speed",
        "diameter": "📐 Workpiece Diameter (mm)",
        "mode_select": "🔄 Choose Calculation Mode:",
        "mode_n": "Calculate Spindle RPM (n)",
        "mode_v": "Calculate Cutting Speed (V)",
        "use_default": "Use suggested cutting speed",
        "input_speed": "🔸 Enter custom cutting speed (m/min)",
        "result_n": "✅ Spindle Speed",
        "input_rpm": "🔸 Enter spindle RPM",
        "result_v": "✅ Cutting Speed",
        "footer": "Customized for your exact cutting speeds 🎯"
    }
}

txt = texts[lang]

st.title(txt["title"])
st.markdown("---")

# سرعت‌های داده‌شده توسط کاربر
custom_speeds = {
    "فولاد کربنی | Mild Steel": {"HSS": 20, "Carbide": 25},
    "فولاد آلیاژی سخت | Alloy Steel": {"HSS": 15, "Carbide": 20},
    "آلومینیوم | Aluminum": {"HSS": 100, "Carbide": 120},
    "برنج | Brass": {"HSS": 80, "Carbide": 90},
    "چدن خاکستری | Cast Iron": {"HSS": 20, "Carbide": 25},
    "استنلس استیل | Stainless Steel": {"HSS": 10, "Carbide": 15},
    "پلاستیک سخت | Hard Plastic": {"HSS": 150, "Carbide": 150}
}

material = st.selectbox(txt["material_select"], list(custom_speeds.keys()))
tool = st.radio(txt["tool_select"], ["HSS", "Carbide"])

default_V = custom_speeds[material][tool]
st.markdown(f"{txt['default_speed']}: **{default_V} m/min**")

D = st.number_input(txt["diameter"], min_value=1.0, step=0.1)

mode = st.radio(txt["mode_select"], [txt["mode_n"], txt["mode_v"]])

if mode == txt["mode_n"]:
    use_default = st.checkbox(f"{txt['use_default']} ({default_V} m/min)", value=True)
    if use_default:
        V = default_V
    else:
        V = st.number_input(txt["input_speed"], min_value=1.0, step=1.0)
    if D > 0:
        n = (1000 * V) / (math.pi * D)
        st.success(f"{txt['result_n']}: **{n:.1f} rpm**")

elif mode == txt["mode_v"]:
    n = st.number_input(txt["input_rpm"], min_value=1.0, step=1.0)
    if D > 0:
        V = (math.pi * D * n) / 1000
        st.success(f"{txt['result_v']}: **{V:.1f} m/min**")

st.markdown("---")
st.caption(txt["footer"])
