from pathlib import Path
import json
import csv

class LeadRepository:
    def __init__(self):
        self.DATA_DIR = Path(__file__).resolve().parent / "data"
        self.DATA_DIR.mkdir(exist_ok=True)
        self.DB_PATH = self.DATA_DIR / "leads.json"

    def _load(self):
        if not self.DB_PATH.exists():
            return[]

        try:
            return json.loads(self.DB_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return[]
            # se corromper, retorna banco vazio

    def _save(self, leads):
        self.DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

    def create_lead(self, lead_dict):
        read_leads = self._load() # a 1° vez será array  vazio []
        read_leads.append(lead_dict)
        self._save(read_leads)

    def read_leads(self):
        return self._load()

    def csv_export(self):
        path_csv = self.DATA_DIR / "leads.csv"
        leads = self._load()
        try:
            with path_csv.open("w", newline ="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "company", "email", "stage", "created"])
                writer.writeheader()
                for lead in leads:
                    writer.writerow(lead)
            return path_csv
        except PermissionError:
            # Caso o arquivo esteja aberto e outro programa, por ex.
            return None