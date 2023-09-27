numero_acl = input ("ACL IPv4: ")
if numero_acl.isdigit() and int(numero_acl) >= 1 and int(numero_acl) <= 99: tipo_acl = "ACL Estándar"
elif numero_acl.isdigit() and int(numero_acl) >= 100 and int(numero_acl) <= 199: tipo_acl = "ACL Extendida"
else:
    tipo_acl = "No corresponde a una lista de acceso."
print (f"El número {numero_acl} es una {tipo_acl}.")