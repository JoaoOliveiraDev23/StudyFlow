"""
Instância compartilhada do SQLAlchemy.
Separado para evitar importações circulares.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
