# main.py
import threading, subprocess, time, argparse
import ingest, simulation

def run_api():
    subprocess.run(["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"])

def run_simulation(scenario):
    time.sleep(2)  # attend que l'API soit prête
    simulation.main(scenario)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="ideal", choices=simulation.SCENARIOS.keys())
    args = parser.parse_args()

    ingest.download()
    t1 = threading.Thread(target=run_api)
    t2 = threading.Thread(target=run_simulation, args=(args.scenario,))
    t1.start(); t2.start()
    t1.join(); t2.join()