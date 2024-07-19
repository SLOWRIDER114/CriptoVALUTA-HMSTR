ma = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
mb = ma.upper()
me = 'abcdefghijklmnopqrstuvwxyz'
mem = me.upper()

class Vigener:
    def encrypt(s, k, alf='ru'):
        w = 0
        if alf == 'ru':
            ky = [ma.index(i.lower()) for i in ''.join(k.split())]
            ans = ''
            for i in range(len(s)):
                j = ky[w % len(ky)]
                if s[i] in ma:
                    ans += ma[(ma.index(s[i]) + j) % 33]
                    w += 1
                elif s[i] in mb:
                    ans += mb[(mb.index(s[i]) + j) % 33]
                    w += 1
                else:
                    ans += str(s[i])
        else:
            ky = [me.index(i.lower()) for i in ''.join(k.split())]
            ans = ''
            for i in range(len(s)):
                j = ky[w % len(ky)]
                if s[i] in me:
                    ans += me[(me.index(s[i]) + j) % 26]
                    w += 1
                elif s[i] in mem:
                    ans += mem[(mem.index(s[i]) + j) % 26]
                    w += 1
                else:
                    ans += str(s[i])
        return ans


    def decrypt(s, k, alf):
        w = 0
        if alf == 'ru':
            ky = [ma.index(i.lower()) for i in ''.join(k.split())]
            ans = ''
            for i in range(len(s)):
                j = ky[w % len(ky)]
                if s[i] in ma:
                    ans += ma[(ma.index(s[i]) - j) % 33]
                    w += 1
                elif s[i] in mb:
                    ans += mb[(mb.index(s[i]) - j) % 33]
                    w += 1
                else:
                    ans += str(s[i])
        else:
            ky = [me.index(i.lower()) for i in ''.join(k.split())]
            ans = ''
            for i in range(len(s)):
                j = ky[w % len(ky)]
                if s[i] in me:
                    ans += me[(me.index(s[i]) - j) % 26]
                    w += 1
                elif s[i] in mem:
                    ans += mem[(mem.index(s[i]) - j) % 26]
                    w += 1
                else:
                    ans += str(s[i])
        return ans

