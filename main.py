from datetime import datetime, timedelta
from tkinter import *
from tkinter import ttk


def calculate_cost():
    start_time = datetime.strptime(start_time_entry.get(), '%I:%M %p')
    end_time = datetime.strptime(end_time_entry.get(), '%I:%M %p')
    selected_date = date_var.get()

    if start_time > end_time:
        cost_label.config(text='Error: Start time must be before end time')
        return
    duration = (end_time - start_time).seconds / 3600
    if selected_date in ('Saturday', 'Sunday', 'State Holiday'):
        rate = 1.00
        cost = rate * duration
        cost_label.config(text='Cost: ${:,.2f}'.format(cost))
        return
    elif start_time.weekday() in (0, 1, 2, 3, 4):
        if start_time.hour < 17:
            if duration <= 2:
                rate = 0.75
            else:
                rate = 1.50
        else:
            if duration <= 2:
                rate = 0.50
            else:
                rate = 1.00
    else:
        rate = 0
    cost = rate * duration
    cost_label.config(text='Cost: ${:,.2f}'.format(cost))

if __name__ == "__main__":
    root = Tk()
    root.title('IUEC126 VALIDATION CALCULATOR')

    date_var = StringVar()
    date_var.set('Monday')

    date_label = ttk.Label(root, text='Select date:')
    date_label.grid(row=0, column=0, padx=5, pady=5)
    date_dropdown = ttk.OptionMenu(root, date_var, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'State Holiday')
    date_dropdown.grid(row=0, column=1, padx=5, pady=5)

    start_time_label = ttk.Label(root, text='Enter start time (HH:MM AM/PM):')
    start_time_label.grid(row=1, column=0, padx=5, pady=5)
    start_time_entry = ttk.Entry(root)
    start_time_entry.grid(row=1, column=1, padx=5, pady=5)

    end_time_label = ttk.Label(root, text='Enter end time (HH:MM AM/PM):')
    end_time_label.grid(row=2, column=0, padx=5, pady=5)
    end_time_entry = ttk.Entry(root)
    end_time_entry.grid(row=2, column=1, padx=5, pady=5)

    calculate_button = ttk.Button(root, text='Calculate Cost', command=calculate_cost)
    calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    cost_label = ttk.Label(root)
    cost_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    
root.mainloop()
      



