#!/usr/bin/env python3
"""
Logique métier de la calculatrice
Sépare la logique des calculs de l'interface utilisateur
"""

import math
from typing import Optional


class Calculator:
    """
    Classe qui gère tous les calculs et l'état de la calculatrice
    
    Principe : Cette classe ne sait RIEN de l'interface graphique.
    Elle peut être utilisée en ligne de commande, dans une app web, etc.
    """
    
    def __init__(self):
        """Initialise une calculatrice vierge"""
        self.reset()
    
    def reset(self) -> None:
        """Remet la calculatrice à zéro"""
        self.current_value = "0"      # Ce qui s'affiche
        self.previous_value = ""      # Valeur précédente pour les calculs
        self.operation = None         # +, -, *, /
        self.wait_for_operand = False # En attente d'un nouveau nombre ?
    
    def input_number(self, number: str) -> str:
        """
        Ajoute un chiffre à la valeur actuelle
        
        Args:
            number: Chiffre de 0 à 9 (en string)
        
        Returns:
            La nouvelle valeur à afficher
        """
        if self.wait_for_operand:
            # Après une opération, on commence un nouveau nombre
            self.current_value = number
            self.wait_for_operand = False
        else:
            # On ajoute le chiffre (sauf si on a juste "0")
            if self.current_value == "0":
                self.current_value = number
            else:
                self.current_value += number
        
        return self.current_value
    
    def input_decimal(self) -> str:
        """
        Ajoute un point décimal si pas déjà présent
        
        Returns:
            La nouvelle valeur à afficher
        """
        if self.wait_for_operand:
            # Nouveau nombre décimal
            self.current_value = "0."
            self.wait_for_operand = False
        elif "." not in self.current_value:
            # Ajoute le point seulement s'il n'y en a pas déjà
            self.current_value += "."
        
        return self.current_value
    
    def input_operation(self, next_operation: str) -> str:
        """
        Traite une opération (+, -, *, /)
        
        Args:
            next_operation: L'opération à effectuer
        
        Returns:
            La valeur à afficher (peut être un résultat intermédiaire)
        """
        current_float = float(self.current_value)
        
        if self.previous_value == "":
            # Premier nombre : on le stocke
            self.previous_value = current_float
        elif self.operation:
            # Il y a déjà une opération en cours : on calcule
            previous_float = float(self.previous_value)
            result = self._perform_calculation(previous_float, current_float, self.operation)
            
            if result is None:
                return "Erreur"
            
            self.current_value = str(result)
            self.previous_value = result
        else:
            self.previous_value = current_float
        
        self.wait_for_operand = True
        self.operation = next_operation
        return self.current_value
    
    def _perform_calculation(self, prev: float, current: float, operation: str) -> Optional[float]:
        """
        Effectue le calcul selon l'opération
        
        Args:
            prev: Valeur précédente
            current: Valeur actuelle
            operation: Opération à effectuer
        
        Returns:
            Le résultat du calcul, ou None si erreur
        """
        try:
            if operation == "+":
                return prev + current
            elif operation == "-":
                return prev - current
            elif operation == "*":
                return prev * current
            elif operation == "/":
                if current == 0:
                    return None  # Division par zéro
                return prev / current
            elif operation == "√":
                if current < 0:
                    return None  # Racine de nombre négatif
                return math.sqrt(current)
            elif operation == "x²":
                return current ** 2
            return None
        except (ValueError, OverflowError, ArithmeticError):
            return None
    
    def calculate_result(self) -> str:
        """
        Calcule et retourne le résultat final
        
        Returns:
            Le résultat final en string, ou "Erreur"
        """
        if self.operation and self.previous_value != "":
            current_float = float(self.current_value)
            previous_float = float(self.previous_value)
            
            result = self._perform_calculation(previous_float, current_float, self.operation)
            if result is None:
                return "Erreur"
            
            self.current_value = str(result)
            self.previous_value = ""
            self.operation = None
            self.wait_for_operand = True
        
        return self.current_value
    
    def get_display_value(self) -> str:
        """Retourne la valeur à afficher (utile pour l'interface)"""
        return self.current_value