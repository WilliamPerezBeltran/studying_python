""" Administrador de clientes """

clients = []

# añadimos mock data
# objectos simulador en programación orientada a objectos

marta = {'nombre':'Marta','apellido':'Pérez','dni':'15J'}
clients.append(marta)

# no hace falta crear la variable
# deben tener las mismas claves 
# eso es muy importante
clients.append({'nombre':'Manolo','apellido':'López','dni':'48H'})
clients.append({'nombre':'Ana','apellido':'García','dni':'28Z'})

if __name__ == '__main__':
	print(clients)
