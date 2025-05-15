# FoodDB Project — OOP Assignment

## Description

This project is a command-line tool for managing and searching a food nutrition database stored in JSON format. It uses object-oriented programming concepts with classes for handling JSON data (`JsonDB` and `FoodDB`).

Users can interact through a menu to:

- Search food items by keyword or nutritional range
- Delete records by row ID
- View results with formatted terminal output using `rich`
- Navigate menus with `InquirerPy`

---

## Files

- `food.json` — Data file with food nutrition records  
- `jsonDB.py` — Base class for JSON database operations  
- `foodDB.py` — Subclass handling filtering and deleting food records  
- `menu.py` — Main CLI interface with menus and user interaction  

---

## Requirements

- Python 3.7+  
- Packages: `InquirerPy`, `rich`

Install dependencies:

```bash
pip install InquirerPy rich
