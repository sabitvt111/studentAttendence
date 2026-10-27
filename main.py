
# Colorful Student Attendance System

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

students = [
    "Kabir", "Adit", "Ahsan", "Taham", "Ayaan",
    "Navan", "Sabit", "Rafi", "Mayaam", "Sadik",
    "Farhan", "Akib", "Tamim", "Ayon", "Abdullah",
    "Jishan", "Al Jubayer", "Jubayer", "Junayed", "Asif", "Alif"
]

present = 0
absent = 0

# Header
print(CYAN + BOLD + "=" * 42)
print("       STUDENT ATTENDANCE SYSTEM")
print("=" * 42 + RESET)

print(YELLOW + f"\nTotal students to mark: {len(students)}")
print("-" * 42 + RESET)

# Attendance input
for number, name in enumerate(students, start=1):
    while True:
        status = input(
            f"{BLUE}[{number:02}/{len(students)}] "
            f"{WHITE}{name:<15} "
            f"{CYAN}(p/a): {RESET}"
        ).strip().lower()

        if status == "p":
            present += 1
            print(GREEN + "       ✓ PRESENT" + RESET)
            break

        elif status == "a":
            absent += 1
            print(RED + "       ✗ ABSENT" + RESET)
            break

        else:
            print(
                YELLOW + "       ! Enter only p or a."
                + RESET
            )

# Calculate statistics
total = len(students)
percentage = (present / total) * 100

# Progress bar
bar_length = 20
filled = round(present / total * bar_length)
bar = GREEN + "█" * filled + RED + "█" * (
    bar_length - filled
) + RESET

# Final summary
print("\n" + MAGENTA + BOLD + "=" * 42)
print("             ATTENDANCE REPORT")
print("=" * 42 + RESET)

print(f"\n{WHITE}Total Students   : {CYAN}{total}")
print(f"{GREEN}Present Students : {present}")
print(f"{RED}Absent Students  : {absent}")

print(f"\n{YELLOW}Attendance Rate  : {percentage:.1f}%")
print(f"{WHITE}Progress         : [{bar}]")

print("\n" + CYAN + "-" * 42)

if absent == 0:
    print(GREEN + BOLD + "Excellent! Everyone is present.")
elif present == 0:
    print(RED + BOLD + "Nobody is present today.")
else:
    print(YELLOW + BOLD + "Attendance recorded successfully.")

print(CYAN + "=" * 42 + RESET)
