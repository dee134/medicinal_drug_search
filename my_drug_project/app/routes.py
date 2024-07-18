from flask import render_template, request, redirect, url_for
from . import db
from .models import User, Drug, Store, Inventory, DrugIngredient, Ingredient, PharmaCompany
from flask import current_app as app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        drug_name = request.form['drug_name']
        drugs = Drug.query.filter(Drug.drug_name.ilike(f"{drug_name}%")).all()
        return render_template('search_results.html', drugs=drugs)
    return render_template('search.html')

@app.route('/drug/<int:drug_id>')
def drug_detail(drug_id):
    drug = Drug.query.get_or_404(drug_id)
    ingredients = DrugIngredient.query.filter_by(drug_id=drug_id).all()
    pharma_company = PharmaCompany.query.get(drug.pharma_company_id)
    inventories = Inventory.query.filter_by(drug_id=drug_id).all()
    return render_template('drug_detail.html', drug=drug, ingredients=ingredients, pharma_company=pharma_company, inventories=inventories)
