from datetime import date
import calendar


def convert_date(date_for_convert: str) -> str:
    """This function should take a date string in the format dd/mm/yyyy and convert it to the format yyyy-mm-dd.
     If the input is not in the correct format, the function should return an error message "Error: Invalid date.
     the input should match the pattern: dd/mm/yyyy, where 01 ≤ dd ≤ 31, 01 ≤ mm ≤ 12, and 1900 ≤ yyyy ≤ 2100."""
    day = int(date_for_convert[:2])
    month = int(date_for_convert[3:5])
    year = int(date_for_convert[6:10])
    if len(date_for_convert) != 10:
        return "Error: Invalid date."
    if 1900 <= year <= 2100:
        if 1 <= month <= 12:
            _, last_day = calendar.monthrange(year, month)
            if 1 <= day <= last_day:
                return date(year, month, day).isoformat()
            else:
                return "Error: Invalid date."
        else:
            return "Error: Invalid date."
    else:
        return "Error: Invalid date."



print("Example:")
print(convert_date("01/01/2023"))

# These "asserts" are used for self-checking
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"
assert convert_date("10/10/2010") == "2010-10-10"
assert convert_date("31/05/1985") == "1985-05-31"
assert convert_date("07/08/1960") == "1960-08-07"
assert convert_date("02/09/1999") == "1999-09-02"
assert convert_date("30/04/1975") == "1975-04-30"
assert convert_date("29/02/2019") == "Error: Invalid date."
assert convert_date("30/04/1975/1") == "Error: Invalid date."

print("The mission is done! Click 'Check Solution' to earn rewards!")