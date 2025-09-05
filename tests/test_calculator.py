#!/usr/bin/env python3
"""
Tests unitaires pour la calculatrice
"""

import pytest
import sys
import os

# Ajoute le dossier src au PATH pour les imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator


class TestCalculator:
    """Tests pour la classe Calculator"""
    
    def setup_method(self):
        """Créé une nouvelle calculatrice avant chaque test"""
        self.calc = Calculator()
    
    def test_initial_state(self):
        """Test de l'état initial"""
        assert self.calc.get_display_value() == "0"
        assert self.calc.previous_value == ""
        assert self.calc.operation is None
    
    def test_input_single_number(self):
        """Test de saisie d'un chiffre"""
        result = self.calc.input_number("5")
        assert result == "5"
        assert self.calc.get_display_value() == "5"
    
    def test_input_multiple_numbers(self):
        """Test de saisie de plusieurs chiffres"""
        self.calc.input_number("1")
        self.calc.input_number("2")
        result = self.calc.input_number("3")
        assert result == "123"
    
    def test_decimal_input(self):
        """Test du point décimal"""
        self.calc.input_number("5")
        result = self.calc.input_decimal()
        assert result == "5."
        
        # Pas de double point
        result2 = self.calc.input_decimal()
        assert result2 == "5."
    
    def test_basic_addition(self):
        """Test addition simple : 5 + 3 = 8"""
        self.calc.input_number("5")
        self.calc.input_operation("+")
        self.calc.input_number("3")
        result = self.calc.calculate_result()
        assert result == "8.0"
    
    def test_basic_subtraction(self):
        """Test soustraction : 10 - 4 = 6"""
        self.calc.input_number("1")
        self.calc.input_number("0")
        self.calc.input_operation("-")
        self.calc.input_number("4")
        result = self.calc.calculate_result()
        assert result == "6.0"
    
    def test_basic_multiplication(self):
        """Test multiplication : 6 * 7 = 42"""
        self.calc.input_number("6")
        self.calc.input_operation("*")
        self.calc.input_number("7")
        result = self.calc.calculate_result()
        assert result == "42.0"
    
    def test_basic_division(self):
        """Test division : 15 / 3 = 5"""
        self.calc.input_number("1")
        self.calc.input_number("5")
        self.calc.input_operation("/")
        self.calc.input_number("3")
        result = self.calc.calculate_result()
        assert result == "5.0"
    
    def test_division_by_zero(self):
        """Test division par zéro"""
        self.calc.input_number("5")
        self.calc.input_operation("/")
        self.calc.input_number("0")
        result = self.calc.calculate_result()
        assert result == "Erreur"
    
    def test_chain_operations(self):
        """Test d'opérations en chaîne : 2 + 3 * 4 (doit faire (2+3)*4 = 20)"""
        self.calc.input_number("2")
        self.calc.input_operation("+")
        self.calc.input_number("3")
        # À ce stade, on a 2+3 en attente
        self.calc.input_operation("*")  # Ceci calcule 2+3=5 et prépare *
        self.calc.input_number("4")
        result = self.calc.calculate_result()  # 5*4 = 20
        assert result == "20.0"
    
    def test_decimal_calculations(self):
        """Test avec des décimaux : 2.5 + 1.5 = 4"""
        self.calc.input_number("2")
        self.calc.input_decimal()
        self.calc.input_number("5")
        self.calc.input_operation("+")
        self.calc.input_number("1")
        self.calc.input_decimal()
        self.calc.input_number("5")
        result = self.calc.calculate_result()
        assert result == "4.0"
    
    def test_reset_functionality(self):
        """Test de la remise à zéro"""
        self.calc.input_number("5")
        self.calc.input_operation("+")
        self.calc.input_number("3")
        
        # Remise à zéro
        self.calc.reset()
        
        # Vérifications
        assert self.calc.get_display_value() == "0"
        assert self.calc.previous_value == ""
        assert self.calc.operation is None


# Tests pour les fonctions spéciales (à ajouter plus tard)
class TestSpecialFunctions:
    """Tests pour les fonctions spéciales (racine, carré...)"""
    
    def setup_method(self):
        self.calc = Calculator()
    
    # Ces tests seront pour les fonctions racine, carré, etc.
    # À implémenter quand on ajoutera ces fonctions
    pass


# Point d'entrée pour lancer les tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])