import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# LOAD DATA
# ===============================
CSV_PATH = "phase1_acknowledged_wind.csv"   # adjust path if needed
df = pd.read_csv(CSV_PATH)

# If no explicit time column, create one
if "time" not in df.columns:
    df["time"] = np.arange(len(df)) * 0.1  # assuming 0.1s timestep

# ===============================
# HELPER FUNCTION
# ===============================
def plot_with_ma(x, y, label, window=20):
    ma = y.rolling(window).mean()
    plt.plot(x, y, alpha=0.4, label=f"{label} (raw)")
    plt.plot(x, ma, linewidth=2, label=f"{label} (MA)")

# ===============================
# 1️⃣ ATTITUDE (ROLL, PITCH, YAW)
# ===============================
plt.figure(figsize=(12, 6))
plot_with_ma(df["time"], df["roll"], "Roll")
plot_with_ma(df["time"], df["pitch"], "Pitch")
plot_with_ma(df["time"], df["yaw"], "Yaw")

plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.title("Phase-1 Attitude Response (Hikes & Downs)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ===============================
# 2️⃣ ANGULAR VELOCITY (OMEGA)
# ===============================
plt.figure(figsize=(12, 6))
plot_with_ma(df["time"], df["omega_x"], "ωx")
plot_with_ma(df["time"], df["omega_y"], "ωy")
plot_with_ma(df["time"], df["omega_z"], "ωz")

plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (rad/s)")
plt.title("Phase-1 Angular Velocity (Instability Spikes)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ===============================
# 3️⃣ ANGULAR VELOCITY MAGNITUDE
# ===============================
df["omega_mag"] = np.sqrt(
    df["omega_x"]**2 + df["omega_y"]**2 + df["omega_z"]**2
)

plt.figure(figsize=(12, 5))
plot_with_ma(df["time"], df["omega_mag"], "||ω||", window=30)

plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity Magnitude")
plt.title("Overall Rotational Instability Indicator")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ===============================
# 4️⃣ LINEAR VELOCITY
# ===============================
plt.figure(figsize=(12, 6))
plot_with_ma(df["time"], df["vx"], "Vx")
plot_with_ma(df["time"], df["vy"], "Vy")
plot_with_ma(df["time"], df["vz"], "Vz")

plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Phase-1 Linear Velocity Drift")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ===============================
# 5️⃣ LINEAR ACCELERATION
# ===============================
plt.figure(figsize=(12, 6))
plot_with_ma(df["time"], df["ax"], "Ax")
plot_with_ma(df["time"], df["ay"], "Ay")
plot_with_ma(df["time"], df["az"], "Az")

plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Phase-1 Acceleration Spikes (Wind Disturbance Signature)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ===============================
# 6️⃣ OPTIONAL: WIND FLAG VISUALIZATION
# ===============================
if "wind_flag" in df.columns:
    plt.figure(figsize=(12, 3))
    plt.step(df["time"], df["wind_flag"], where="post")
    plt.xlabel("Time (s)")
    plt.ylabel("Wind Active")
    plt.title("Wind Disturbance Timeline")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

print("✅ Phase-1 visualization complete.")
