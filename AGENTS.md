### Prompt for Codex (Python)

Write a complete, self-contained Python 3 program that implements a desktop GUI Password Generator using Tkinter.

**Functional requirements**
1. The window title should be “Secure Password Generator”.
2. Layout:
   • A label asking “Password length:” next to a Spinbox (minimum = 6, maximum = 64, default = 12).  
   • Four Checkbuttons to include/exclude character sets:  
     – “Uppercase A-Z” (checked by default)  
     – “Lowercase a-z” (checked by default)  
     – “Digits 0-9” (checked by default)  
     – “Symbols !@#$…​” (checked by default)  
   • A “Generate” Button.  
   • A readonly Entry field that displays the newly generated password.  
   • A “Copy to clipboard” Button that copies the current password to the system clipboard and shows a short confirmation (e.g., a pop-up or temporary status label).

3. If the user unchecks **every** character-set box, disable the Generate button and display an error message until at least one box is re-checked.

4. Password generation must be cryptographically secure: use `secrets.choice` over a combined character pool built from the selected character sets.

5. The GUI window must be resizable, with sensible padding, and widgets should expand/anchor gracefully.

**Code style & delivery requirements**
- Provide **the entire code**, from `import` statements to the `if __name__ == "__main__":` guard, with no omissions, truncations, or placeholders.  
- Include clear inline comments in English explaining each logical section.  
- Follow PEP 8 where practical (line length ≤ 88).  
- Avoid global variables except `CHAR_SETS` constants; encapsulate the app in a class named `PasswordGeneratorApp`.  
- Do not rely on external libraries beyond Python’s standard library.

Return only the Python code block—no extra explanation or markdown.
password_generator_gui.py
packages.txt 
add a lot of colors
