"""
Python Exercises for Beginners
A GUI application guiding new programmers through 42 Python exercises
from "Python Programming Exercises, Gently Explained" by Al Sweigart.
"""

import sys
if "--run-script" in sys.argv:
    script_idx = sys.argv.index("--run-script") + 1
    if script_idx < len(sys.argv):
        import runpy
        # Hide the --run-script from argv
        script_path = sys.argv[script_idx]
        sys.argv = [script_path]
        try:
            runpy.run_path(script_path, run_name="__main__")
        except SystemExit as e:
            sys.exit(e.code)
        except Exception as e:
            import traceback
            traceback.print_exc()
        sys.exit(0)

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os
import json
import io
import re
import threading
import tempfile
import time
from contextlib import redirect_stdout, redirect_stderr

from exercises_data import EXERCISES
from solutions_data import SOLUTIONS

# ── Theme ─────────────────────────────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Paths — frozen (PyInstaller) vs plain source
if getattr(sys, "frozen", False):
    # Running as a packaged executable
    _BUNDLE_DIR = sys._MEIPASS          # where bundled data lives
    _EXE_DIR    = os.path.dirname(sys.executable)  # next to the .exe/binary
else:
    _BUNDLE_DIR = os.path.dirname(os.path.abspath(__file__))
    _EXE_DIR    = _BUNDLE_DIR

APP_DIR       = _EXE_DIR               # user-writable (progress, solutions)
PROGRESS_FILE = os.path.join(APP_DIR, "progress.json")
SOLUTIONS_DIR = os.path.join(APP_DIR, "my_solutions")
os.makedirs(SOLUTIONS_DIR, exist_ok=True)

# Import exercise data (use bundle dir so PyInstaller can find the modules)
sys.path.insert(0, _BUNDLE_DIR)

# Path to the icon image
ICON_PATH = os.path.join(_BUNDLE_DIR, "images", "PythonExercisesIcon.png")


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"completed": [], "unlocked": [1], "current": 1, "theme": "Dark"}


def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def load_user_solution(exercise_num):
    path = os.path.join(SOLUTIONS_DIR, f"exercise_{exercise_num:02d}.py")
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return ""


def save_user_solution(exercise_num, code):
    path = os.path.join(SOLUTIONS_DIR, f"exercise_{exercise_num:02d}.py")
    with open(path, "w") as f:
        f.write(code)


# ── Colors ────────────────────────────────────────────────────────────────────
# Each value is a (light_mode, dark_mode) tuple — CTk picks automatically.
COLORS = {
    "bg_dark":      ("#e8edf2", "#0f1117"),
    "bg_panel":     ("#f0f4f8", "#1a1d2e"),
    "bg_card":      ("#e2e8f0", "#252840"),
    "accent":       ("#2563eb", "#4f8ef7"),
    "accent_hover": ("#1d4ed8", "#6ba0f9"),
    "success":      ("#16a34a", "#2ecc71"),
    "error":        ("#dc2626", "#e74c3c"),
    "warning":      ("#d97706", "#f39c12"),
    "text":         ("#1e293b", "#e8eaf6"),
    "text_muted":   ("#64748b", "#9098b8"),
    "border":       ("#cbd5e1", "#2d3154"),
    "completed":    ("#dcfce7", "#1a3a2a"),
    "locked":       ("#f1f5f9", "#1a1d2e"),
    "code_bg":      ("#f8fafc", "#0d0f1a"),
}

FONTS = {
    "title": ("Inter", 20, "bold"),
    "heading": ("Inter", 14, "bold"),
    "body": ("Inter", 12),
    "small": ("Inter", 11),
    "mono": ("JetBrains Mono", 12) if sys.platform != "win32" else ("Consolas", 12),
    "mono_sm": ("JetBrains Mono", 11) if sys.platform != "win32" else ("Consolas", 11),
}


# ── Syntax Highlighter ──────────────────────────────────────────────────────────────────

