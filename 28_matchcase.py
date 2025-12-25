# Match-case - It is an alternative for the elif statement
# it is clear and easier to read 


def holiday(day):
    match day:
        case "Saturday":
            return "It is holiday"
        case "Sunday"|"Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
            return "It is not holiday. "

print(holiday("Sunday"))