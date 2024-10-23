import json
import csv
from datetime import datetime



def menu():
            print("""
        ===========================================
        ============ Menu inventario ==============
        =                                         =
        =   1. Registrar trabajador               =
        =   2. Ingresar Inasistencias             =
        =   3. Ingresar Bonos extra-legales       =
        =   4. Calcular Nomina                    =
        =   5. Salir                              =
        =                                         =
        ===========================================
             """)
            
#______________________________________________________________________________________________________________________________________
def creacion():
  
  trabajador={
    "cc": int(input("ingrece documento: ")),
    "nombre": input("indique nombre del colaborador: "),
    "cargo": input("indique el cargo: "),
    "salario": int(input("salario que debenga: ")),
  }

  usuario = None
  try:  # se crea un try
    file = open('nomina.json', 'r')  
    usuario = json.load(file)   
    file.close        
  except Exception as error:  
       usuario = []   
  usuario.append(trabajador) 
  file = open('nomina.json', 'w')
  json.dump(usuario,file,indent=4) 
  file.close
#______________________________________________________________________________________________________________________________________

def inasistencias():

  descuento= None
  try:
    file = open('nomina.json', 'r') 
    descuento = json.load(file) 
    file.close
  except Exception as erro:
      descuento = []
  cc = int(input("ingrece la cecula del trabajador: "))
  for faltas in descuento:
        if faltas['cc'] == cc:
            # Calcular el descuento por faltas de forma más flexible
            descuento_por_falta = 33333  
            num_faltas = int(input("Ingrese número de faltas: "))
            total_descuento = num_faltas * descuento_por_falta

            # Agregar la información de inasistencias al empleado
            if 'inasistencias' not in faltas:
                faltas['inasistencias'] = []
                faltas['inasistencias']={
                'num_faltas': num_faltas,
                'total_descuento': total_descuento,
                'fecha': datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            }
  descuento.append(faltas)
  file = open('calculo_nomina.json', 'a')
  json.dump(faltas,file,indent=4)
  file.close
#______________________________________________________________________________________________________________________________________

def bonos():
  try:
      
    file = open('nomina.json', 'r+') # se abre el archivo json en modo lectura
    money = json.load(file) 
    file.close
  except Exception as erro:
      money = []
  cc = int(input("ingrece la cecula del trabajador: "))

  for extras in money:
    if extras["cc"] ==cc:
        valor_bono= int(input("Indique valor del bono: "))
        if 'bonos' not in extras:
            extras['bonos'] = []
            extras['bonos'].append({
                'bono': valor_bono,
                'concepto': input("concepto: "),
                'fecha': datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
            })

  money.append(extras)
  file = open('calculo_nomina.json', 'a')
  json.dump(extras,file,indent=4)
  file.close  
#______________________________________________________________________________________________________________________________________

def calculo_nomina():

  nomina_final=[]

  file = open('calculo_nomina.json', 'r') # se abre el archivo json en modo lectura
  empleados = json.load(file) 
  file.close
  
  cc = int(input("ingrece la cecula del trabajador: "))



  datos_reporte = []


  for empleado in empleados:
        if empleado['cc'] == cc:
            salario_base = empleado['salario']
            descuento_salud = salario_base * 0.04
            descuento_pension = salario_base * 0.04

            # Calcular total de inasistencias y bonos (ajusta según tu estructura de datos)
            total_inasistencias = sum(inasistencia['monto'] for inasistencia in empleado['inasistencias'])
            total_bonos = sum(bono['monto'] for bono in empleado['bonos'])

            if salario_base < 2000000:
                salario_base += 150000

            salario_final = salario_base - descuento_salud - descuento_pension - total_inasistencias + total_bonos
            empleado['salario_final'] = salario_final

            # Guardar los cambios en el archivo
            with open('calculo_nomina.json', 'w') as file:
                json.dump(empleados, file, indent=4)

            return salario_final

  print("Empleado no encontrado")
  return None


  cc = int(input("Ingrese la cédula del trabajador: "))
  resultado = calcular_nomina(cc)
  if resultado is not None:
        print("El salario final es:", resultado)

#______________________________________________________________________________________________________________________________________