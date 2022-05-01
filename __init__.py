from flask import Flask
app=Flask(__name__)
from core import get_feature
from core import main
from core import process
from core import predict