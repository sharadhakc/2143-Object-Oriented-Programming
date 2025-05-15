
from jsonDB import JsonDB
from rich import print

class FoodDB(JsonDB):
    """
    FoodDB is a subclass of JsonDB that provides
    a description‐only search over a collection of foods.
    """

    def __init__(self, filepath):
        """
        Initialize the FoodDB with a path to the JSON file.
        """
        super().__init__(filepath)
        self.current = 0
        self._load_data()
        self._save_data()

    def read(self, **filters):
        """
        Read records filtering only by 'description'.
        E.g. read(description="cookie") does a case‐insensitive substring search on 'Shrt_Desc'.
        Returns: a list of {'id': index, 'record': record_dict}
        """
        keyword = filters.get("description", None)
        records = []

        if keyword:
            i = 0
            for record in self.data:
                desc = record.get("Shrt_Desc", "")
                if keyword.lower() in desc.lower():
                    records.append({"id": i, "record": record})
                i += 1

        return records

    def delete(self, row_id):
        """
        Delete by list index.
        """
        print(f"[red]Deleting row ID: {row_id}[/red]")
        if 0 <= row_id < len(self.data):
            removed = self.data.pop(row_id)
            self._save_data()
            return removed
        else:
            raise IndexError(f"Row ID {row_id} out of range.")

if __name__ == "__main__":
    db = FoodDB("food.json")

    # Example: search for any record whose description contains "cookie"
    results = db.read(description="cookie")
    print(results)
