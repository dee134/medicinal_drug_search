from . import db
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = 'Users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    user_drugs = db.relationship('UserDrug', backref='user', lazy=True)

class DrugIngredient(db.Model):
    __tablename__ = 'DrugIngredients'
    drug_ingredient_id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer, db.ForeignKey('Drugs.drug_id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('Ingredients.ingredient_id'), nullable=False)
    quantity = db.Column(db.Numeric(10, 2))

    # Define relationships
    drug = db.relationship('Drug', back_populates='drug_ingredients')
    ingredient = db.relationship('Ingredient', back_populates='ingredient_drugs')

class Drug(db.Model):
    __tablename__ = 'Drugs'
    drug_id = db.Column(db.Integer, primary_key=True)
    drug_name = db.Column(db.String(100), nullable=False, unique=True)
    drug_description = db.Column(db.String(255))
    manufacture_date = db.Column(db.Date)
    expiry_date = db.Column(db.Date)
    cost = db.Column(db.Numeric(10, 2))
    # number_per_sheet = db.Column(db.Integer)
    # form_id = db.Column(db.Integer, db.ForeignKey('DrugForms.form_id'))
    pharma_company_id = db.Column(db.Integer, db.ForeignKey('PharmaCompanies.pharma_company_id'))

    # Define relationships
    drug_ingredients = db.relationship('DrugIngredient', back_populates='drug')
    pharma_company = db.relationship('PharmaCompany', back_populates='pharma_company_drugs')
    inventories = db.relationship('Inventory', back_populates='drug')

class PharmaCompany(db.Model):
    __tablename__ = 'PharmaCompanies'
    pharma_company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False, unique=True)
    contact_info = db.Column(db.String(255))

    # Define relationships
    pharma_company_drugs = db.relationship('Drug', back_populates='pharma_company')

class Ingredient(db.Model):
    __tablename__ = 'Ingredients'
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(100), nullable=False, unique=True)

    # Define relationships
    ingredient_drugs = db.relationship('DrugIngredient', back_populates='ingredient')

class Store(db.Model):
    __tablename__ = 'Stores'
    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), nullable=False)
    store_address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(20))  # Add this line
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    inventories = db.relationship('Inventory', backref='store', lazy=True)

class Inventory(db.Model):
    __tablename__ = 'Inventory'
    inventory_id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('Stores.store_id'), nullable=False)
    drug_id = db.Column(db.Integer, db.ForeignKey('Drugs.drug_id'), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    # Define relationships
    drug = db.relationship('Drug', back_populates='inventories')

class UserDrug(db.Model):
    __tablename__ = 'User_Drugs'
    user_drug_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    drug_id = db.Column(db.Integer, db.ForeignKey('Drugs.drug_id'), nullable=False)
    search_time = db.Column(db.DateTime, default=datetime.now(timezone.utc))
