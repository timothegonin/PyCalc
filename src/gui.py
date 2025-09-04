#!/usr/bin/env python3
"""
Interface graphique moderne avec CustomTkinter
"""

import customtkinter as ctk
import math
from typing import Callable
from .calculator import Calculator


class CalculatorGUI:
    """
    Interface graphique de la calculatrice
    
    Cette classe s'occupe UNIQUEMENT de l'affichage et des interactions utilisateur.
    Tous les calculs sont délégués à la classe Calculator.
    """
    
    def __init__(self):
        # Configuration du thème moderne
        ctk.set_appearance_mode("dark")  # "dark", "light", "system"
        ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"
        
        # Logique métier (séparée !)
        self.calculator = Calculator()
        
        # Interface
        self._setup_window()
        self._create_widgets()
    
    def _setup_window(self) -> None:
        """Configuration de la fenêtre principale"""
        self.root = ctk.CTk()
        self.root.title("🧮 Calculatrice i-gore")
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        
        # Configuration responsive
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
    
    def _create_widgets(self) -> None:
        """Création de tous les widgets de l'interface"""
        self._create_display()
        self._create_buttons()
        self._create_status_bar()
    
    def _create_display(self) -> None:
        """Crée l'écran d'affichage des nombres"""
        self.display_frame = ctk.CTkFrame(self.root, corner_radius=10)
        self.display_frame.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")
        
        # Variable pour l'affichage
        self.display_var = ctk.StringVar(value="0")
        
        # Label d'affichage avec style moderne
        self.display = ctk.CTkLabel(
            self.display_frame,
            textvariable=self.display_var,
            font=ctk.CTkFont(size=32, weight="bold"),
            anchor="e",  # Aligné à droite comme une vraie calculatrice
            width=300,
            height=70
        )
        self.display.pack(padx=15, pady=15)
    
    def _create_buttons(self) -> None:
        """Crée tous les boutons de la calculatrice"""
        self.buttons_frame = ctk.CTkFrame(self.root, corner_radius=10)
        self.buttons_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        
        # Configuration responsive : tous les boutons s'adaptent
        for i in range(5):  # 5 lignes de boutons
            self.buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):  # 4 colonnes
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        
        # Définition des boutons : (texte, ligne, colonne, couleur)
        button_config = [
            # Ligne 0 - Fonctions spéciales
            ("AC", 0, 0, "#ff4444"),   # All Clear - rouge
            ("±", 0, 1, "#666666"),    # Plus/Minus - gris
            ("√", 0, 2, "#666666"),    # Racine carrée - gris
            ("/", 0, 3, "#ff8c00"),    # Division - orange
            
            # Ligne 1 - Chiffres 7-9 et multiplication
            ("7", 1, 0, "#333333"),    # Chiffres - gris foncé
            ("8", 1, 1, "#333333"),
            ("9", 1, 2, "#333333"),
            ("*", 1, 3, "#ff8c00"),    # Multiplication - orange
            
            # Ligne 2 - Chiffres 4-6 et soustraction
            ("4", 2, 0, "#333333"),
            ("5", 2, 1, "#333333"),
            ("6", 2, 2, "#333333"),
            ("-", 2, 3, "#ff8c00"),    # Soustraction - orange
            
            # Ligne 3 - Chiffres 1-3 et addition
            ("1", 3, 0, "#333333"),
            ("2", 3, 1, "#333333"),
            ("3", 3, 2, "#333333"),
            ("+", 3, 3, "#ff8c00"),    # Addition - orange
            
            # Ligne 4 - Zero, virgule, carré et égal
            ("0", 4, 0, "#333333"),
            (".", 4, 1, "#333333"),    # Point décimal
            ("x²", 4, 2, "#666666"),   # Carré
            ("=", 4, 3, "#ff8c00"),    # Égal - orange
        ]
        
        # Création des boutons avec leurs styles
        self.button_widgets = {}
        for text, row, col, color in button_config:
            btn = ctk.CTkButton(
                self.buttons_frame,
                text=text,
                font=ctk.CTkFont(size=18, weight="bold"),
                command=lambda t=text: self._on_button_click(t),
                width=70,
                height=60,
                corner_radius=10,
                fg_color=color,
                hover_color=self._get_hover_color(color)
            )
            
            # Le bouton "0" prend 2 colonnes (comme sur iPhone)
            if text == "0":
                btn.grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky="nsew")
            else:
                btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            
            self.button_widgets[text] = btn
    
    def _create_status_bar(self) -> None:
        """Barre de statut en bas pour les messages"""
        self.status_frame = ctk.CTkFrame(self.root, corner_radius=10, height=40)
        self.status_frame.grid(row=2, column=0, padx=10, pady=(5, 10), sticky="ew")
        
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Prêt",
            font=ctk.CTkFont(size=12)
        )
        self.status_label.pack(pady=10)
    
    def _get_hover_color(self, base_color: str) -> str:
        """Génère une couleur de survol plus claire que la couleur de base"""
        color_map = {
            "#ff4444": "#ff6666",  # Rouge plus clair
            "#ff8c00": "#ffaa33",  # Orange plus clair
            "#666666": "#888888",  # Gris plus clair
            "#333333": "#555555"   # Gris foncé plus clair
        }
        return color_map.get(base_color, "#555555")
    
    def _on_button_click(self, button_text: str) -> None:
        """
        Gestionnaire principal de tous les clics de boutons
        
        Cette méthode fait le pont entre l'interface et la logique métier
        """
        try:
            if button_text.isdigit():
                # Chiffres 0-9
                result = self.calculator.input_number(button_text)
                self._update_display(result)
                self._update_status(f"Nombre saisi : {button_text}")
                
            elif button_text == ".":
                # Point décimal
                result = self.calculator.input_decimal()
                self._update_display(result)
                self._update_status("Point décimal ajouté")
                
            elif button_text in ["+", "-", "*", "/"]:
                # Opérations de base
                result = self.calculator.input_operation(button_text)
                self._update_display(result)
                self._update_status(f"Opération : {button_text}")
                
            elif button_text == "=":
                # Calcul du résultat final
                result = self.calculator.calculate_result()
                self._update_display(result)
                if result == "Erreur":
                    self._update_status("❌ Erreur de calcul")
                else:
                    self._update_status("✅ Résultat calculé")
                
            elif button_text == "AC":
                # All Clear - remise à zéro complète
                self.calculator.reset()
                self._update_display("0")
                self._update_status("🔄 Calculatrice remise à zéro")
                
            elif button_text == "√":
                # Racine carrée (opération immédiate)
                current = float(self.calculator.get_display_value())
                if current < 0:
                    self._update_display("Erreur")
                    self._update_status("❌ Racine de nombre négatif impossible")
                else:
                    result = math.sqrt(current)
                    self.calculator.current_value = str(result)
                    self._update_display(str(result))
                    self._update_status(f"√{current} = {result}")
            
            elif button_text == "x²":
                # Carré (opération immédiate)
                current = float(self.calculator.get_display_value())
                result = current ** 2
                self.calculator.current_value = str(result)
                self._update_display(str(result))
                self._update_status(f"{current}² = {result}")
                
            elif button_text == "±":
                # Changement de signe
                current = float(self.calculator.get_display_value())
                result = -current
                self.calculator.current_value = str(result)
                self._update_display(str(result))
                self._update_status("Signe inversé")
                
        except Exception as e:
            # Gestion d'erreur globale
            self._update_display("Erreur")
            self._update_status(f"❌ Erreur : {str(e)[:30]}")
    
    def _update_display(self, value: str) -> None:
        """Met à jour l'affichage principal"""
        # Limite la longueur pour éviter le débordement
        if len(value) > 12:
            try:
                # Passage en notation scientifique si trop long
                float_value = float(value)
                value = f"{float_value:.4e}"
            except ValueError:
                value = "Erreur"
        
        self.display_var.set(value)
    
    def _update_status(self, message: str) -> None:
        """Met à jour la barre de statut"""
        self.status_label.configure(text=message)
    
    def run(self) -> None:
        """Lance l'application graphique"""
        print("🚀 Lancement de la calculatrice...")
        self.root.mainloop()


# Test rapide si le fichier est lancé directement
if __name__ == "__main__":
    app = CalculatorGUI()
    app.run()