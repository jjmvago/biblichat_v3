# Imports necessários
import os
import uuid
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, trim_messages
import streamlit as st

# Carregar variáveis de ambiente
load_dotenv()
