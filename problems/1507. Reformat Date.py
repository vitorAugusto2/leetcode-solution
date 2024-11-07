class Solution:
    def reformatDate(self, date: str) -> str:
        month = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05",
            "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10",
            "Nov": "11", "Dec": "12"
        }

        date_split = date.split()

        day = date_split[0][:-2]
        month_num = month[date_split[1]]
        year = date_split[2]

        return f"{year}-{month_num}-{day}"
