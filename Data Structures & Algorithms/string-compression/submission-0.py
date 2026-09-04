class Solution:
    def compress(self, chars: List[str]) -> int:
        # 2 Pointer chars -> read_ptr go thru char and count letters
        # write_ptr will write the letter and count to array
        # for the rest of len(chars) after write_ptr, popright()

        if len(chars) <= 1:
            return len(chars)

        read = 0
        write = 0

        curr = chars[0]
        count = 0
        for c in chars:
            if c == curr:
                count += 1
            else:
                chars[write] = curr
                write += 1
                if count > 1:
                    for ch in str(count):
                        chars[write] = ch
                        write += 1
                curr = c
                count = 1
        
        chars[write] = curr
        write += 1
        if count > 1:
            for ch in str(count):
                chars[write] = ch
                write += 1

        print("pre chars: ", chars)
        
        for i in range(len(chars) - write):
            chars.pop()
        
        print("chars: ", chars)

        return len(chars)