from InquirerPy import inquirer
from foodDB import FoodDB
from rich import print
from rich.panel import Panel
from rich.console import Console
import os
import shutil

# Terminal sizing
term_size = shutil.get_terminal_size()
WIDTH = int(term_size.columns * 0.75)
HEIGHT = int(term_size.lines * 0.75)

console = Console()
db = FoodDB("food.json")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def submenu_create():
    clear_screen()
    console.print(Panel("[bold cyan]Create New Food Item[/bold cyan]", width=WIDTH))
    desc = console.input("[blue]Description: [/blue]")
    kcal = console.input("[blue]Calories (kcal): [/blue]")
    prot = console.input("[blue]Protein (g): [/blue]")
    fat = console.input("[blue]Fat (g): [/blue]")

    record = {
        "_id": desc[:8].replace(" ", "_") + str(len(db.data)),
        "Shrt_Desc": desc,
        "Energ_Kcal": kcal,
        "Protein": prot,
        "Lipid_Tot": fat,
    }
    db.create(record)
    console.print(Panel(f"[green]Created:[/green] {desc} ({kcal} kcal)", title="Success", width=WIDTH))
    console.input("Press ENTER to continue")


def submenu_search():
    clear_screen()
    console.print(Panel("[bold cyan]Search by Description[/bold cyan]", width=WIDTH))
    keyword = console.input("[blue]Enter keyword to search: [/blue]")
    results = db.read(description=keyword)

    if not results:
        console.print(Panel(f"[red]No items found containing '{keyword}'[/red]", width=WIDTH))
    else:
        console.print(Panel(f"[green]Found {len(results)} item(s):[/green]", width=WIDTH))
        for idx, rec in enumerate(results):
            console.print(f"{idx}. {rec['Shrt_Desc']} — {rec['Energ_Kcal']} kcal")
    console.input("Press ENTER to continue")


def submenu_update():
    clear_screen()
    console.print(Panel("[bold cyan]Update Food Item[/bold cyan]", width=WIDTH))
    idx_str = console.input("[blue]Enter row index to update: [/blue]")
    if not idx_str.isdigit():
        console.print("[red]Invalid index[/red]")
        console.input("Press ENTER to continue")
        return
    idx = int(idx_str)
    if idx < 0 or idx >= len(db.data):
        console.print("[red]Index out of range[/red]")
        console.input("Press ENTER to continue")
        return

    record = db.data[idx]
    console.print(f"Current: {record['Shrt_Desc']} — {record['Energ_Kcal']} kcal")
    new_desc = console.input("[blue]New Description (blank to skip): [/blue]")
    new_kcal = console.input("[blue]New Calories (blank to skip): [/blue]")
    new_prot = console.input("[blue]New Protein (g) (blank to skip): [/blue]")
    new_fat = console.input("[blue]New Fat (g) (blank to skip): [/blue]")

    updates = {}
    if new_desc: updates["Shrt_Desc"] = new_desc
    if new_kcal: updates["Energ_Kcal"] = new_kcal
    if new_prot: updates["Protein"] = new_prot
    if new_fat: updates["Lipid_Tot"] = new_fat

    if updates:
        db.update(record["_id"], updates)
        console.print(Panel("[green]Update successful![/green]", width=WIDTH))
    else:
        console.print("[yellow]No changes made[/yellow]")
    console.input("Press ENTER to continue")


def submenu_delete():
    clear_screen()
    console.print(Panel("[bold cyan]Delete Food Item[/bold cyan]", width=WIDTH))
    idx_str = console.input("[blue]Enter row index to delete: [/blue]")
    if not idx_str.isdigit():
        console.print("[red]Invalid index[/red]")
        console.input("Press ENTER to continue")
        return
    idx = int(idx_str)
    if idx < 0 or idx >= len(db.data):
        console.print("[red]Index out of range[/red]")
        console.input("Press ENTER to continue")
        return

    record = db.data[idx]
    db.delete(record["_id"])
    console.print(Panel(f"[green]Deleted:[/green] {record['Shrt_Desc']}", width=WIDTH))
    console.input("Press ENTER to continue")


def main_menu():
    while True:
        clear_screen()
        choice = inquirer.select(
            message="CRUD Menu:",
            choices=["Create", "Search", "Update", "Delete", "Exit"]
        ).execute()

        if choice == "Create":
            submenu_create()
        elif choice == "Search":
            submenu_search()
        elif choice == "Update":
            submenu_update()
        elif choice == "Delete":
            submenu_delete()
        else:
            console.print("[bold red]Goodbye![/bold red]")
            break


if __name__ == "__main__":
    main_menu()
