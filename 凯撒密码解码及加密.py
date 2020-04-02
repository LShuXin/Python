def kaisamima():
    mark=input("您想加密还是解密？（加密请输入1，解密请输入0；并按回车。）")
    def process(mark):
        if mark=='1' or mark=='0':
                if mark=='1':
                        secret=input("请输入名文，并按回车结束...")
                        if secret:
                            for word in secret:
                                if ord('a')<=ord(word)<=ord('z'):
                                    print(chr(ord('a')+(ord(word)-ord('a')+3)%26))
                                else:
                                    print(chr(ord('A')+(ord(word)-ord('A')+3)%26))
                            kaisamima()
                        else:
                            mark = input("您未输入任何字符，请重新加密解密（加密请输入1，解密请输入0，并按回车）。")
                            process(mark)
                else:
                        mingwen = input("请输入密文，并按回车结束...")
                        if mingwen:
                            for word in mingwen:
                                if ord('a') <= ord(word) <= ord('z'):
                                    print(chr(ord('a') + (ord(word) - ord('a') - 3) % 26))
                                else:
                                    print(chr(ord('A') + (ord(word) - ord('A') -3) % 26))
                            kaisamima()
                        else:
                            mark = input("您未输入任何字符，请重新加密解密（加密请输入1，解密请输入0，并按回车）。")
                            process(mark)
        else:
            mark=input("您的输入未按照规定格式，请重新选择解密还是加密（加密输入1，解密输入0，并按回车）。")
            process(mark)
    process(mark)
kaisamima()
