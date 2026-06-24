import streamlit as st
import time
import math

def triangle_perimeter(a,b,c):
    return a+b+c

def triangle_area(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    return area

def square_perimeter(side):
    return 4*side

def square_area(side):
    return side**2

def rectangle_perimeter(l,b):
    return 2*(l+b)

def rectangle_area(l,b):
    return l+b

def circle_perimeter(r):
    return 2*(22/7)*(r**2)
def circle_area(r):
    return math.pi *r*r

# 3d objects

def cone_tsa(r,h):
    return((22/7)*r*(r+1))

def cone_vol(r, h):
    return (1/3) * (22/7) * (r**2) * ((1**2)-(r**2)) ** (1/2)

def cube_tsa(s):
    return s**3

def cube_vol(s):
    return s**3



def cuboid_tsa(l,b,h):
    return 2*(1*b+b*h+h*1)

def cuboid_vol(l,b,h):
    return l*b*h

def sphere_tsa(r):
    return 4*(22/7)*(r**2)

def sphere_vol(r):
    return (4/3)*(22/7)*(r**3)


def cylinder_tsa(r,h):
    return 2*(22/7)*r*(h+r)

def cylinder_vol(r,h):
    return (22/7)*(r**2)*h


st.title('Geometry calculator')

st.header('2D shapes')

st.subheader('Triangle')

col1,col2 = st.columns([1,3])

with col1:
    a = st.number_input('side1:',key='tri_a')
    b = st.number_input('side2:',key='tri_b')
    c = st.number_input('side3:',key='tri_c')

cola,colb = st.columns(2)

with cola:
    st.metric('perimeter',triangle_perimeter(a,b,c))

with colb:
    st.metric('Area',round(triangle_area(a,b,c),2))


############################################### square
st.divider()

st.subheader('Square')

col1s,col2s = st.columns([1,3])


with col1s:
   s = st.number_input('side:',key='sq_s')

colas,colbs = st.columns(2)


with colas:
    st.metric('permeter',square_perimeter(s))

with colbs:
    st.metric('Area',round(square_area(s),2))

    
####################################################rectangle

st.divider()

st.subheader('Rectangle')

col1s,col2s = st.columns([1,3])

with col1s:
    l = st.number_input('length: ',key='rect_l')
    b = st.number_input('breadth:',key='rect_b')



colas,colbs = st.columns(2)


with colas:
    st.metric('permeter',rectangle_perimeter(l,b))

with colbs:
    st.metric('Area',round(rectangle_area(l,b)))

###################################################circle

st.divider()

st.subheader('Circle')

col1c,col2c = st.columns([1,3])

with col1c:
    r = st.number_input('Radius:',key='cir_r')


with col1c:
   s = st.number_input('permeter',round(circle_perimeter(c),2))

colac,colbc = st.columns(2)


with colac:
    st.metric('permeter',round(circle_perimeter(c)))

with colbc:
    st.metric('Area',round(circle_area(c),2))

    
#####################################################

st.divider()
st.divider()

st.header('3D objects')

st.subheader('Cone')

col1aco,col2aco = st.columns([1,3])

with col1aco:
    r_cone = st.number_input('Radius:')
    h_cone = st.number_input('leteral side length:')


colaco,colbaco = st.columns(2)

with colaco:
    st.metric('Total surface area',cone_tsa(r_cone,h_cone))


with colbaco:
    st.metric('Volume',cone_vol(r_cone,h_cone))

#######################################cube

st.divider()

st.subheader('Cube')

col1cu,col2cu = st.columns([1,3])


with col1cu:
   s_cube = st.number_input('side:',key='cube_s')

cola_cu,colb_cu = st.columns(2)


with cola_cu:
    st.metric('Total Surface Area',cube_tsa(s_cube))

with colb_cu:
    st.metric('Volume',cube_vol(s_cube))
   

########################################cuboid
st.divider()

st.subheader('Cuboid')

col1s,col2s = st.columns([1,3])

with col1s:
    l = st.number_input('length: ',key='cuboid_l')
    b = st.number_input('breadth:',key='cuboid_b')
    h = st.number_input('height:',key='cuboid_h')



cola_boid,colb_boid = st.columns(2)


with cola_boid:
    st.metric('Total surface area',cuboid_tsa(l,b,h))

with colb_boid:
    st.metric('Volume',cuboid_vol(l,b,h))

####################################speare

st.divider()

st.subheader('Sphere')

col1_sp,col2_sp = st.columns([1,3])

with col1_sp:
    r_sphere= st.number_input('Radius:',key='sphere_r')



cola_sp,colb_sp = st.columns(2)


with cola_sp:
    st.metric('Total Surface Area',round((sphere_tsa(r_sphere)),2))

with colb_sp:
    st.metric('volume',round(circle_area(r_sphere),2))

#############################################cylnder
st.divider()

st.subheader('Cylinder')

col1cy,col2cy = st.columns([1,3])

with col1cy:
    r_cyl = st.number_input('length: ',key='r_cyl')
    h_cyl = st.number_input('breadth:',key='h_cyl')
    



cola_cyl,colb_cyl = st.columns(2)


with cola_cyl:
    st.metric('Total surface area',cylinder_tsa(r_cyl,h_cyl))

with colb_cyl:
    st.metric('Volume',cylinder_vol(r_cyl,h_cyl))










