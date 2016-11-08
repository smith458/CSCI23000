from tkinter import *
from tkinter import ttk

def createEntries(parent, names, values):
    for x in range(len(names)):
        Label(parent, text=names[x]).grid(row=x, column=0)
        values[x] = Entry(parent)
        values[x].grid(row=x, column=1)
    return values

def main():
    root = Tk()
    n = ttk.Notebook(root)

    tab1 = ttk.Frame(n)
    tab2 = ttk.Frame(n)
    tab3 = ttk.Frame(n)
    tab4 = ttk.Frame(n)
    tab5 = ttk.Frame(n)
    n.add(tab1, text="General")
    n.add(tab2, text="Skills")
    n.add(tab3, text="Proficiencies")
    n.add(tab4, text="Equipment")
    n.add(tab5, text="Spells")
    n.pack()

    skills = [
        "Charisma",
        "Constitution",
        "Dexterity",
        "Intelligence",
        "Strength",
        "Wisdom"]

    valueSkills = [0] * len(skills)

    valueSkills = createEntries(tab2, skills, valueSkills)
    print(valueSkills)

    root.mainloop()
    
if __name__ == "__main__":
    main()
