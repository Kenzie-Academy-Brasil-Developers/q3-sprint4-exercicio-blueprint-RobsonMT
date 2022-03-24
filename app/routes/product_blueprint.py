
from flask import Blueprint
from app.controllers import product_controller

# Crie a instancia da Bleuprint
bp = Blueprint("products", __name__, url_prefix="/api")

# Crie aqui sua rota get para todos os produtos com a blueprint
bp.get("/products")(product_controller.get_all_product)

# Crie aqui sua rota get para um produto por id com a blueprint
bp.get("/products/<int:product_id>")(product_controller.get_product_by_id)