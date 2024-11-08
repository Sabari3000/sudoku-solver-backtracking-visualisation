import numpy as np
import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, board, n, update_gui):
        self.board = board
        self.n = n
        self.sq = int(n ** 0.5)
        self.update_gui = update_gui

    def is_valid(self, num, row, col):
        if num in self.board[row]: return False
        if num in self.board[:, col]: return False
        start_row, start_col = self.sq * (row // self.sq), self.sq * (col // self.sq)
        for i in range(self.sq):
            for j in range(self.sq):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve(self):
        empty = self.find_empty()
        if not empty: return True
        row, col = empty
        for num in range(1, self.n + 1):
            if self.is_valid(num, row, col):
                self.board[row][col] = num
                self.update_gui(self.board)
                if self.solve(): return True
                self.board[row][col] = 0
                self.update_gui(self.board)
        return False

    def find_empty(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.size_var = tk.IntVar()
        self.board = None
        self.entries = None
        self.create_size_selection()

    def create_size_selection(self):
        tk.Label(self.root, text="Select Sudoku size (n x n):", font=("Arial", 14)).grid(row=0, column=0, columnspan=3, pady=10)
        sizes = [4, 9]  # Only 4x4 and 9x9 options
        self.size_menu = tk.OptionMenu(self.root, self.size_var, *sizes)
        self.size_menu.grid(row=1, column=0, columnspan=3, pady=5)
        tk.Button(self.root, text="Select Size", font=("Arial", 14), command=self.set_size).grid(row=2, column=0, columnspan=3, pady=10)

    def set_size(self):
        self.size = self.size_var.get()
        if self.size not in [4, 9]:
            messagebox.showerror("Error", "Invalid size selected.")
            return
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.sq = int(self.size ** 0.5)
        self.entries = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) >= 3:
                widget.grid_forget()

        for row in range(self.size):
            for col in range(self.size):
                entry = tk.Entry(self.root, width=5, font=("Arial", 18), justify="center", borderwidth=2, relief="solid")
                color = "#e6e6e6" if (row // self.sq + col // self.sq) % 2 == 0 else "#ffffff"
                entry.config(bg=color, highlightthickness=1, highlightbackground="#cccccc", highlightcolor="#cccccc")
                entry.grid(row=row + 3, column=col, padx=1, pady=1)
                self.entries[row][col] = entry

    def create_buttons(self):
        tk.Button(self.root, text="Solve", font=("Arial", 14), command=self.solve_sudoku).grid(row=self.size + 4, column=0, columnspan=self.size, pady=10)
        tk.Button(self.root, text="Clear", font=("Arial", 14), command=self.clear_board).grid(row=self.size + 5, column=0, columnspan=self.size)

    def is_valid_input(self):
        for i in range(self.size):
            for j in range(self.size):
                value = self.entries[i][j].get()
                if value.isdigit():
                    num = int(value)
                    if num < 1 or num > self.size:
                        return False
                elif value:
                    return False
        return True

    def is_valid_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                num = self.board[i][j]
                if num != 0:
                    self.board[i][j] = 0
                    if not SudokuSolver(self.board, self.size, lambda x: None).is_valid(num, i, j):
                        self.board[i][j] = num
                        return False
                    self.board[i][j] = num
        return True

    def solve_sudoku(self):
        for i in range(self.size):
            for j in range(self.size):
                value = self.entries[i][j].get()
                if value.isdigit():
                    self.board[i][j] = int(value)
                else:
                    self.board[i][j] = 0

        if not self.is_valid_input():
            messagebox.showerror("Error", f"Please enter numbers between 1 and {self.size}.")
            return

        if not self.is_valid_grid():
            messagebox.showerror("Error", "The initial Sudoku board has conflicts. Please correct it.")
            return

        solver = SudokuSolver(self.board, self.size, self.update_board)
        if solver.solve():
            messagebox.showinfo("Success", "Sudoku Solved!")
        else:
            messagebox.showerror("Error", "No solution exists.")

    def update_board(self, board):
        for i in range(self.size):
            for j in range(self.size):
                self.entries[i][j].delete(0, tk.END)
                if board[i][j] != 0:
                    self.entries[i][j].insert(tk.END, str(board[i][j]))
                else:
                    self.entries[i][j].insert(tk.END, "")
        self.root.update_idletasks()

    def clear_board(self):
        for i in range(self.size):
            for j in range(self.size):
                self.entries[i][j].delete(0, tk.END)
        self.board = np.zeros((self.size, self.size), dtype=int)

root = tk.Tk()
SudokuGUI(root)
root.mainloop()