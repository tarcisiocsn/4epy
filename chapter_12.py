# HTTP
# a free book on network architecture

# TCP CONNECTIONS / SOCKETS
# In computer networking, an Internet socket or network socket is an endpoint
# of a bidirectional inter-process communication flow across an Internet
# Protocol-based computer network, such as the internet

# TCP Port Numbers
# - A port is an application-specific or process-specific software communications endpoint;

# - It allows multiple networked applications to coexist on the same server

# - There is a list of well-known TCP port numbers
# Common TCP Ports
# TELNET (23) - Login / SSH (22) - Secure Login / HTTP (80) / HTTPS (443) - Secure
# IMAP(143/220/993) - Mail retrieval / POP (109/110) - Mail Retrieval / DNS (53) - Domain name
# FTP (21) - File transfer

                                #SOCKETS IN PYTHON

# Python has built-in support for TCP sockets

#socket function
# é basicamente uma conexão entre a internet e python
# Since TCP (and python) gives us a reliable socket, what do we want to do with the socket?
# What problem do we want to solve?
# - Aplication Protocols
    # - Mail
    # - World Wide Web

# HTTP - HYPERTEXT TRANSFER PROTOCOL
# what is a protocol?
# A set of rules that all parties follow so we can predict each other's behavior
# And not bump into each other
    # on two-way roads in USA, drive on the righ-hand side of the road
    # on two-way roads in UK, drive on the left-hand side of the road

# An HTTP Request in PYTHON

# Dará um data base do texto com informações do http web browser mais o texto conteúdo da página

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)) < 1:
        break
    print(data.decode(), end = '')
mysock.close()

#                         NETWORKING:  TEXT PROCESSING
# To represent the wide range of character computers must handle we represent
# characters with more than one byte

# UTF - 8 -> 1-4 BYTES ( TYPE OF ENCODING MOST WEBSITE USE)
# in python 3, all strings are Unicode

# PYTHON STRINGS TO BYTES
    # - When we talk to an external resource like a network socket we send bytes,
    # so we need to encode  Python 3 strings into a given character encoding.
    # - When we read data from an external resource. We must decode it based on the
    # character set so it is property represented in python 3 as a string

#                       NETWORKING : USING URLLIB IN PYTHON

# write a webbrowser
# Since HTTP is so common, we have a library that does all the socket work for us
# and makes web pages look like a file

# A mesma coisa que o de cima, mas bem mais soft simple

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

###############

counts = dict()
for line in fhand:
    words = line.decode().split() #coloco decode pq essa linha é bytes e n string
    for word in words:
        counts[words] = counts.get(word, 0) + 1
print(counts)

############

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
