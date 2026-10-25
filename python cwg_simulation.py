# cwg_simulation.py
import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)

plt.rcParams["font.family"] = "Arial"
plt.rcParams["figure.figsize"] = (14, 7)

hours = np.arange(0, 24, 1)

renewable = np.array([8,7,6,5,6,9,14,22,28,30,32,33,31,29,26,20,14,9,6,5,5,4,4,6])
price = np.array([0.32,0.30,0.28,0.27,0.29,0.35,0.42,0.48,0.46,0.40,0.36,0.33,0.31,0.34,0.38,0.43,0.47,0.49,0.45,0.40,0.36,0.33,0.31,0.30])

baseline_compute = np.array([12,0,15,0,0,18,24,0,0,22,0,0,16,0,0,20,0,0,14,0,0,10,0,0])
cwg_compute = np.array([12,15,10,14,12,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

battery_soc = np.array([30,40,50,62,74,85,92,88,82,76,70,64,58,52,46,40,36,32,29,26,24,22,21,20])


fig, ax1 = plt.subplots()

color_green = "#27ae60"
color_price = "#e74c3c"
color_base = "#95a5a6"
color_cwg = "#2980b9"

ax1.set_xlabel("Hour of Day (0-24)")
ax1.set_ylabel("Power / Load (kW)", color="#333333")
ax1.plot(hours, renewable, color=color_green, label="Renewable Power", linewidth=2.5)
ax1.plot(hours, baseline_compute, color=color_base, linestyle="--", label="Baseline Compute", linewidth=2)
ax1.plot(hours, cwg_compute, color=color_cwg, label="CWG Scheduled Compute", linewidth=2.5)
ax1.tick_params(axis='y')

ax2 = ax1.twinx()
ax2.set_ylabel("Electricity Price ($/kWh)", color=color_price)
ax2.plot(hours, price, color=color_price, linestyle=":", label="Grid Price", linewidth=2)
ax2.tick_params(axis='y', labelcolor=color_price)

ax3 = ax1.twinx()
ax3.spines.right.set_position(("axes", 1.18))
ax3.set_ylabel("Battery SOC (%)", color="#f39c12")
ax3.plot(hours, battery_soc, color="#f39c12", linestyle="-.", label="Battery SOC", linewidth=2)
ax3.tick_params(axis='y', labelcolor="#f39c12")


lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax1.legend(lines1+lines2+lines3, labels1+labels2+labels3, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=5)

plt.title("Compute-When-Green: 24-hour Scheduling Simulation", pad=20, fontsize=14)
plt.grid(alpha=0.25)
plt.xlim(0,23)
plt.xticks(np.arange(0,24,2))
plt.tight_layout()

plt.savefig("figures/simulation_plot.png", dpi=300, bbox_inches="tight")
plt.show()


baseline_cost = np.sum(baseline_compute * price / 100)
cwg_cost = np.sum(cwg_compute * price /100)

baseline_carbon = np.sum(baseline_compute * price)
cwg_carbon = np.sum(cwg_compute * price)

print("===== Simulation Result =====")
print(f"Baseline total cost: {baseline_cost:.2f}")
print(f"CWG total cost:      {cwg_cost:.2f}")
print(f"Cost reduction:      {(1 - cwg_cost/baseline_cost)*100:.1f} %")
print(f"Carbon reduction:    {(1 - cwg_carbon/baseline_carbon)*100:.1f} %")
