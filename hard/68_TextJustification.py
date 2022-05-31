def reflowLines(line_length, lines):
        ans = []
        index = 0
        lines = " ".join(lines).split()
        print(lines)
        while index < len(lines):
            print(index)
            tempSize = len(lines[index])
            currIndex = index

            # Adding words to current line along with a space till it exceeds limit
            while currIndex + 1 < len(lines) and tempSize + 1 + len(lines[currIndex + 1]) <= line_length:
                currIndex += 1
                tempSize += 1+len(lines[currIndex])
                print(currIndex, tempSize)
            
            # No of words added OR No of gaps where - can be added
            spaceBetween = currIndex - index
            if spaceBetween == 0:
                ans.append(lines[index])
                index += 1
                continue
            
            # Number of - in each gap
            midSpaceNum = (line_length-tempSize)//spaceBetween
            # Actual string of -'s common between each word of this line
            midSpaces = "-" * (1 + midSpaceNum)
            
            # For extra -'s
            extraSpaces = line_length - midSpaceNum*spaceBetween - tempSize
            print("extra", extraSpaces)
            inner = index
            # Appending an extra - to each word starting from the left
            while extraSpaces > 0:
                lines[inner] += "-"
                print(lines[inner])
                extraSpaces -= 1
                inner += 1
            
            ans.append(midSpaces.join(lines[index:currIndex+1]))
            index = currIndex + 1
            
        print("\n".join(ans)) 


reflowLines(13, ["What must be ack shall be"])