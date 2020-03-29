class jiema:
    def getOneStepString(self,m):#将子码转换为人能看懂的String类型
        b='\u0072\u006e\u0042\u0062\u0041\u0061\u004b\u006b\u0063\u3000\u3000\u3000\u3000\u3000\u3000\u3000\u0050\u0070\u4e00\u0031\u4e8c\u0032\u4e09\u0033\u56db\u0034\u4e94\u0035\u516d\u0036\u4e03\u0037\u516b\u0038\u4e5d\u0039\u0071\u007a\u0068\u006a\u0074\u005a';
        s = ""
        for i in str(m):
            s += b[ord(i)-49]
        return s

    def getText(self,s,p,b):#将一行的密码转换为字码
        I = ''
        t=' UW| UVW| UEGW| UEGIW||| WU| WVU| WGEU| WIGEU'.split('|')
        r='CDEFGHIJKLMNOPQRST'
        f='12357532199AAAAA12468642199BBBBB'
        #密码
        fc = int(s[0])
        fr = int(s[1])
        tc = int(s[2])
        tr = int(s[3])
        fp = f[int(p[int(s[:2])])]
        if b==0:
            m=fp+r[(8-fc)*2]
            if fp=='1'or fp=='2' or fp=='9' or fp=='A':
                for i in range(10):
                    tp = int(p[fc*10+i])
                    if tp<16 and f[tp]==fp:
                        I+=str(i)
                if len(I)>=3:
                    m=t[len(I)+3][I[fr]]
                    if len(I)<=4 and fp=='A':
                        p="_".join(p)+'_'
                        s_cont = [str(i)+'_'for i in range(11,16)]
                        t_cont = ''
                        for i_cont in s_cont:
                            this_str = str(int(p.index(i_cont)/3))
                            if len(this_str)==2:
                                t_cont+=this_str[0]
                            else:
                                t_cont+='0'
                        if re.match(r"(\d).*\1",t_cont)==None:
                            m=r[16-fc*2]
                        else:
                            m=fp
                    else:
                        m+=fp
            if fr==tr:
                m+='Z'+r[(8-tc)*2]
            elif fr>tr:
                m+='X'
                if fp.isdigit() and int(fp)>1 and int(fp)<7:
                    m+=r[(8-tc)*2]
                else:
                    m+=r[(fr-tr-1)*2+b]
            else:
                m+='Y'
                if fp.isdigit() and int(fp)>1 and int(fp)<7:
                    m+=r[(8-tc)*2]
                else:
                    m+=r[(tr-fr-1)*2+b]
        else:
            m=fp + r[fc*2+b]
            if fp=='1' or fp=='2' or fp=='9' or fp=='B':
                for i in range(10):
                    tp = int(p[fc*10+i])
                    if tp>15 and tp<32 and f[tp]==fp:
                        I+=str(i)
                if len(I)>=3:
                    m=t[len(I)+3][I[fr]]
                    if len(I)<=4 and fp=='B':
                        p="_".join(p)+'_'
                        s_cont = [str(i)+'_'for i in range(27,32)]
                        t_cont = ''
                        for i_cont in s_cont:
                            this_str = str(int(p.index(i_cont)/3))
                            if len(this_str)==2:
                                t_cont+=this_str[0]
                            else:
                                t_cont+='0'
                        if re.match(r"(\d).*\1",t_cont)==None:
                            m=r[fc*2+1]
                        else:
                            m=fp
                    else:
                        m+=fp
            if fr==tr:
                m+='Z'+r[tc*2+b]
            elif fr>tr:
                m+='Y'
                if fp.isdigit() and int(fp)>1 and int(fp)<7:
                    m+=r[tc*2+b]
                else:
                    m+=r[(fr-tr-1)*2+b]
            else:
                m+='X'
                if fp.isdigit() and int(fp)>1 and int(fp)<7:
                    m+=r[tc*2+b]
                else:
                    m+=r[(tr-fr-1)*2+b]    
        return m
    
    def getMoveListString(self,m0,p0):
        p=[99 for i in range(100)]
        if p0 == '':
            p0='8979695949392919097717866646260600102030405060708012720323436383'
        p0=[p0[i*2:i*2+2] for i in range(int(len(p0)/2))]
        for i in range(32):
            p[int(p0[i])]=str(100+i)[1:]
        m=[m0[i*4:i*4+4] for i in range(int(len(m0)/4))]
        ms=[]
        for index,(mi) in enumerate(m):
            t=int(p[int(mi[:2])])
            if t>=0 and t<=15:
                ms.append([self.getOneStepString(self.getText(mi,p,0)),0])
            elif t>=16 and t<=31:
                ms.append([self.getOneStepString(self.getText(mi,p,1)),1])
            else:
                ms.append(['\u7740\u6CD5\u9519\u8BEF'])
                continue
            p[int(mi[2:])]=p[int(mi[:2])]
            p[int(mi[:2])]='99'
        return ms