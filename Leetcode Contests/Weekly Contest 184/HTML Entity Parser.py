class Solution:
    def entityParser(self, text: str) -> str:
        dct = {"&quot;": "\"",
               "&apos;": "'",
               "&amp;": "&",
               "&gt;": ">",
               "&lt;": "<",
               "&frasl;": "/"
               }

        for i in dct:
            text = text.replace(i, dct[i])

        return text
