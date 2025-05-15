import json

class JsonDB:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []
        self._load_data()

    def _load_data(self):
        try:
            with open(self.filepath, "r") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []

    def _save_data(self):
        with open(self.filepath, "w") as f:
            json.dump(self.data, f, indent=4)

    def create(self, record):
        self.data.append(record)
        self._save_data()
        return record

    def read(self, **filters):
        results = self.data
        for key, value in filters.items():
            results = [
                item for item in results
                if value.lower() in str(item.get(key, "")).lower()
            ]
        return results

    def update(self, record_id, updated_data):
        for i, item in enumerate(self.data):
            if item.get("_id") == record_id:
                self.data[i].update(updated_data)
                self._save_data()
                return self.data[i]
        raise ValueError(f"Record with _id '{record_id}' not found.")

    def delete(self, record_id):
        for i, item in enumerate(self.data):
            if item.get("_id") == record_id:
                removed = self.data.pop(i)
                self._save_data()
                return removed
        raise ValueError(f"Record with _id '{record_id}' not found.")
