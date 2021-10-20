
#TRIANGULO a=área p_t= perimetro
def p_triangulo():

  s_1 = int(input())
  s_2 = int(input())
  s_3 = int(input())
  suma=(s_1+s_2+s_3)
  print(suma)

def a_triangulo():
  b = int(input("Base" , ))
  a = int(input("Altura" , ))
  area = ((b*a)/2)
  print(area)

#CUADRILÁTEROS

def p_cuadrado():
  s = int(input())
  perimetro = (s*4)
  print(perimetro())

def a_cuadrado():
  a = int(input())
  area = (a*a)
  print(area())

def p_rectangulo():
  l = int(input())
  w = int(input())
  perimetro = ((l*2)+(w*2))
  print(perimetro())

def a_rectangulo():
  l = int(input())
  w = int(input())
  area = (l*w)
  print(area)

def p_trapecio():
  s = int(input())
  perimetro = (s*4)
  print(perimetro())

def a_trapecio():
  b_1 = int(input())
  b_2 = int(input())
  h = int(input())
  area = ((b_1+b_2)*h/2)
  print(area())

def a_trapezoide():
  b_d_1 = int(input())
  b_d_2 = int(input())
  h_1 = int(input())
  h_2 = int(input())
  suma_1 = ((b_d_1*h_1)/2)
  suma_2 = ((b_d_2*h_2)/2)
  area = (suma_1+suma_2)
  print(area())
