from src.flow import energy_flow

deployment = energy_flow.deploy(
    name="energy-training-deploy",
    work_pool_name="default",       # ✅ required
    interval=3600                   # every 1 hour (in seconds)
)

if __name__ == "__main__":
    deployment.apply()
