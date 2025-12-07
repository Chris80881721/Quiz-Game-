# Quiz Game

Simple command-line quiz game written in Python. The game asks four hardware-related questions (CPU, GPU, RAM, PSU) and keeps score of correct answers.

## How to run

1. Make sure you have Python 3 installed.
2. Open PowerShell and change to the project folder:

```
Set-Location -Path 'C:\Users\cpk36\OneDrive\Documents\Quiz_Code_Game'
```

3. Run the script:

```
&C:/Users/cpk36/AppData/Local/Python/pythoncore-3.14-64/python.exe Quiz_Game.py
```

Or if `python` is on your PATH:

```
python Quiz_Game.py
```

## How it works

- The script prompts: `Do you want to play my game?` — type `yes` (any capitalization is accepted, e.g. `Yes`, `YES`).
- It then asks four questions. For each question the program accepts either the abbreviation (e.g. `CPU`) or the full phrase (e.g. `central processing unit`) in any mix of uppercase/lowercase.
- A running `score` variable tracks the number of correct answers and is displayed at the end.

## Accepted answers (examples)

- CPU: `cpu` or `central processing unit`
- GPU: `gpu` or `graphics processing unit`
- RAM: `ram` or `random access memory`
- PSU: `psu` or `power supply unit`

Note: The program compares answers case-insensitively but expects either the common abbreviation or the full phrase.

## Tips

- If you want to accept single-letter confirmations like `y`, the input check must be adjusted (currently it expects the full word `yes`).
- Add a `.gitignore` before committing to avoid pushing virtual environment files or secrets.

## License

This is a small learning project — use and modify it freely.
