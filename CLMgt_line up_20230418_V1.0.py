@app.route('/yourxinxi',methods=['post'])
@cross_origin()
def Yourxinxi():
    chepaihao = session.get('chepaihao')
    cheweihao=getcheweihao(chepaihao)
    name=foundname(chepaihao)
    cheweihao=str(cheweihao)
    chepaihao=str(chepaihao)
    name=str(name)
    re=cheweihao+'&'+chepaihao+'&'+name
    return re
def getcheweihao(n):
    n=str(n)
    try:
        sel='select cheweihao from tingche where chepaihao=%s order by id desc;'
        cur.execute(sel,n)
        w=cur.fetchone()
        return w[0]
    except Exception :
        return "error"
    finally:
        conn.commit()
def foundname(n):
    n=str(n)
    try:
        sel='select xingming from user where chepai=%s;'
        cur.execute(sel,n)
        w=cur.fetchone()
        return w[0]
    except Exception :
        return "error"
    finally:
        conn.commit()


# #用户登出时需要进行三部分操作：1、已用车位重新可用2、用户表中删除该用户
# # 3、记录表中将停车记录改为已退出
@app.route('/dropme',methods=['POST'])
@cross_origin()
def Dropme():
    chepaihao = session.get('chepaihao')
    cheweihao = Foundchewei(chepaihao)
    cheweihao=str(cheweihao)
    chepaihao=str(chepaihao)
    Rechewei(cheweihao)
    Rejilu(chepaihao)
    try:
        dele = "delete from user where chepai=%s"
        cur.execute(dele, chepaihao)
        return "已退出"+render_template('/stop.html')
    except Exception :
        return "error"
    finally:
        conn.commit()


#管理员登录，这里管理员唯一
@app.route('/logguanli',methods=['POST'])
@cross_origin()
def Logguanli():
    zhanghao=request.form['zhanghao']
    pwd=request.form['pwd']
    if zhanghao=="unname":
        if pwd=="unpwd":
             return redirect('/forward?addr=guanli.html')
        else:
            return "密码错误！"+render_template('log.html')
    else:
        return "账号错误！"+render_template('log.html')


#获取所有车位信息
@app.route('/allcheweizhanshi',methods=['post'])
@cross_origin()
def Allcheweizhanshi():
    try:
        sel = "select * from chewei;"
        cura = conn.cursor()
        cura.execute(sel)
        w = cura.fetchall()
        re = ''
        for i in w:
            for j in i:
                re += str(j) + '&'
            re = re[:-1]
            re += '|'
        re = re[:-1]
        return re
    except Exception :
        return "error"
    finally:
        cura.close()

#删除车位
#删除时，会检查是否该车位还在使用，若使用则提示，否则直接删除
@app.route('/deletechewei',methods=['POST'])
@cross_origin()
def Deletechewei():
    rd = request.data
    rd = str(rd)
    t = ''
    for i in rd:
        if i >= '0' and i <= '9':
            t += i
    t = str(t)
    u=ifdel(t)
    if u == "已使用":
        return redirect('/forward?addr=guanli.html')
    try:
        dele = "delete from chewei where cheweihao=%s"
        cur.execute(dele, t)
        return redirect('/forward?addr=guanli.html')
    except Exception :
        return "error"
    finally:
        conn.commit()
def ifdel(n):
    n=str(n)
    try:
        sel='select qingkuang from chewei where cheweihao=%s;'
        cur.execute(sel,n)
        w=cur.fetchone()
        return w[0]
    except Exception :
        return "error"
    finally:
        conn.commit()
