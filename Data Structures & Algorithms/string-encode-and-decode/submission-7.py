class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for s in strs:
            out += f'{len(s)}#{s}'
        
        out = "".join(out)
        return out


    def decode(self, s: str) -> List[str]:
        length = -1
        word = []
        out = []
        for c in s:
            # if we're currently decoding a word
            if length >= 0:
                word += c
                length -= 1

                if length == -1:
                    out.append("".join(word))
                    word = []

                continue

            # read until hashtag
            if c != '#':
                word += c

            # compute length and read that many
            else:
                length = int("".join(word)) - 1

                word = []

                # edge case word is empty str
                if length == -1:
                    out.append("")

        return out
