from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
import tkinter as tk
from tkinter import ttk

# Statewide base sales tax rates in percent.
STATE_TAX_RATES = {
    "Alabama": Decimal("4.00"),
    "Alaska": Decimal("0.00"),
    "Arizona": Decimal("5.60"),
    "Arkansas": Decimal("6.50"),
    "California": Decimal("7.25"),
    "Colorado": Decimal("2.90"),
    "Connecticut": Decimal("6.35"),
    "Delaware": Decimal("0.00"),
    "Florida": Decimal("6.00"),
    "Georgia": Decimal("4.00"),
    "Hawaii": Decimal("4.00"),
    "Idaho": Decimal("6.00"),
    "Illinois": Decimal("6.25"),
    "Indiana": Decimal("7.00"),
    "Iowa": Decimal("6.00"),
    "Kansas": Decimal("6.50"),
    "Kentucky": Decimal("6.00"),
    "Louisiana": Decimal("4.45"),
    "Maine": Decimal("5.50"),
    "Maryland": Decimal("6.00"),
    "Massachusetts": Decimal("6.25"),
    "Michigan": Decimal("6.00"),
    "Minnesota": Decimal("6.875"),
    "Mississippi": Decimal("7.00"),
    "Missouri": Decimal("4.225"),
    "Montana": Decimal("0.00"),
    "Nebraska": Decimal("5.50"),
    "Nevada": Decimal("6.85"),
    "New Hampshire": Decimal("0.00"),
    "New Jersey": Decimal("6.625"),
    "New Mexico": Decimal("5.125"),
    "New York": Decimal("4.00"),
    "North Carolina": Decimal("4.75"),
    "North Dakota": Decimal("5.00"),
    "Ohio": Decimal("5.75"),
    "Oklahoma": Decimal("4.50"),
    "Oregon": Decimal("0.00"),
    "Pennsylvania": Decimal("6.00"),
    "Rhode Island": Decimal("7.00"),
    "South Carolina": Decimal("6.00"),
    "South Dakota": Decimal("4.20"),
    "Tennessee": Decimal("7.00"),
    "Texas": Decimal("6.25"),
    "Utah": Decimal("6.10"),
    "Vermont": Decimal("6.00"),
    "Virginia": Decimal("5.30"),
    "Washington": Decimal("6.50"),
    "West Virginia": Decimal("6.00"),
    "Wisconsin": Decimal("5.00"),
    "Wyoming": Decimal("4.00"),
}


class SalesTaxCalculatorApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Sales Tax Calculator")
        self.root.geometry("620x340")
        self.root.minsize(540, 300)

        self.price_var = tk.StringVar()
        self.state_var = tk.StringVar(value="Alabama")
        self.status_var = tk.StringVar(value="Enter a price and choose a state.")

        container = ttk.Frame(self.root, padding=16)
        container.pack(fill=tk.BOTH, expand=True)

        title = ttk.Label(container, text="U.S. Sales Tax Calculator", font=("Segoe UI", 14, "bold"))
        title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 12))

        ttk.Label(container, text="Total Price:", font=("Segoe UI", 10)).grid(
            row=1, column=0, sticky="w", padx=(0, 10), pady=6
        )
        price_entry = ttk.Entry(container, textvariable=self.price_var, width=24)
        price_entry.grid(row=1, column=1, sticky="ew", pady=6)

        ttk.Label(container, text="State:", font=("Segoe UI", 10)).grid(
            row=2, column=0, sticky="w", padx=(0, 10), pady=6
        )
        self.state_combo = ttk.Combobox(
            container,
            textvariable=self.state_var,
            state="readonly",
            values=sorted(STATE_TAX_RATES.keys()),
            width=24,
        )
        self.state_combo.grid(row=2, column=1, sticky="ew", pady=6)

        calculate_button = ttk.Button(container, text="Calculate", command=self.calculate_total)
        calculate_button.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(12, 8))

        status_label = ttk.Label(container, textvariable=self.status_var, foreground="#444444")
        status_label.grid(row=4, column=0, columnspan=2, sticky="w", pady=(0, 10))

        output_frame = ttk.LabelFrame(container, text="Output")
        output_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")

        self.output_table = ttk.Treeview(
            output_frame,
            columns=("price", "tax_rate", "total"),
            show="headings",
            height=1,
        )
        self.output_table.heading("price", text="Price")
        self.output_table.heading("tax_rate", text="Sales Tax Rate")
        self.output_table.heading("total", text="Total")
        self.output_table.column("price", width=180, anchor="center")
        self.output_table.column("tax_rate", width=180, anchor="center")
        self.output_table.column("total", width=180, anchor="center")
        self.output_table.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)

        self.output_table.insert("", tk.END, iid="result", values=("$0.00", "0.00%", "$0.00"))

        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)

        container.columnconfigure(1, weight=1)
        container.rowconfigure(5, weight=1)

        price_entry.focus_set()

    def calculate_total(self) -> None:
        try:
            price = Decimal(self.price_var.get().strip())
            if price < 0:
                raise InvalidOperation
        except (InvalidOperation, ValueError):
            self.status_var.set("Please enter a valid non-negative number for price.")
            return

        selected_state = self.state_var.get()
        tax_rate = STATE_TAX_RATES.get(selected_state, Decimal("0.00"))

        tax_amount = (price * tax_rate / Decimal("100")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        total = (price + tax_amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        price_display = price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        self.output_table.item(
            "result",
            values=(
                f"${price_display}",
                f"{tax_rate.normalize()}%",
                f"${total}",
            ),
        )
        self.status_var.set(f"Using {selected_state} sales tax rate.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SalesTaxCalculatorApp(root)
    root.mainloop()
