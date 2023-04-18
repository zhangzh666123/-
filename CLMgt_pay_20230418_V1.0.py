from cgitb import html
from flask import Flask,redirect,render_template,session
from flask_cors import*
from flask import request
import pymysql
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='tingche',#数据库名
    charset='utf8'
)
#游标
cur = conn.cursor()
Lock_=False
app=Flask(__name__)
app.config['SESSION_KEY']='123asd456zxc'
app.secret_key='123asd456zxc'



#用户需要输入车牌号和姓名才可进入
@app.route('/chezhu',methods=['post'])
@cross_origin()
def Chezhulog():
    chepaihao=request.form['chepaihao']
    name=request.form['name']
    chepaihao=str(chepaihao)
    name=str(name)
    f=[chepaihao,name]
    u=ifcunzai(chepaihao)#如果车主没退出就离开页面则重新进入时不需要选择车位
    session['chepaihao']=chepaihao
    z=('使用中',)
    if z in u:
        return redirect('/forward?addr=chosok.html')
    try:
        ins='insert into user values(%s,%s);'
        cur.execute(ins,f)
        return render_template('/wait.html')
    except Exception:
        return render_template('/wait.html')
    finally:
        conn.commit()
def ifcunzai(n):
    n=str(n)
    try:
        sel='select ifuse from tingche where chepaihao=%s;'
        cur.execute(sel,n)
        w=cur.fetchall()
        return w
    except Exception:
        return "error"
    finally:
        conn.commit()


#展示所有车位
@app.route('/getchewei',methods=['post'])
@cross_origin()
def Getchewei():
    try:
        sel = "select * from chewei;"
        cur.execute(sel)
        w = cur.fetchall()
        re = ''
        for i in w:
            for j in i:
                re += str(j) + '&'
            re = re[:-1]
            re += '|'
        re = re[:-1]
        return re
    except Exception:
        return "error"
    finally:
        conn.commit()


#当车主选择车位时进行反馈
@app.route('/updme',methods=['post'])
@cross_origin()
def Updme():
    rd = request.data
    rd = str(rd)
    t = ''
    for i in rd:
        if i >= '0' and i <= '9':
            t += i
    t = str(t)#获取到的车位号
    ll=panduan(t)
    z="已使用"
    p="问题处理中"
    if z == ll:
        return "该车位已使用" + render_template('/wait.html')
    if p == ll:
        return "该车位存在问题" + render_template('/wait.html')
    jilu(t)#将本次停车记录保存到停车表中
    try:
        upd = 'update chewei set qingkuang="已使用" where cheweihao=%s'
        cur.execute(upd, t)
        return redirect('/forward?addr=chosok.html')
    except Exception:
        return "error"
    finally:
        conn.commit()
def panduan(n):#该车位必须没有被占，否则返回该界面
    n=str(n)
    try:
        sel='select qingkuang from chewei where cheweihao=%s'
        cur.execute(sel,n)
        w=cur.fetchone()
        return w[0]
    except Exception :
        return "error"
    finally:
        conn.commit()
def jilu(n):
    cheweihao=str(n)
    chepaihao=session['chepaihao']
    f=[chepaihao,cheweihao]
    try:
        ins='insert into tingche(chepaihao,cheweihao,ifuse) values(%s,%s,"使用中")'
        cur.execute(ins,f)
    except Exception :
        return "error"
    finally:
        conn.commit()
