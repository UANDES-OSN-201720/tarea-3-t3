# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 02:05:39 2017

@author: Juan Rodriguez
"""
import socket 
import threading
#Tarea Sistemas operativos y redes

class server():
    def __init__(self):
    #servidor a toda raja
        self.list1 = []
        self.list2 = []
        self.grupos = []
        self.direcciones_grupos = []
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('0.0.0.0', 10000))
        self.s.listen(1)
        print self.s.getsockname()
        
    def inicio(self):
        while True:
            print "kc"
            cliente_soc, address = self.s.accept()
            tr = threading.Thread(target = self.admin_con, args = (cliente_soc))
            tr.start()
            self.list1.append(cliente_soc)
            self.list2.append(address)
            for i in self.list1:
                print i
            
    def send(self, cliente):
        #enviar al cliente la lista de los clientes
        ver = cliente.send(self.list)
        if(ver == 0):
            print(str(cliente) + " no ha podido recibir la lista de las personas.")
            
    def crear_grupo(self):
        print "No olvide agregar su direccion"
        for i in self.list1:
            print str(i)
        a = False
        print "INgrese nombre del grupo: "
        #agregar nombre del grupo a la lista del grupo 
        nom = raw_input()
        self.grupos.append(nom)
        while not a:
            print "Ingrese nombres para agreagr al grupo"
            b = raw_input()
            if b not in self.list1:
                print "Nombre ingresado no existente"
            else:
                self.direcciones_grupos.append(b)
            print "Desea agregar a alguien mas, [y] para si cualquier otra tecla no?"
            c = raw_input()
            if c != "y":
                a = True # sale del ciclo
                
    def admin_con(self, con):
        while True:
            
            #primero para conversacciones privadas
            data = con.recv(4096)
            recp = ""
            a = 0
            while True:
                b = data[a]
                if b != "!":
                    "".join(recp, b)
                else:
                    break
                a += 1
            data = data[a:]
            exist = False
            if recp == "lista":
                self.send(con)
            for i in self.list1:
                b = i.getnameinfo()
                b = str(b[1]) #guarda el puerto donde el servior tiene la conexion
                if b == recp:#para enviar personal
                    i.send(data)
                    exist = True
                    break
                elif b in self.direcciones_grupos:
                    #funcion enviar a los grupos(data)
                    self.send_group(self, data, recp)
            if exist == False:
                print recp + " no existe esa conexion"
                c = "".join("error!No existe la conexixon con ", recp)
                con.send(c)
            if not data:
                break
            
    def send_group(self, data, group):
        for i in self.direcciones_grupos:
            i.send(data)
            
class client():
    def __init__(self):
        self.name #numero de puerto del server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect("0.0.0.0", 10000)
        c = threading.Thread(target=self.listen)
        c.start()
        d = threading.Thread(target=self.write)
        d.start()
    def listen(self):
        while True:
            data = self.s.recv(4096)
            recp =""
            a = 0
            while True:
                b = data[a]
                if b != "!":
                    "".join(recp, b)
                else:
                    break
                a += 1
                data = data[a:]
            if recp == "server":
                #print server message
                print "server: " + data
            elif recp == "error":
                print "Error servidor dice: " + data
            else:
                print recp + ": " + data 
            
    def write(self):
        while True:
            i = raw_input()#ingresar numero y separar con ! del mensaje
            self.s.send(i)
            
server = server()