class PythonHighlighter:
    """Live syntax highlighter for a CTkTextbox using tk's tag system."""

    KEYWORDS = frozenset([
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
        'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
        'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
        'while', 'with', 'yield'
    ])
    BUILTINS = frozenset([
        'abs', 'all', 'any', 'bool', 'bytearray', 'bytes', 'callable', 'chr',
        'classmethod', 'complex', 'dict', 'dir', 'divmod', 'enumerate', 'eval',
        'exec', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals',
        'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance',
        'issubclass', 'iter', 'len', 'list', 'locals', 'map', 'max', 'min',
        'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
        'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
        'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type',
        'vars', 'zip'
    ])

    # Combined regex: order matters — strings/comments FIRST to avoid
    # matching keywords inside string literals.
    _PATTERN = re.compile(
        r'(?P<triple_dq>"""[\s\S]*?""")'         # triple double-quoted string
        r"|(?P<triple_sq>'''[\s\S]*?''')"
        r'|(?P<string_dq>"(?:[^"\\\n]|\\.)*")'
        r"|(?P<string_sq>'(?:[^'\\\n]|\\.)*')"
        r'|(?P<comment>#[^\n]*)'
        r'|(?P<number>\b\d+\.?\d*(?:[eE][+-]?\d+)?j?\b)'
        r'|(?P<word>\b[A-Za-z_]\w*\b)'
    )

    # Tag colours: (light_mode_colour, dark_mode_colour)
    TAG_COLORS = {
        'kw':      ('#b45309', '#ff9d00'),   # amber — keywords
        'builtin': ('#1d4ed8', '#56b6c2'),   # blue/teal — built-ins
        'string':  ('#15803d', '#98c379'),   # green — strings
        'comment': ('#6b7280', '#7f848e'),   # grey — comments
        'number':  ('#7c3aed', '#d19a66'),   # purple/gold — numbers
        'defname': ('#9a3412', '#e5c07b'),   # red-brown/pale-yellow — def/class names
    }

    def __init__(self, ctk_textbox):
        self._box = ctk_textbox
        self._tw = ctk_textbox._textbox    # raw tk.Text widget
        self._after_id = None
        self._configure_tags()
        ctk_textbox.bind('<KeyRelease>', self._on_key)

    def _configure_tags(self):
        mode = ctk.get_appearance_mode()
        i = 0 if mode == 'Light' else 1
        for tag, colors in self.TAG_COLORS.items():
            self._tw.tag_configure(tag, foreground=colors[i])
        # Ensure tags render on top of the default text colour
        for tag in self.TAG_COLORS:
            self._tw.tag_raise(tag)

    def update_theme(self):
        """Call after set_appearance_mode() to refresh tag colours."""
        self._configure_tags()
        self._highlight()

    def _on_key(self, event=None):
        if self._after_id:
            self._box.after_cancel(self._after_id)
        self._after_id = self._box.after(150, self._highlight)

    def _highlight(self):
        tw = self._tw
        code = self._box.get('1.0', 'end-1c')
        # Remove previous tags
        for tag in self.TAG_COLORS:
            tw.tag_remove(tag, '1.0', 'end')

        prev_kw = None
        for m in self._PATTERN.finditer(code):
            kind = m.lastgroup
            si = f'1.0+{m.start()}c'
            ei = f'1.0+{m.end()}c'

            if kind == 'word':
                word = m.group()
                if prev_kw in ('def', 'class'):
                    tw.tag_add('defname', si, ei)
                    prev_kw = None
                elif word in self.KEYWORDS:
                    tw.tag_add('kw', si, ei)
                    prev_kw = word        # remember 'def'/'class' for next word
                elif word in self.BUILTINS:
                    tw.tag_add('builtin', si, ei)
                    prev_kw = None
                else:
                    prev_kw = None
            elif kind in ('string_dq', 'string_sq', 'triple_dq', 'triple_sq'):
                tw.tag_add('string', si, ei)
                prev_kw = None
            elif kind == 'comment':
                tw.tag_add('comment', si, ei)
                prev_kw = None
            elif kind == 'number':
                tw.tag_add('number', si, ei)
                prev_kw = None


class ExerciseApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Python Exercises for Beginners")
        self.geometry("1400x860")
        self.minsize(1100, 700)
        self.configure(fg_color=COLORS["bg_dark"])

        try:
            # Set window icon (taskbar & title bar)
            if sys.platform == "linux":
                icon = tk.PhotoImage(file=ICON_PATH)
                self.iconphoto(True, icon)
            else:
                self.iconbitmap(ICON_PATH)
        except Exception as e:
            print(f"Warning: Could not load application icon: {e}")

        self.progress = load_progress()
        self.current_exercise_index = 0
        self.running_process = None

        # Apply saved theme before building UI
        ctk.set_appearance_mode(self.progress.get("theme", "Dark"))

        # Find the current exercise in the list
        for i, ex in enumerate(EXERCISES):
            if ex["number"] == self.progress.get("current", 1):
                self.current_exercise_index = i
                break

        self._build_ui()
        self._load_exercise(self.current_exercise_index)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    # ── UI Build ──────────────────────────────────────────────────────────────

    def _build_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Left sidebar: exercise list
        self.sidebar = ctk.CTkFrame(self, width=220, fg_color=COLORS["bg_panel"],
                                     corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        # Sidebar header
        sidebar_header = ctk.CTkFrame(self.sidebar, fg_color=COLORS["bg_card"],
                                       corner_radius=0, height=60)
        sidebar_header.pack(fill="x")
        sidebar_header.pack_propagate(False)
        ctk.CTkLabel(sidebar_header, text="🐍 Exercises",
                     font=FONTS["heading"], text_color=COLORS["text"]).pack(
            anchor="w", padx=16, pady=16)

        # Progress label
        self.progress_label = ctk.CTkLabel(
            self.sidebar, text="", font=FONTS["small"],
            text_color=COLORS["text_muted"])
        self.progress_label.pack(anchor="w", padx=16, pady=(8, 4))

        # Scrollable exercise list
        self.exercise_list_frame = ctk.CTkScrollableFrame(
            self.sidebar, fg_color=COLORS["bg_panel"], scrollbar_button_color=COLORS["border"])
        self.exercise_list_frame.pack(fill="both", expand=True, padx=4, pady=4)

        self.exercise_buttons = []
        for ex in EXERCISES:
            btn = ctk.CTkButton(
                self.exercise_list_frame,
                text=f"#{ex['number']:02d} {ex['title']}",
                font=FONTS["small"],
                anchor="w",
                height=36,
                corner_radius=6,
                fg_color="transparent",
                hover_color=COLORS["bg_card"],
                text_color=COLORS["text_muted"],
                command=lambda i=EXERCISES.index(ex): self._on_exercise_click(i)
            )
            btn.pack(fill="x", padx=4, pady=1)
            self.exercise_buttons.append(btn)

        # Theme selector
        ctk.CTkLabel(
            self.sidebar, text="🎨 Theme",
            font=FONTS["small"], text_color=COLORS["text_muted"]
        ).pack(anchor="w", padx=16, pady=(8, 2))

        current_theme = self.progress.get("theme", "Dark")
        self.theme_selector = ctk.CTkSegmentedButton(
            self.sidebar,
            values=["Light", "Dark", "System"],
            command=self._set_theme,
            font=FONTS["small"],
            height=28,
        )
        self.theme_selector.set(current_theme)
        self.theme_selector.pack(fill="x", padx=8, pady=(0, 4))

        # Reset button at bottom
        ctk.CTkButton(
            self.sidebar, text="↺ Reset Progress",
            font=FONTS["small"], fg_color="transparent",
            text_color=COLORS["text_muted"], hover_color=COLORS["bg_card"],
            height=36, command=self._reset_progress
        ).pack(fill="x", padx=8, pady=(4, 12))

        # Main content area
        self.main_frame = ctk.CTkFrame(self, fg_color=COLORS["bg_dark"], corner_radius=0)
        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Top bar with exercise title and nav buttons
        self.top_bar = ctk.CTkFrame(self.main_frame, fg_color=COLORS["bg_panel"],
                                     height=60, corner_radius=0)
        self.top_bar.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.top_bar.grid_propagate(False)
        self.top_bar.grid_columnconfigure(1, weight=1)

        self.prev_btn = ctk.CTkButton(
            self.top_bar, text="← Prev", width=80, height=36,
            fg_color=COLORS["bg_card"], hover_color=COLORS["border"],
            text_color=COLORS["text"],
            font=FONTS["small"], command=self._prev_exercise)
        self.prev_btn.grid(row=0, column=0, padx=(12, 8), pady=12)

        self.exercise_title_label = ctk.CTkLabel(
            self.top_bar, text="", font=FONTS["title"],
            text_color=COLORS["text"])
        self.exercise_title_label.grid(row=0, column=1, padx=8, pady=12, sticky="w")

        self.status_badge = ctk.CTkLabel(
            self.top_bar, text="", font=FONTS["small"],
            text_color=COLORS["text_muted"])
        self.status_badge.grid(row=0, column=2, padx=8, pady=12)

        self.next_btn = ctk.CTkButton(
            self.top_bar, text="Next →", width=80, height=36,
            fg_color=COLORS["bg_card"], hover_color=COLORS["border"],
            text_color=COLORS["text"],
            font=FONTS["small"], command=self._next_exercise)
        self.next_btn.grid(row=0, column=3, padx=(8, 12), pady=12)

        # Left panel: description + expected output
        left_panel = ctk.CTkFrame(self.main_frame, fg_color=COLORS["bg_panel"],
                                   corner_radius=10)
        left_panel.grid(row=1, column=0, padx=(12, 6), pady=12, sticky="nsew")
        left_panel.grid_rowconfigure(1, weight=2)
        left_panel.grid_rowconfigure(3, weight=1)
        left_panel.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(left_panel, text="📋 Description",
                     font=FONTS["heading"], text_color=COLORS["accent"],
                     anchor="w").grid(row=0, column=0, padx=16, pady=(12, 4), sticky="w")

        self.desc_text = ctk.CTkTextbox(
            left_panel, font=FONTS["body"],
            fg_color=COLORS["bg_card"], text_color=COLORS["text"],
            border_color=COLORS["border"], border_width=1,
            corner_radius=6, wrap="word", state="disabled")
        self.desc_text.grid(row=1, column=0, padx=12, pady=(0, 8), sticky="nsew")

        ctk.CTkLabel(left_panel, text="🎯 Expected Output / Validation",
                     font=FONTS["heading"], text_color=COLORS["accent"],
                     anchor="w").grid(row=2, column=0, padx=16, pady=(4, 4), sticky="w")

        self.expected_text = ctk.CTkTextbox(
            left_panel, font=FONTS["mono_sm"],
            fg_color=COLORS["code_bg"], text_color=("#1e40af", "#a8e6cf"),
            border_color=COLORS["border"], border_width=1,
            corner_radius=6, state="disabled")
        self.expected_text.grid(row=3, column=0, padx=12, pady=(0, 12), sticky="nsew")

        # Right panel: code editor + console
        right_panel = ctk.CTkFrame(self.main_frame, fg_color=COLORS["bg_panel"],
                                    corner_radius=10)
        right_panel.grid(row=1, column=1, padx=(6, 12), pady=12, sticky="nsew")
        right_panel.grid_rowconfigure(1, weight=3)
        right_panel.grid_rowconfigure(5, weight=2)
        right_panel.grid_columnconfigure(0, weight=1)

        # Code editor header with buttons
        code_header = ctk.CTkFrame(right_panel, fg_color="transparent")
        code_header.grid(row=0, column=0, padx=12, pady=(12, 4), sticky="ew")
        code_header.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(code_header, text="✏️ Code Editor",
                     font=FONTS["heading"], text_color=COLORS["accent"]).grid(
            row=0, column=0, sticky="w")

        btn_frame = ctk.CTkFrame(code_header, fg_color="transparent")
        btn_frame.grid(row=0, column=1, sticky="e")

        self.clear_btn = ctk.CTkButton(
            btn_frame, text="Clear", width=60, height=28,
            fg_color=COLORS["bg_card"], hover_color=COLORS["border"],
            text_color=COLORS["text"],
            font=FONTS["small"], command=self._clear_code)
        self.clear_btn.pack(side="right", padx=(4, 0))

        self.hint_btn = ctk.CTkButton(
            btn_frame, text="💡 Hint", width=70, height=28,
            fg_color=COLORS["bg_card"], hover_color=COLORS["border"],
            text_color=COLORS["text"],
            font=FONTS["small"], command=self._show_hint)
        self.hint_btn.pack(side="right", padx=4)

        self.solution_btn = ctk.CTkButton(
            btn_frame, text="🔑 Solution", width=90, height=28,
            fg_color=COLORS["bg_card"], hover_color=COLORS["border"],
            text_color=COLORS["text"],
            font=FONTS["small"], command=self._show_solution)
        self.solution_btn.pack(side="right", padx=4)

        # Code editor
        self.code_editor = ctk.CTkTextbox(
            right_panel, font=FONTS["mono"],
            fg_color=COLORS["code_bg"], text_color=("#1e293b", "#e8eaf6"),
            border_color=COLORS["border"], border_width=1,
            corner_radius=6, wrap="none")
        self.code_editor.grid(row=1, column=0, padx=12, pady=(0, 8), sticky="nsew")
        self.code_editor.bind("<Tab>", self._handle_tab)
        # Attach syntax highlighter
        self.highlighter = PythonHighlighter(self.code_editor)

        # Console header with run/check buttons
        console_header = ctk.CTkFrame(right_panel, fg_color="transparent")
        console_header.grid(row=2, column=0, padx=12, pady=(4, 4), sticky="ew")
        console_header.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(console_header, text="🖥️ Output Console",
                     font=FONTS["heading"], text_color=COLORS["accent"]).grid(
            row=0, column=0, sticky="w")

        run_frame = ctk.CTkFrame(console_header, fg_color="transparent")
        run_frame.grid(row=0, column=1, sticky="e")

        self.run_btn = ctk.CTkButton(
            run_frame, text="▶ Run", width=80, height=28,
            fg_color=COLORS["accent"], hover_color=COLORS["accent_hover"],
            font=FONTS["small"], command=self._run_code)
        self.run_btn.pack(side="right", padx=(4, 0))

        self.check_btn = ctk.CTkButton(
            run_frame, text="✓ Submit", width=90, height=28,
            fg_color="#1a6b3c", hover_color="#2a8c52",
            font=FONTS["small"], command=self._check_solution)
        self.check_btn.pack(side="right", padx=4)

        # ── stdin input area ──────────────────────────────────────────────────
        stdin_header = ctk.CTkFrame(right_panel, fg_color="transparent")
        stdin_header.grid(row=3, column=0, padx=12, pady=(0, 2), sticky="ew")
        ctk.CTkLabel(stdin_header, text="⌨️ Program Input  (one value per line — fed to input() calls)",
                     font=FONTS["small"], text_color=COLORS["text_muted"]).pack(side="left")

        self.stdin_input = ctk.CTkTextbox(
            right_panel, font=FONTS["mono_sm"],
            fg_color=COLORS["bg_card"], text_color=("#92400e", "#ffe08a"),
            border_color=COLORS["border"], border_width=1,
            corner_radius=6, wrap="none", height=56)
        self.stdin_input.grid(row=4, column=0, padx=12, pady=(0, 4), sticky="ew")

        # Output console
        self.console_output = ctk.CTkTextbox(
            right_panel, font=FONTS["mono_sm"],
            fg_color=COLORS["code_bg"], text_color=("#166534", "#c8ffc8"),
            border_color=COLORS["border"], border_width=1,
            corner_radius=6, state="disabled", wrap="none")
        self.console_output.grid(row=5, column=0, padx=12, pady=(0, 12), sticky="nsew")

        # Bottom status bar
        self.status_bar = ctk.CTkFrame(self.main_frame, fg_color=COLORS["bg_panel"],
                                        height=32, corner_radius=0)
        self.status_bar.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.status_bar.grid_propagate(False)

        self.status_msg = ctk.CTkLabel(
            self.status_bar, text="", font=FONTS["small"],
            text_color=COLORS["text_muted"])
        self.status_msg.pack(side="left", padx=16, pady=4)

        self._update_sidebar_buttons()

    # ── Exercise Loading ──────────────────────────────────────────────────────

    def _load_exercise(self, index):
        self.current_exercise_index = index
        ex = EXERCISES[index]
        num = ex["number"]

        # Update title
        self.exercise_title_label.configure(
            text=f"Exercise #{num}: {ex['title']}")

        # Update status badge
        if num in self.progress["completed"]:
            self.status_badge.configure(text="✅ Completed", text_color=COLORS["success"])
        elif num in self.progress["unlocked"]:
            self.status_badge.configure(text="🔓 Unlocked", text_color=COLORS["accent"])
        else:
            self.status_badge.configure(text="🔒 Locked", text_color=COLORS["text_muted"])

        # Update description
        self._set_text(self.desc_text, ex["description"])

        # Update expected output / validation info
        vtype = ex.get("validation_type", "assert")
        if vtype == "assert" and ex.get("asserts"):
            expected_content = (
                "🤖  Auto-tested on Submit — do NOT copy these into your code.\n"
                "    Just write the required function(s). When you click\n"
                "    \u2713 Submit, the app runs these checks automatically:\n\n"
            )
            expected_content += "\n".join(ex["asserts"])
        elif vtype == "output" and ex.get("expected_output"):
            expected_content = f"Expected output of `{ex.get('run_code', '')}` :\n\n"
            expected_content += ex["expected_output"]
        elif vtype == "output_contains":
            expected_content = "Output must contain all of:\n"
            for s in ex.get("output_must_contain", []):
                expected_content += f'  • "{s}"\n'
        else:
            expected_content = ex.get("validation_note", "")
        self._set_text(self.expected_text, expected_content)

        # Load user's saved code, or show starter template
        saved_code = load_user_solution(num)
        self.code_editor.delete("1.0", "end")
        if saved_code:
            self.code_editor.insert("1.0", saved_code)
        else:
            template = (
                f"# Exercise #{num}: {ex['title']}\n"
                f"# Prerequisites: {ex['prerequisites']}\n\n"
                "# --- SOLUTION CODE ---\n"
                "# Write your exercise solution below. This is what gets evaluated\n"
                "# when you click 'Submit'.\n\n\n\n"
                "# --- TESTING CODE ---\n"
                "# Write any code you want to manually test below this line.\n"
                "# This section is run when you click 'Run', but is completely\n"
                "# ignored by the 'Submit' validation.\n\n"
            )
            self.code_editor.insert("1.0", template)
        self.highlighter._highlight()

        # Clear console
        self._set_console("")

        # Update nav buttons
        self.prev_btn.configure(state="normal" if index > 0 else "disabled")
        self.next_btn.configure(state="normal" if index < len(EXERCISES) - 1 else "disabled")

        # Update sidebar
        self._update_sidebar_buttons()
        self.progress["current"] = num
        save_progress(self.progress)

        self._set_status(f"Exercise #{num} loaded. Prerequisites: {ex['prerequisites']}")

    def _update_sidebar_buttons(self):
        completed = self.progress.get("completed", [])
        unlocked = self.progress.get("unlocked", [1])
        current_num = EXERCISES[self.current_exercise_index]["number"]

        total = len(EXERCISES)
        done = len(completed)
        self.progress_label.configure(text=f"{done}/{total} completed")

        for i, (ex, btn) in enumerate(zip(EXERCISES, self.exercise_buttons)):
            num = ex["number"]
            is_current = (num == current_num)

            if num in completed:
                color = COLORS["success"] if is_current else "#1e4d33"
                text_color = "#ffffff"
                prefix = "✅"
            elif num in unlocked:
                color = COLORS["accent"] if is_current else "transparent"
                text_color = COLORS["text"] if is_current else COLORS["text_muted"]
                prefix = "▶" if is_current else "·"
            else:
                color = "transparent"
                text_color = COLORS["border"]
                prefix = "🔒"

            btn.configure(
                text=f" {prefix} #{num:02d} {ex['title']}",
                fg_color=color,
                text_color=text_color,
                state="normal" if num in unlocked or num in completed else "disabled"
            )

    # ── Code Execution ────────────────────────────────────────────────────────

    def _run_code(self):
        code = self.code_editor.get("1.0", "end").strip()
        if not code:
            self._set_console("⚠ No code to run.")
            return

        # Save code before running
        ex = EXERCISES[self.current_exercise_index]
        save_user_solution(ex["number"], code)

        # Grab any user-supplied stdin lines
        stdin_text = self.stdin_input.get("1.0", "end")

        self._set_console("Running...\n", color="#888")
        self.run_btn.configure(state="disabled", text="⏳ Running")

        def run_in_thread():
            output, error = self._execute_code(code, stdin_input=stdin_text)
            self.after(0, lambda: self._show_run_result(output, error))

        threading.Thread(target=run_in_thread, daemon=True).start()

    def _execute_code(self, code, stdin_input=None):
        """Execute code in a subprocess and return (stdout, stderr)."""
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py',
                                              delete=False, dir=APP_DIR) as f:
                f.write(code)
                tmpfile = f.name

            cmd = [sys.executable, tmpfile]
            if getattr(sys, "frozen", False):
                cmd = [sys.executable, "--run-script", tmpfile]

            result = subprocess.run(
                cmd,
                input=stdin_input,
                capture_output=True, text=True,
                timeout=10, cwd=APP_DIR
            )
            os.unlink(tmpfile)
            return result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            if tmpfile:
                try:
                    os.unlink(tmpfile)
                except:
                    pass
            return "", "⏰ Timeout: Program ran for more than 10 seconds."
        except Exception as e:
            return "", f"Error executing code: {e}"

    def _show_run_result(self, output, error):
        self.run_btn.configure(state="normal", text="▶ Run")
        if error:
            self._set_console(f"OUTPUT:\n{output}\n\nERROR:\n{error}", color="#ff8888")
        else:
            self._set_console(output if output else "(No output)", color="#c8ffc8")

    def _check_solution(self):
        code = self.code_editor.get("1.0", "end").strip()
        if not code:
            self._set_console("⚠ Write some code first!")
            return

        ex = EXERCISES[self.current_exercise_index]
        save_user_solution(ex["number"], code)
        
        # Only validate the solution code, ignore the testing code section
        if "# --- TESTING CODE ---" in code:
            code = code.split("# --- TESTING CODE ---")[0].strip()

        self._set_console("Checking solution...\n", color="#888")
        self.check_btn.configure(state="disabled")

        def check_in_thread():
            passed, message = self._validate_solution(code, ex)
            self.after(0, lambda: self._show_check_result(passed, message, ex))

        threading.Thread(target=check_in_thread, daemon=True).start()

    def _validate_solution(self, code, ex):
        """Run validation based on exercise type."""
        vtype = ex.get("validation_type", "assert")

        if vtype == "assert":
            # Build test code: user code + assert statements
            asserts_code = "\n".join(ex.get("asserts", []))
            test_code = code + "\n\n" + asserts_code
            output, error = self._execute_code(test_code)
            if error:
                return False, f"❌ Tests failed:\n\n{error}"
            return True, f"✅ All tests passed!\n\nOutput:\n{output}"

        elif vtype == "output":
            run_code = ex.get("run_code", "")
            test_code = code + "\n\n" + run_code
            output, error = self._execute_code(test_code)
            if error:
                return False, f"❌ Error:\n{error}"
            expected = ex.get("expected_output", "").strip()
            actual = output.strip()
            if actual == expected:
                return True, f"✅ Output matches!\n\nYour output:\n{output}"
            else:
                return False, (f"❌ Output doesn't match.\n\n"
                               f"Expected:\n{expected}\n\n"
                               f"Your output:\n{output}")

        elif vtype == "output_contains":
            run_code = ex.get("run_code", "")
            test_code = code + ("\n\n" + run_code if run_code else "")
            output, error = self._execute_code(test_code)
            if error:
                return False, f"❌ Error:\n{error}"
            must_contain = ex.get("output_must_contain", [])
            missing = [s for s in must_contain if s not in output]
            if not missing:
                return True, f"✅ Output contains all required text!\n\nOutput:\n{output}"
            else:
                return False, (f"❌ Output missing required text:\n"
                               + "\n".join(f'  • "{s}"' for s in missing)
                               + f"\n\nYour output:\n{output}")

        elif vtype == "interactive":
            # For interactive programs like Hello World, supply 'Alice' as stdin
            output, error = self._execute_code(code, stdin_input="Alice\n")
            if error:
                return False, f"❌ Error running program:\n{error}"
            # Check if output contains expected strings
            if "Hello, world!" in output and "Hello, Alice" in output:
                return True, f"✅ Program runs and produces expected output!\n\nOutput:\n{output}"
            else:
                return False, (f"❌ Output doesn't look right.\n\n"
                               f"Make sure your program prints 'Hello, world!' and greets by name.\n"
                               f"The Submit check sends 'Alice' as input automatically.\n\n"
                               f"Your output:\n{output}")

        return False, "Unknown validation type"

    def _show_check_result(self, passed, message, ex):
        self.check_btn.configure(state="normal")
        num = ex["number"]

        if passed:
            self._set_console(message, color="#a8e6cf")
            if num not in self.progress["completed"]:
                self.progress["completed"].append(num)
                # Unlock next exercise
                next_num = num + 1
                if next_num <= 42 and next_num not in self.progress["unlocked"]:
                    self.progress["unlocked"].append(next_num)
                save_progress(self.progress)
                self._update_sidebar_buttons()
                self._show_completion_dialog(ex)
            else:
                self.status_badge.configure(text="✅ Completed",
                                             text_color=COLORS["success"])
        else:
            self._set_console(message, color="#ffaaaa")

    def _show_completion_dialog(self, ex):
        """Show a congratulations popup when exercise is completed."""
        num = ex["number"]
        dialog = ctk.CTkToplevel(self)
        dialog.title("Exercise Complete!")
        dialog.geometry("400x260")
        dialog.transient(self)
        dialog.wait_visibility()
        dialog.grab_set()
        dialog.configure(fg_color=COLORS["bg_panel"])

        ctk.CTkLabel(dialog, text="🎉", font=("", 40)).pack(pady=(24, 8))
        ctk.CTkLabel(dialog, text=f"Exercise #{num} Complete!",
                     font=FONTS["title"], text_color=COLORS["success"]).pack()
        ctk.CTkLabel(dialog, text=f"{ex['title']}",
                     font=FONTS["body"], text_color=COLORS["text_muted"]).pack(pady=4)

        if num < 42:
            ctk.CTkLabel(dialog, text=f"Exercise #{num + 1} is now unlocked!",
                         font=FONTS["small"], text_color=COLORS["accent"]).pack(pady=8)
            ctk.CTkButton(dialog, text="Next Exercise →",
                          fg_color=COLORS["accent"],
                          command=lambda: (dialog.destroy(), self._next_exercise())).pack(pady=8)
        else:
            ctk.CTkLabel(dialog, text="You've completed ALL 42 exercises! 🏆",
                         font=FONTS["body"], text_color=COLORS["success"]).pack(pady=8)
            ctk.CTkButton(dialog, text="Amazing! 🎊",
                          fg_color=COLORS["success"],
                          command=dialog.destroy).pack(pady=8)

        self.status_badge.configure(text="✅ Completed", text_color=COLORS["success"])
        self._update_sidebar_buttons()

    # ── Helper Methods ────────────────────────────────────────────────────────

    def _set_text(self, widget, text):
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", text)
        widget.configure(state="disabled")

    def _set_console(self, text, color=None):
        self.console_output.configure(state="normal")
        self.console_output.delete("1.0", "end")
        self.console_output.configure(
            text_color=color or COLORS["text"])
        self.console_output.insert("1.0", text)
        self.console_output.configure(state="disabled")

    def _set_status(self, msg):
        self.status_msg.configure(text=msg)

    def _handle_tab(self, event):
        """Insert 4 spaces instead of a tab."""
        self.code_editor.insert(tk.INSERT, "    ")
        return "break"

    def _clear_code(self):
        self.code_editor.delete("1.0", "end")
        ex = EXERCISES[self.current_exercise_index]
        self.code_editor.insert("1.0",
            f"# Exercise #{ex['number']}: {ex['title']}\n"
            f"# Prerequisites: {ex['prerequisites']}\n\n")
        self.highlighter._highlight()

    def _show_hint(self):
        ex = EXERCISES[self.current_exercise_index]
        num = ex["number"]
        solution = SOLUTIONS.get(num, "No solution available.")

        # Show only a partial hint (first few lines)
        lines = solution.strip().split("\n")
        hint_lines = lines[:min(5, len(lines))]
        hint = "\n".join(hint_lines) + "\n# ... (try to complete it yourself!)"

        dialog = ctk.CTkToplevel(self)
        dialog.title(f"Hint — Exercise #{num}")
        dialog.geometry("600x280")
        dialog.transient(self)
        dialog.wait_visibility()
        dialog.grab_set()
        dialog.configure(fg_color=COLORS["bg_panel"])

        ctk.CTkLabel(dialog, text=f"💡 Hint for Exercise #{num}: {ex['title']}",
                     font=FONTS["heading"], text_color=COLORS["warning"]).pack(
            anchor="w", padx=16, pady=(16, 8))

        hint_box = ctk.CTkTextbox(dialog, font=FONTS["mono_sm"],
                                   fg_color=COLORS["code_bg"],
                                   text_color=("#92400e", "#ffe08a"),
                                   state="normal")
        hint_box.pack(fill="both", expand=True, padx=12, pady=(0, 8))
        hint_box.insert("1.0", hint)
        hint_box.configure(state="disabled")

        ctk.CTkButton(dialog, text="Close", command=dialog.destroy,
                      fg_color=COLORS["bg_card"]).pack(pady=(0, 12))

    def _show_solution(self):
        ex = EXERCISES[self.current_exercise_index]
        num = ex["number"]

        # Only show solution if exercise is completed
        if num not in self.progress["completed"]:
            messagebox.showinfo(
                "Solution Locked",
                f"Complete Exercise #{num} first to unlock the reference solution!\n\n"
                "Try submitting your answer with the \u2713 Submit button.")
            return

        reference = SOLUTIONS.get(num, "# No reference solution available.")
        user_code = load_user_solution(num) or "# No saved solution found."

        dialog = ctk.CTkToplevel(self)
        dialog.title(f"Solution Comparison — Exercise #{num}: {ex['title']}")
        dialog.geometry("1150x560")
        dialog.transient(self)
        dialog.configure(fg_color=COLORS["bg_panel"])
        dialog.wait_visibility()
        dialog.grab_set()

        # Header row
        header = ctk.CTkFrame(dialog, fg_color="transparent")
        header.pack(fill="x", padx=16, pady=(14, 6))
        ctk.CTkLabel(
            header,
            text=f"🔑 Exercise #{num} — {ex['title']}  │  Compare your solution with the reference",
            font=FONTS["heading"], text_color=COLORS["success"]
        ).pack(side="left")

        # Two-pane body
        body = ctk.CTkFrame(dialog, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=12, pady=(0, 8))
        body.grid_columnconfigure(0, weight=1)
        body.grid_columnconfigure(1, weight=1)
        body.grid_rowconfigure(1, weight=1)

        # Left pane — user's solution
        ctk.CTkLabel(
            body,
            text="📝  Your Saved Solution",
            font=FONTS["small"], text_color=COLORS["accent"]
        ).grid(row=0, column=0, sticky="w", padx=(4, 8), pady=(0, 4))

        user_box = ctk.CTkTextbox(
            body, font=FONTS["mono_sm"],
            fg_color=COLORS["code_bg"], text_color=("#1e293b", "#e8eaf6"),
            border_color=COLORS["accent"], border_width=1,
            corner_radius=6
        )
        user_box.grid(row=1, column=0, padx=(4, 6), pady=0, sticky="nsew")
        user_box.insert("1.0", user_code)
        user_box.configure(state="disabled")

        # Right pane — reference solution
        ctk.CTkLabel(
            body,
            text="🕑  Reference Solution (Al Sweigart)",
            font=FONTS["small"], text_color=COLORS["success"]
        ).grid(row=0, column=1, sticky="w", padx=(8, 4), pady=(0, 4))

        ref_box = ctk.CTkTextbox(
            body, font=FONTS["mono_sm"],
            fg_color=COLORS["code_bg"], text_color=("#1e40af", "#a8e6cf"),
            border_color=COLORS["success"], border_width=1,
            corner_radius=6
        )
        ref_box.grid(row=1, column=1, padx=(6, 4), pady=0, sticky="nsew")
        ref_box.insert("1.0", reference)
        ref_box.configure(state="disabled")

        # Close button
        ctk.CTkButton(
            dialog, text="Close", command=dialog.destroy,
            fg_color=COLORS["bg_card"], width=100
        ).pack(pady=(0, 14))

    def _on_exercise_click(self, index):
        ex = EXERCISES[index]
        num = ex["number"]
        if num in self.progress["completed"] or num in self.progress["unlocked"]:
            # Save current code first
            current_ex = EXERCISES[self.current_exercise_index]
            current_code = self.code_editor.get("1.0", "end").strip()
            if current_code:
                save_user_solution(current_ex["number"], current_code)
            self._load_exercise(index)
        else:
            messagebox.showinfo("Locked",
                f"Complete the previous exercise to unlock Exercise #{num}!")

    def _prev_exercise(self):
        if self.current_exercise_index > 0:
            self._save_current_code()
            self._load_exercise(self.current_exercise_index - 1)

    def _next_exercise(self):
        if self.current_exercise_index < len(EXERCISES) - 1:
            self._save_current_code()
            next_index = self.current_exercise_index + 1
            next_num = EXERCISES[next_index]["number"]
            if next_num in self.progress["completed"] or next_num in self.progress["unlocked"]:
                self._load_exercise(next_index)
            else:
                messagebox.showinfo("Locked",
                    f"Complete Exercise #{EXERCISES[self.current_exercise_index]['number']} first!")

    def _save_current_code(self):
        ex = EXERCISES[self.current_exercise_index]
        code = self.code_editor.get("1.0", "end").strip()
        if code:
            save_user_solution(ex["number"], code)

    def _on_close(self):
        """Save the current editor code before closing the app."""
        self._save_current_code()
        save_progress(self.progress)
        self.destroy()

    def _set_theme(self, theme: str):
        """Switch between Light, Dark, and System appearance modes."""
        ctk.set_appearance_mode(theme)
        self.progress["theme"] = theme
        save_progress(self.progress)
        self.highlighter.update_theme()

    def _reset_progress(self):
        if messagebox.askyesno("Reset Progress",
                                "Reset all progress? Your saved solutions won't be deleted."):
            self.progress = {"completed": [], "unlocked": [1], "current": 1}
            save_progress(self.progress)
            self.current_exercise_index = 0
            self._load_exercise(0)
            self._update_sidebar_buttons()


if __name__ == "__main__":
    app = ExerciseApp()
    app.mainloop()
