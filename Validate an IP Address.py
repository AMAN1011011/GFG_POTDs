no = []
        i = 0
        n = len(str)
        while i < n:
            st = ''
            while i < n and str[i] != '.':
                st += str[i]
                i += 1
            no.append(st)
            i += 1
        
        if len(no) != 4:
            return False
        
        for it in no:
            if len(it) > 3 or len(it) == 0:
                return False
            
            octal = 0
            for its in it:
                octal = octal * 10 + (ord(its) - ord('0'))
            
            if octal < 0 or octal > 255:
                return False
            
            if (octal >= 0 and octal <= 9 and len(it) > 1) or \
               (octal >= 10 and octal <= 99 and len(it) > 2):
                return False
        
        return True