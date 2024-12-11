import tkinter as tk
from tkinter import messagebox, ttk
from statistics import mean, stdev
from tkinter import PhotoImage

# Store submissions
submissions = []

# Functions for validation and form submission
def validate_and_submit():
    try:
        # Collect and validate all inputs
        name = name_var.get().strip()
        age_input = age_var.get().strip() 
        sex = sex_var.get()
        ethnicity = ethnicity_var.get()
        disabled_status = disabled_var.get()
        enjoyed = enjoyed_var.get()
        curious = curious_var.get()
        more_science = science_var.get()

        # Check if any field is empty
        if not (name and age_input and sex and ethnicity and disabled_status and enjoyed and curious and more_science):
            raise ValueError("Please answer all questions before continuing.")
        
        # Validate and convert age
        age = int(age_input)  
        
        # Store submission as a dictionary
        submission = {
            "name": name,
            "age": age,
            "sex": sex,
            "ethnicity": ethnicity,
            "disabled_status": disabled_status,
            "enjoyed": enjoyed,
            "curious": curious,
            "science": more_science
        }
        submissions.append(submission)
        messagebox.showinfo("Success", "Thank you for your submission!")
        clear_form()
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input. Please check your entries.")

def clear_form():
    name_var.set("")
    age_var.set("")
    sex_var.set("")
    ethnicity_var.set("")
    disabled_var.set("")
    enjoyed_var.set("")
    curious_var.set("")
    science_var.set("")

# Admin login function
def admin_login():
    # Check if the password is correct
    if admin_password.get() == "password1":
        # Opens the admin window
        admin_window()
    else:
        # Show error message for incorrect password
        messagebox.showerror("Login Error", "Incorrect password. Please try again.")

# Admin window functionality
def admin_window():
    admin = tk.Toplevel(root)
    admin.title("Admin View - Survey Submissions")
    admin.geometry("1200x500")
    
    tk.Label(admin, text="Survey Submissions", font=("Arial", 16, "bold")).pack(pady=10)
    
    # Creates Treeview widget for displaying data
    columns = ("Sub Num", "Name", "Age", "Sex", "Ethnicity", "Disability Status", 
               "Enjoyment of Sculpture", "Were You Curious", "Did It Inspire Interest")
    tree = ttk.Treeview(admin, columns=columns, show="headings")
    tree.pack(fill="both", expand=True, pady=10, padx=10)

    # Defines column headers
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")

    # Inserts data into Treeview
    if submissions:
        for idx, submission in enumerate(submissions, start=1):
            tree.insert("", "end", values=(
                idx, 
                submission["name"], 
                submission["age"], 
                submission["sex"], 
                submission["ethnicity"], 
                submission["disabled_status"], 
                submission["enjoyed"], 
                submission["curious"], 
                submission["science"]
            ))
        
        # Calculates and displays statistics data
        ages = [sub["age"] for sub in submissions]
        male_count = sum(1 for sub in submissions if sub["sex"] == "Male")
        female_count = sum(1 for sub in submissions if sub["sex"] == "Female")
        others_count = sum(1 for sub in submissions if sub["sex"] == "Other")
        
        stats = f"\nAverage age: {mean(ages):.2f}\n" \
                f"Female count: {female_count}\n" \
                f"Male count: {male_count}\n" \
                f"Others count: {others_count}\n" \
                f"Age standard deviation: {stdev(ages):.2f}\n"

        stats_label = tk.Label(admin, text=stats, justify="left", font=("Arial", 12))
        stats_label.pack(pady=10, padx=10, anchor="w")
    else:
        # Show message if there are no submissions
        tree.insert("", "end", values=("No submissions yet",))

# Main Survey GUI
root = tk.Tk()
root.title("Singing Sculpture Survey")
root.geometry("700x1100")

# Adding the Image
try:
    image = tk.PhotoImage(file="./Sculpture.png") 
    tk.Label(image=image).pack(pady=10)
except Exception as e:
    print(f"Error loading image: {e}")

# Form variables
name_var = tk.StringVar()
age_var = tk.StringVar()
sex_var = tk.StringVar()
ethnicity_var = tk.StringVar()
disabled_var = tk.StringVar()
enjoyed_var = tk.StringVar()
curious_var = tk.StringVar()
science_var = tk.StringVar()
admin_password = tk.StringVar()

# Form Layout
tk.Label(root, text="Singing Sculpture Survey", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Name:").pack(anchor="w", padx=10)
tk.Entry(root, textvariable=name_var).pack(fill="x", padx=10)

tk.Label(root, text="Age:").pack(anchor="w", padx=10)
tk.Entry(root, textvariable=age_var).pack(fill="x", padx=10)

tk.Label(root, text="Sex:").pack(anchor="w", padx=10)
tk.OptionMenu(root, sex_var, "Male", "Female", "Other").pack(fill="x", padx=10)

tk.Label(root, text="Ethnicity:").pack(anchor="w", padx=10)
tk.OptionMenu(root, ethnicity_var, "White", "Black", "Asian", "Other").pack(fill="x", padx=10)

tk.Label(root, text="Disabled Status:").pack(anchor="w", padx=10)
tk.OptionMenu(root, disabled_var, "Yes", "No").pack(fill="x", padx=10)

tk.Label(root, text="Did you enjoy the sculpture?").pack(anchor="w", padx=10)
tk.OptionMenu(root, enjoyed_var, "Strongly Agree", "Agree", "Neither Agree nor Disagree", "Disagree", "Strongly Disagree").pack(fill="x", padx=10)

tk.Label(root, text="Were you curious about how it worked?").pack(anchor="w", padx=10)
tk.OptionMenu(root, curious_var, "Strongly Agree", "Agree", "Neither Agree nor Disagree", "Disagree", "Strongly Disagree").pack(fill="x", padx=10)

tk.Label(root, text="Did it inspire any interest in science?").pack(anchor="w", padx=10)
tk.OptionMenu(root, science_var, "Strongly Agree", "Agree", "Neither Agree nor Disagree", "Disagree", "Strongly Disagree").pack(fill="x", padx=10)

tk.Button(root, text="Submit", command=validate_and_submit, bg="green", fg="white").pack(pady=10)

# Admin Section
tk.Label(root, text="Admin Login", font=("Arial", 14, "bold")).pack(pady=20)
admin_frame = tk.Frame(root)
admin_frame.pack(padx=10, pady=5, fill="x")

tk.Entry(admin_frame, textvariable=admin_password, show="*").pack(side="left", expand=True, fill="x", padx=5)
tk.Button(admin_frame, text="Login", command=admin_login, bg="blue", fg="white").pack(side="left", padx=5)

root.mainloop()