# ingest.py
from huggingface_hub import snapshot_download
from pathlib import Path

PARQUET_DIR = Path("data/parquet")
HF_REPO = "zeriix3/waterleak"

def download():
    if PARQUET_DIR.exists() and any(PARQUET_DIR.rglob("*.parquet")):
        print("✅ Parquet déjà présents, skip download")
        return
    print("📥 Téléchargement depuis HuggingFace...")
    snapshot_download(
        repo_id=HF_REPO,
        repo_type="dataset",
        local_dir=PARQUET_DIR,
    )
    print(f"✅ Parquet téléchargés dans {PARQUET_DIR}")

if __name__ == "__main__":
    download()