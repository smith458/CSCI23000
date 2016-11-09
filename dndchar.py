from tkinter import *
from tkinter import ttk

def createEntries(parent, names, values):
    values = {}
    for name in names:
        lab = Label(parent, text=name)
        lab.pack()
        ent = Entry(parent)
        ent.pack()
        values[name] = ent
    return values

def submit(values):
    for x in values:
        values[x].get()
        print(values[x])
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

    #Button(tab2, text="Submit", command=lambda: submit(valueSkills)).grid(column=1, row=6)

    root.mainloop()
    
if __name__ == "__main__":
    main()
