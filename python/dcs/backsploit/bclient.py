import os, sys, socket, threading, subprocess, json, base64, requests, time

HOST = '127.0.0.1'
PORT = 1234
path = os.path.realpath(sys.argv[0])
tmp = os.environ['APPDATA']
