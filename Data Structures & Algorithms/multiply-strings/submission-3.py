class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        strToInt = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }

        intToStr = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9"
        }
        
        def stringToInteger(num: str) -> int:
            result = 0
            i = len(num) - 1

            while i >= 0:
                result += strToInt[num[i]] * (10 ** (len(num) - 1 - i))
                i -= 1

            return result

        def integerToString(num: int) -> str:
            if not num:
                return "0"

            result = ""
            i = 1
            while num > 0:
                x = num % (10 ** i)
                num -= x
                x = x // (10 ** (i - 1))
                result = intToStr[x] + result
                i += 1

            return result

        product = stringToInteger(num1) * stringToInteger(num2)

        return integerToString(product)
