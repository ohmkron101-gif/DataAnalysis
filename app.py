import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('sustainable_waste_management_dataset_2024.csv')

st.write(df)






df = pd.read_csv("sustainable_waste_management_dataset_2024.csv")

st.title("ปริมาณขยะรวมแยกตามพื้นที่ (ปี 2024)")


area_summary = df.groupby("area", as_index=False)["waste_kg"].sum()


st.vega_lite_chart(
    area_summary,
    {
        "mark": {
            "type": "bar",
            "cornerRadiusTopLeft": 6,
            "cornerRadiusTopRight": 6
        },
        "encoding": {
            "x": {
                "field": "area",
                "type": "nominal",
                "title": "พื้นที่",
                "axis": {"labelAngle": -30}
            },
            "y": {
                "field": "waste_kg",
                "type": "quantitative",
                "<h1>title": "ปริมาณขยะรวม (กิโลกรัม)</h1>"
            },
            "color": {
                "field": "area",
                "type": "nominal",
                "legend": None
            },
            "tooltip": [
                {"field": "area", "type": "nominal", "title": "พื้นที่"},
                {"field": "waste_kg", "type": "quantitative", "title": "ขยะ (กก.)"}
            ]
        }
    },
    use_container_width=True
)



st.title("Predicted vs. Actual Dollar Price")


Y_test = np.array([
    10000, 12000, 14000, 15000, 18000, 20000, 22000,
    24000, 26000, 30000, 32000, 34000, 36000, 40000
])

Y_pred = np.array([
    10500, 11800, 13800, 14500, 18500, 19500, 22500,
    24500, 25500, 26500, 35000, 34000, 35500, 36000
])


min_val = min(Y_test.min(), Y_pred.min())
max_val = max(Y_test.max(), Y_pred.max())


fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(Y_test, Y_pred, alpha=0.7)

ax.plot(
    [min_val, max_val],
    [min_val, max_val],
    '--',
    color='red',
    linewidth=2,
    label='Perfect Prediction Line'
)

ax.set_xlabel("Actual Dollar Price (Y_test)")
ax.set_ylabel("Predicted Dollar Price (Y_pred)")
ax.set_title("Predicted vs. Actual Dollar Price")

ax.legend()
ax.grid(True)

st.pyplot(fig)




