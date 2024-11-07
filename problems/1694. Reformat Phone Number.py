class Solution:
    def reformatNumber(self, number: str) -> str:
        num = number.replace("-", "").replace(" ", "")

        ans = []
        i = 0
        while i < len(num):
            reaming = len(num) - i

            if reaming > 4:
                ans.append(num[i:i+3])
                i += 3
            elif reaming == 4:
                ans.append(num[i:i+2])
                ans.append(num[i+2:i+4])
                break
            else:
                ans.append(num[i:i + reaming])
                break

        return "-".join(ans)