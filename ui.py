import streamlit as st
import mysql.connector as mycon
db= mycon.connect(
    host ='localhost', user= 'root', password= 'root' ,database='pydb'
)
db_curr = db.cursor()

#GUI
st.title('CURD operations')
tab1, tab2, tab3, = st.tabs(['insert','update','delete'])
with tab1:
    no = st.number_input('enter product no:')
    name = st.text_input('enter product name:')
    loc = st.text_input('enter product location:')


    if st.button('submit'):
        sql ="insert into dmart(pro_no,pro_name,pro_loc)values (%s,%s,%s)"
        val = (no,name,loc)
        db_curr.execute(sql,val)
        db.commit()
        db_curr.execute('select* from dmart')
        st.table(db_curr.fetchall())


with tab2:
    no = st.number_input('no:')
    name = st.text_input('name:')
    loc = st.text_input('location:')


    if st.button('update'):
        sql ="update dmart set pro_no = %s, pro_name = %s where pro_loc =%s"
        val = (no,name,loc)
        db_curr.execute(sql,val)
        db.commit()
        db_curr.execute('select* from dmart')
        st.table(db_curr.fetchall())

with tab3:
    db_curr.execute('select* from dmart')
    st.table(db_curr.fetchall())
    no = st.text_input('product No which you want to delete: ')
    if st.button('delete'):
        sql = "delete from dmart where pro_no =%s"
        val =(no,)
        db_curr.execute(sql,val)
        db.commit()
        st.success("data deleted successfully")
db_curr.execute('select * from dmart')
data = db_curr.fetchall()
st.table(data)  
