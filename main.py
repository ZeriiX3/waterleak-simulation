# main.py
import threading, subprocess, time
import ingest, simulation

def run_api():
    subprocess.run(["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"])

def run_simulation():
    time.sleep(2)  # attend que l'API soit prête
    simulation.main()

if __name__ == "__main__":
    ingest.download()
    t1 = threading.Thread(target=run_api)
    t2 = threading.Thread(target=run_simulation)
    t1.start(); t2.start()
    t1.join(); t2.join()